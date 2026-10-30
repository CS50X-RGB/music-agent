
"use client";
import {
  QueryClient,
  QueryClientProvider,
} from '@tanstack/react-query'
import { MusicPlayerProvider } from "@/context/MusicPlayerContext";
import { Toast } from '@heroui/react';

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
                <Toast.Provider placement='top end' />
            </MusicPlayerProvider>
        </QueryClientProvider>
    );
}
