"use client";

import { useEffect, useState } from "react";
import type { ReactNode } from "react";
import Link from "next/link";

import { Avatar } from "@heroui/react";
import { IoMdHome, IoMdClose } from "react-icons/io";
import { IoSave } from "react-icons/io5";
import { FaHeart } from "react-icons/fa";
import { RxHamburgerMenu } from "react-icons/rx";
import { IoLogOut } from "react-icons/io5";
import { clientToken, currentUser } from "@/core/api/localStorageKeys";
import { useRouter } from "next/navigation";
import { User } from "@/types/states";
import { queryClient } from "@/context/Providers";
import { getData } from "@/core/api/apiHandler";
import { accountRoutes } from "@/core/api/apiRoutes";
import { useQuery } from "@tanstack/react-query";


type SidebarLink = {
    name: string;
    href: string;
    icon: ReactNode;
};

export default function SideBar({
    children,
}: {
    children: ReactNode;
}) {
    const [isMenuOpen, setIsMenuOpen] = useState(false);
    const router = useRouter();

    const handleLogout = () => {
        localStorage.removeItem(clientToken);
        localStorage.removeItem(currentUser);
        router.push('/login');
    };

    const { data: profileValue, isLoading } = useQuery({
        queryKey: ["get-profile"],
        queryFn: () => getData(accountRoutes.profile, {}),
    });


    const links: SidebarLink[] = [
        {
            name: "Dashboard",
            href: "/dashboard",
            icon: <IoMdHome size={18} />,
        },
        {
            name: "My Playlists",
            href: "/playlists/1",
            icon: <IoSave size={18} />,
        },
        {
            name: "Liked Songs",
            href: "/liked-songs",
            icon: <FaHeart size={18} />,
        },
    ];

    const navigation = (mobile = false) => (
        <nav className="flex flex-col gap-2">
            {links.map((item) => (
                <Link
                    key={item.name}
                    href={item.href}
                    onClick={() => {
                        if (mobile) setIsMenuOpen(false);
                    }}
                    className="flex items-center gap-4 rounded-2xl p-4 text-lg text-black transition-colors hover:bg-black hover:text-[rgb(199,243,107)]"
                >
                    {item.icon}
                    <span>{item.name}</span>
                </Link>
            ))}
        </nav>
    );
    const profile = (
        <div className="px-4">
            {isLoading ? (
                <div className="flex animate-pulse items-center gap-3">
                    <div className="h-10 w-10 rounded-full bg-black/20" />

                    <div className="flex-1 space-y-2">
                        <div className="h-3 w-24 rounded bg-black/20" />
                        <div className="h-2 w-16 rounded bg-black/10" />
                    </div>

                    <div className="h-8 w-8 rounded-lg bg-black/10" />
                </div>
            ) : (
                <div className="flex items-center gap-3 text-black">
                    <Avatar>
                        <Avatar.Fallback className="border-none bg-black text-[rgb(199,243,107)]">
                            {profileValue?.data?.name
                                ?.split(" ")
                                .map((word: string) => word[0])
                                .join("")
                                .slice(0, 2)
                                .toUpperCase() || "U"}
                        </Avatar.Fallback>
                    </Avatar>

                    <span className="min-w-0 flex-1 truncate font-medium">
                        {profileValue?.data?.name ?? "Guest"}
                    </span>

                    <button
                        type="button"
                        onClick={handleLogout}
                        aria-label="Logout"
                        title="Logout"
                        className="rounded-lg p-2 transition-colors hover:bg-black/10"
                    >
                        <IoLogOut size={20} />
                    </button>
                </div>
            )}
        </div>
    );

    return (
        <div className="flex min-h-screen w-full flex-col md:flex-row">
            <aside className="fixed left-20 top-[5vh] z-20 hidden h-[90vh] w-64 flex-col justify-between rounded-2xl bg-[rgb(199,243,107)] py-6 md:flex">
                <div className="flex w-full flex-col gap-4 px-4">
                    <h1 className="px-4 py-4 text-xl font-bold text-black">
                        [Music Agent]
                    </h1>

                    {navigation()}
                </div>

                {profile}
            </aside>

            <header className="flex items-center justify-between border-b border-[rgba(199,243,107,0.16)] p-4 md:hidden">
                <h1 className="text-xl font-bold text-accent">
                    [Music Agent]
                </h1>

                <button
                    type="button"
                    onClick={() => setIsMenuOpen((prev) => !prev)}
                    aria-label={isMenuOpen ? "Close menu" : "Open menu"}
                    aria-expanded={isMenuOpen}
                    className="rounded-lg p-2 text-accent transition-colors hover:bg-white/10"
                >
                    {isMenuOpen ? (
                        <IoMdClose size={26} />
                    ) : (
                        <RxHamburgerMenu size={26} />
                    )}
                </button>
            </header>

            {isMenuOpen && (
                <div
                    className="fixed inset-0 z-50 bg-black/60 md:hidden"
                    onClick={() => setIsMenuOpen(false)}
                >
                    <aside
                        className="flex h-full w-72 max-w-[85vw] flex-col justify-between overflow-y-auto bg-[rgb(199,243,107)] p-5"
                        onClick={(e) => e.stopPropagation()}
                    >
                        <div>
                            <div className="mb-8 flex items-center justify-between">
                                <h2 className="text-xl font-bold text-black">
                                    Music Agent
                                </h2>

                                <button
                                    type="button"
                                    onClick={() => setIsMenuOpen(false)}
                                    aria-label="Close menu"
                                    className="rounded-lg p-2 text-black hover:bg-black/10"
                                >
                                    <IoMdClose size={24} />
                                </button>
                            </div>

                            {navigation(true)}
                        </div>

                        {profile}
                    </aside>
                </div>
            )}

            <main className="w-full md:w-64 flex-1 md:ml-84 p-4 rounded-xl">
                {children}
            </main>
        </div>
    );
}
