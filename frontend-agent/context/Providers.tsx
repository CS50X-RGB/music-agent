
"use client";

import { MusicPlayerProvider } from "@/context/MusicPlayerContext";

export default function Providers({
    children,
}: {
    children: React.ReactNode;
}) {
    return (
        <MusicPlayerProvider>
            {children}
        </MusicPlayerProvider>
    );
}
