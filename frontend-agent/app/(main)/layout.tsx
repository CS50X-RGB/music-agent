import "../globals.css";
import type { Metadata } from "next";
import { Roboto } from "next/font/google";

const roboto = Roboto({
    subsets: ["latin"],
    weight: ["400", "500", "700"],
    variable: "--font-roboto",
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
    <html lang="en" className={roboto.variable} suppressHydrationWarning>
      <body
        className="min-h-full flex flex-col"
        suppressHydrationWarning
      >
        {children}
      </body>
    </html>
  );
}