import { IoMdHome } from "react-icons/io";
import { IoSave } from "react-icons/io5";
import { FaHeart } from "react-icons/fa";
import Link from "next/link";
import { Avatar } from '@heroui/react';

type Link = {
    name: string,
    icon: React.ReactNode
}

export default function SideBar({ children }: { children: React.ReactNode }) {
    const links: Link[] = [
        {
            name: "Dashboard",
            icon: <IoMdHome size={18} />
        },
        {
            name: "My Playlists",
            icon: <IoSave size={18} />
        },
        {
            name: "Liked Songs",
            icon: <FaHeart size={18} />
        }
    ]
    return (

        <div className="flex flex-row w-full min-h-screen">
            <div className="flex flex-col items-center justify-between w-64 h-[90vh] rounded-2xl fixed left-20 top-[5vh] z-20 bg-[rgb(199,243,107)] py-6">

                <div className="flex flex-col gap-4 w-full px-4">
                    <h1 className="text-xl font-bold text-black px-4 py-4">
                        Music Agent
                    </h1>

                    <div className="flex flex-col gap-2">
                        {links.map((m: Link, index: number) => {
                            const Icon = m.icon;

                            return (
                                <Link
                                    href="/"
                                    key={index}
                                    className="flex flex-row p-4 rounded-2xl items-center text-black gap-4 text-lg hover:bg-black hover:text-[rgb(199,243,107)] transition-colors"
                                >
                                    {Icon}
                                    <span>{m.name}</span>
                                </Link>
                            );
                        })}
                    </div>
                </div>

                <div className="flex flex-row gap-3 items-center text-black px-4">
                    <Avatar>
                        <Avatar.Fallback className="border-none bg-linear-to-tr from-[rgb(199,243,107)] to-black text-white">
                            RC
                        </Avatar.Fallback>
                    </Avatar>
                    <span className="font-medium">Rohan Chatterjee</span>
                </div>

            </div>

            <main className="flex-1 ml-84 p-6">
                {children}
            </main>
        </div>
    )
}