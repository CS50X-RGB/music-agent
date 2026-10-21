
"use client";

import { Card } from "@heroui/react";
import Image from "next/image";
import { Play } from "lucide-react";

export default function PlaylistCard() {
    return (
        <Card className="w-64 rounded-2xl gap-3 p-3 bg-zinc-900 border border-zinc-800">
            <Card.Header className="relative w-full">
                <Image
                    alt="Chill Vibes playlist cover"
                    className="pointer-events-none aspect-square w-full rounded-xl object-cover select-none"
                    loading="lazy"
                    width={400}
                    height={400}
                    src="https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/docs/demo1.jpg"
                />

                <button
                    type="button"
                    aria-label="Play Chill Vibes playlist"
                    className="absolute bottom-3 right-3 flex h-12 w-12 items-center justify-center rounded-full bg-[rgb(199,243,107)] text-black shadow-lg transition-transform hover:scale-110"
                    onClick={() => console.log("Play Chill Vibes")}
                >
                    <Play size={22} fill="currentColor" />
                </button>
            </Card.Header>

            <Card.Content className="flex flex-col gap-1">
                <h3 className="text-lg font-semibold text-white">
                    Chill Vibes
                </h3>

                <p className="text-sm text-zinc-400">
                    12 songs - 80 mins
                </p>
            </Card.Content>
        </Card>
    );
}
