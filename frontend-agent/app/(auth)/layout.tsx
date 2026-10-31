import "../globals.css";
import type { Metadata } from "next";


export const metadata: Metadata = {
    title: {
        default: "MusicAgent — Your Mood, Your Music",
        template: "%s | MusicAgent",
    },
    description: "Create personalized AI-powered playlists based on your mood, taste, and musical style.",
    applicationName: "MusicAgent",
};

export default function RootLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <div className="min-h-full flex flex-col p-8">
            <section className="flex min-h-[70vh] flex-col items-center justify-center gap-6 px-4 text-center">
                {children}
            </section>
        </div>
    );
}