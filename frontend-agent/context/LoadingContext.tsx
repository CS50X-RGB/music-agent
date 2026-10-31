"use client"
import { createContext,useContext,useState,type ReactNode } from "react"

type LoadingCtxType = {
    isLoading : boolean;
    setIsLoading : (value : boolean) => void;
}

const LoadingContext = createContext<LoadingCtxType | undefined>(
    undefined
);

export function LoadingProvider({ children }: { children: ReactNode }) {
    const [isLoading, setIsLoading] = useState(false);

    return (
        <LoadingContext.Provider value={{ isLoading, setIsLoading }}>
            {children}

            {isLoading && (
                <div className="fixed inset-0 z-9999 flex items-center justify-center bg-black/60 backdrop-blur-sm">
                    <div className="h-12 w-12 animate-spin rounded-full border-4 border-white/20 border-t-[rgb(199,243,107)]" />
                </div>
            )}
        </LoadingContext.Provider>
    );
}

export function useLoading() {
    const context = useContext(LoadingContext);

    if (!context) {
        throw new Error("useLoading must be used inside LoadingProvider");
    }

    return context;
}