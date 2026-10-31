
"use client";

import {
    useIsFetching,
    useIsMutating,
} from "@tanstack/react-query";

export default function GlobalLoader() {
    const isFetching = useIsFetching();
    const isMutating = useIsMutating();

    const isLoading = isFetching > 0 || isMutating > 0;

    if (!isLoading) return null;

    return (
        <div className="fixed inset-0 z-9999 flex items-center justify-center bg-black/50 backdrop-blur-sm">
            <div className="h-12 w-12 animate-spin rounded-full border-4 border-white/20 border-t-[rgb(199,243,107)]" />
        </div>
    );
}
