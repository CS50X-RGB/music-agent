import { Manrope } from "next/font/google";
import "../globals.css";
import type { Metadata } from "next";

const manrope = Manrope({
    subsets: ["latin"],
    variable: "--font-manrope",
    display: "swap",
});

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
        <html lang="en" className={manrope.variable}>
            <body
                className="min-h-full flex flex-col p-8"
                suppressHydrationWarning
            >
                <div className="flex flex-row items-center gap-2">
                    <h1 className="text-xl font-bold text-accent">
                        Music Agent
                    </h1>
                </div>
                <section className="flex min-h-[70vh] flex-col items-center justify-center gap-6 px-4 text-center">
                    {children}
                </section>
            </body>
        </html>
    );
}