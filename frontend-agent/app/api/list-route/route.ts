import { NextRequest, NextResponse } from "next/server";
import { writeFile, mkdir } from "fs/promises";
import path from "path";

export async function POST(req: NextRequest) {
    try {
        const data: {
            session_id: string;
            [key: string]: unknown;
        } = await req.json();

        const { session_id } = data;

        if (!session_id || !/^[a-zA-Z0-9_-]+$/.test(session_id)) {
            return NextResponse.json(
                { error: "Invalid session_id" },
                { status: 400 }
            );
        }

        const jsonDir = path.join(process.cwd(), "json");

        await mkdir(jsonDir, { recursive: true });

        const filePath = path.join(jsonDir, `${session_id}.json`);

        await writeFile(filePath, JSON.stringify(data), "utf-8");

        return NextResponse.json({ session_id });

    } catch (error) {
        console.error(error);

        return NextResponse.json(
            { error: "Unable to save playlist" },
            { status: 500 }
        );
    }
}