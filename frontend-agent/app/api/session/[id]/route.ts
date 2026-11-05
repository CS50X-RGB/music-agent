import { NextResponse } from "next/server";
import fs from "fs/promises";
import path from "path";

export async function GET(
    req: Request,
    { params }: { params: Promise<{ id: string }> }
) {
    const { id } = await params;

    if (!/^[a-zA-Z0-9_-]+$/.test(id)) {
        return NextResponse.json({ error: "Invalid ID" }, { status: 400 });
    }

    const filePath = path.join(process.cwd(), "json", `${id}.json`);

    try {
        const raw = await fs.readFile(filePath, "utf-8");
        const data = JSON.parse(raw);

        await fs.unlink(filePath);

        return NextResponse.json({
            songs: data.songs
        });
    } catch {
        return NextResponse.json(
            { error: "File not found" },
            { status: 404 }
        );
    }
}