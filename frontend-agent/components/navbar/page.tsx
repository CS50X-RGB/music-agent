'use client'
import { Avatar, Button } from "@heroui/react";
import React from "react";
import SideBar from "../Sidebar/page";
import { usePathname, useRouter } from "next/navigation";
import useAuth from "@/hooks/useAuth";


export default function Navbar({ children }: { children: React.ReactNode }) {
    const pathname = usePathname();
    const {accountData,isLoading,isError,error} = useAuth();
    const router = useRouter();

    if (pathname.includes('dashboard') || pathname.includes('generate') || pathname.includes('playlist'))
        return (
            <>
                <SideBar>
                    {children}
                </SideBar>
            </>
        )
    else
        return (
            <>
                <nav className="flex w-full flex-row items-center justify-between p-3">
                    <div className="flex flex-row items-center gap-2">
                        <h1 onClick={() => router.push("/")} className="text-xl font-bold text-accent">
                            [Music Agent]
                        </h1>
                    </div>
                    {!(pathname.includes('login') || pathname.includes('register')) && !accountData && (
                        <div className="flex flex-end gap-2">
                            <Button size="md" className={"text-black"} onPress={() => router.push("/login")}>Login</Button>
                            <Button size="md" className={"text-black"} onPress={() => router.push("/register")}>Register</Button>
                        </div>
                    )}
                    {pathname.includes('/') && !error && (
                    <Avatar>
                        <Avatar.Fallback className="border-none text-black bg-[rgb(199,243,107)]">
                            {accountData?.data.name
                                ?.split(" ")
                                .map((word: string) => word[0])
                                .join("")
                                .slice(0, 2)
                                .toUpperCase() || "U"}
                        </Avatar.Fallback>
                    </Avatar>
                )}

                </nav>
                <div className="flex flex-col p-8  items-center gap-4">
                    {children}
                </div>
            </>
        )
}