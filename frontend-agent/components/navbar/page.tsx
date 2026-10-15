import { Button } from "@heroui/react";
import React from "react";

export default function Navbar({ children }: { children: React.ReactNode }) {
    return (
        <>
            <nav className="flex w-full flex-row items-center justify-between p-3">
                <div className="flex flex-row items-center gap-2">
                    <h1 className="text-xl font-bold text-accent">
                        Music Agent
                    </h1>
                </div>
                <Button size="lg" className={"text-black"}>Login</Button>
            </nav>
            <div className="flex flex-col p-8 items-center gap-4">
                {children}
            </div>
        </>
    )
}