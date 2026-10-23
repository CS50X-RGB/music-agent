"use client";

import { useState } from "react";
import type { ReactNode } from "react";
import Link from "next/link";

import { Avatar } from "@heroui/react";
import { IoMdHome, IoMdClose } from "react-icons/io";
import { IoSave } from "react-icons/io5";
import { FaHeart } from "react-icons/fa";
import { RxHamburgerMenu } from "react-icons/rx";

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

    const links: SidebarLink[] = [
        {
            name: "Dashboard",
            href: "/dashboard",
            icon: <IoMdHome size={18} />,
        },
        {
            name: "My Playlists",
            href: "/playlists",
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
        <div className="flex items-center gap-3 px-4 text-black">
            <Avatar>
                <Avatar.Fallback className="border-none bg-black text-[rgb(199,243,107)]">
                    RC
                </Avatar.Fallback>
            </Avatar>

            <span className="font-medium">Rohan Chatterjee</span>
        </div>
    );

    return (
        <div className="flex min-h-screen w-full flex-col md:flex-row">
            <aside className="fixed left-20 top-[5vh] z-20 hidden h-[90vh] w-64 flex-col justify-between rounded-2xl bg-[rgb(199,243,107)] py-6 md:flex">
                <div className="flex w-full flex-col gap-4 px-4">
                    <h1 className="px-4 py-4 text-xl font-bold text-black">
                        Music Agent
                    </h1>

                    {navigation()}
                </div>

                {profile}
            </aside>

            <header className="flex items-center justify-between border-b border-[rgba(199,243,107,0.16)] p-4 md:hidden">
                <h1 className="text-xl font-bold text-accent">
                    Music Agent
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

            <main className="w-64 flex-1 p-4 rounded-xl">
                {children}
            </main>
        </div>
    );
}
