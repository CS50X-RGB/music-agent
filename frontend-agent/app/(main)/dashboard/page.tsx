import PlaylistCard from "@/components/card/page";
import { Button } from "@heroui/react";

export default function Dashboard() {
    return (
        <>
            <div className="flex flex-col gap-4 p-5">
                <h2 className="text-3xl font-bold">Good Morning,Rohan !</h2>
                <p>Here is what is new for you.</p>
            </div>
            <div className="flex flex-col gap-2 bg-linear-to-tr from-[rgb(199,243,107)] to-black rounded-2xl p-6">
                <h3 className="text-xl font-bold">
                    Create a New Playlist
                </h3>
                <p>Create a new playlist using the artist name and let AI build the perfect playlist for you</p>
                <Button className={"bg-black"}>Generate Playlist -&gt</Button>
            </div>

            <div className="flex flex-row justify-between p-4">
                <h1 className="text-2xl font-bold">Your Playlists</h1>
                <p>View All</p>
            </div>

            <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
                {Array.from({ length: 5 }).map((_, i) => (
                    <PlaylistCard key={i} />
                ))}
            </div>
        </>
    );
}
