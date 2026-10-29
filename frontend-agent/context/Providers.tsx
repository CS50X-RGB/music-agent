
"use client";
import {
  QueryClient,
  QueryClientProvider,
} from '@tanstack/react-query'
import { MusicPlayerProvider } from "@/context/MusicPlayerContext";


export const queryClient = new QueryClient()
export default function Providers({
    children,
}: {
    children: React.ReactNode;
}) {
    return (
        <QueryClientProvider client={queryClient}>
            <MusicPlayerProvider>
                {children}
            </MusicPlayerProvider>
        </QueryClientProvider>
    );
}
