import { Manrope } from "next/font/google";
import "./globals.css";
import type { Metadata } from "next";
import Providers from "@/context/Providers"
import Navbar from "@/components/navbar/page";
import { Suspense } from "react";
import { LoadingProvider } from "@/context/LoadingContext";
import GlobalLoader from "@/context/GloablLoader";

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
        <Providers>
          <Suspense fallback={<div className="h-16" />}>
          <GlobalLoader />
            <Navbar>
                {children}
            </Navbar>
          </Suspense>
        </Providers>
      </body>
    </html>
  );
}