import { IoMdHome } from "react-icons/io";
import { IoSave } from "react-icons/io5";
import { FaHeart } from "react-icons/fa";

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
        <>
            <div className="flex flex-col items-center gap-2 w-1/8 h-[90vh] rounded-2xl absolute left-20 z-20 bg-[rgba(199,243,107)]">
                <h1 className="text-xl font-bold text-black p-8">
                    [Music Agent]
                </h1>
                {links.map((m: Link, index: number) => {
                    const Icon = m.icon;
                    return (
                        <div key={index} className="flex flex-row justify-around text-black gap-4 text-xl">
                            {Icon}
                            <h1 className="text-black">{m.name}</h1>
                        </div>
                    );
                })}
            </div>
            {children}
        </>
    )
}