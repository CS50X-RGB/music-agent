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
        className="min-h-full flex flex-col"
        suppressHydrationWarning
      >
        {children}
      </body>
    </html>
  );
}