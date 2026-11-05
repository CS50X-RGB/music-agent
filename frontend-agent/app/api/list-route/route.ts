import { NextRequest, NextResponse } from "next/server";
import { writeFile } from "fs/promises";
import path from "path";
import os from "os";


export async function POST(req: NextRequest) {
    try {
        const data : { session_id : string;[key : string] : unknown } = await req.json();
        console.log(data)
        const { session_id } =  data
        const filePath = path.join(os.tmpdir(), `${session_id}.json`);

        await writeFile(filePath, JSON.stringify(data), "utf-8");

        return NextResponse.json({ session_id });
    } catch {
        return NextResponse.json(
            { error: "Unable to save playlist" },
            { status: 500 }
        );
    }
}