'use client'

import PlaylistCard from "@/components/card/page";
import { getData } from "@/core/api/apiHandler";
import { accountRoutes } from "@/core/api/apiRoutes";
import { Button, Skeleton } from "@heroui/react";
import { useQuery } from "@tanstack/react-query";

export default function Dashboard() {
    const { data: getProfile, isLoading } = useQuery({
        queryKey: ['get-profile'],
        queryFn: () => getData(accountRoutes.profile, {})
    });
    const getGreeting = () => {
        const hour = new Date().getHours();
        if(hour >=5  && hour < 12) return "Good Morning";
        if(hour >= 12 && hour < 17) return "Good Afternoon";
        if(hour >= 17 && hour < 20) return "Good Evening"
        return "Good Night"
    }

    if (isLoading) {
        return (
            <div className="flex flex-col gap-6 p-5 animate-pulse">
                <div className="flex flex-col gap-3">
                    <Skeleton className="w-72 rounded-lg">
                        <div className="h-9 rounded-lg bg-default-300" />
                    </Skeleton>

                    <Skeleton className="w-56 rounded-lg">
                        <div className="h-4 rounded-lg bg-default-300" />
                    </Skeleton>
                </div>
                <Skeleton className="rounded-2xl">
                    <div className="h-44 rounded-2xl bg-default-300" />
                </Skeleton>
                <div className="flex justify-between items-center">
                    <Skeleton className="w-40 rounded-lg">
                        <div className="h-7 rounded-lg bg-default-300" />
                    </Skeleton>

                    <Skeleton className="w-16 rounded-lg">
                        <div className="h-5 rounded-lg bg-default-300" />
                    </Skeleton>
                </div>
                <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
                    {Array.from({ length: 5 }).map((_, i) => (
                        <div key={i} className="flex flex-col gap-3">
                            <Skeleton className="rounded-xl">
                                <div className="h-40 rounded-xl bg-default-300" />
                            </Skeleton>

                            <Skeleton className="w-3/4 rounded-lg">
                                <div className="h-4 rounded-lg bg-default-300" />
                            </Skeleton>

                            <Skeleton className="w-1/2 rounded-lg">
                                <div className="h-3 rounded-lg bg-default-300" />
                            </Skeleton>
                        </div>
                    ))}
                </div>
            </div>
        );
    }
    return (
    
        <>
            <div className="flex flex-col gap-4 p-5">
                <h2 className="text-3xl font-bold">
                    {getGreeting()}, {getProfile?.data?.name}!
                </h2>
                <p>Here is what is new for you.</p>
            </div>

            <div className="flex flex-col gap-2 bg-linear-to-tr from-[rgb(199,243,107)] to-black rounded-2xl p-6">
                <h3 className="text-xl font-bold">Create a New Playlist</h3>
                <p>Create a new playlist using the artist name and let AI build the perfect playlist for you</p>
                <Button className="bg-black">Generate Playlist -&gt;</Button>
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