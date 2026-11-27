import { NextResponse } from "next/server";
import fs from "fs/promises";
import path from "path";
import { parseBuffer } from "music-metadata";

export async function GET(req: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;

  if (!/^[a-zA-Z0-9_-]+$/.test(id)) {
    return NextResponse.json({ error: "Invalid ID" }, { status: 400 });
  }

  const filePath = path.join(process.cwd(), "json", `${id}.json`);

  try {
    const raw = await fs.readFile(filePath, "utf-8");
    const data = JSON.parse(raw);

    const songs = await Promise.all(
      data.songs.map(async (song: any) => {
        try {
          const response = await fetch(song.AudioUrl);
          if (!response.ok) return { ...song, artwork: null };
          const buffer = Buffer.from(await response.arrayBuffer());
          const metadata = await parseBuffer(buffer, { mimeType: "audio/mpeg" });
          const picture = metadata.common.picture?.[0];
          console.log(picture);
          if (picture) {
            const base64 = btoa(
              new Uint8Array(picture.data).reduce(
                (data, byte) => data + String.fromCharCode(byte),
                "",
              ),
            );

            const artwork = `data:${picture.format};base64,${base64}`;
            return { ...song, album_cover: artwork };
          }
        } catch {
          return { ...song, album_cover: null };
        }
      }),
    );

    //   await fs.unlink(filePath);

    return NextResponse.json({
      songs: songs,
      playlist_name: data.playlist_name,
    });
  } catch {
    return NextResponse.json({ error: "File not found" }, { status: 404 });
  }
}
