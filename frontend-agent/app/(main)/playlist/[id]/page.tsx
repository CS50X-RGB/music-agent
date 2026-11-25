"use client";

import { useParams } from "next/navigation";
import { useEffect, useState } from "react";
import { FaPlay, FaPause, FaHeart, FaEllipsisH } from "react-icons/fa";
import { IoTimeOutline } from "react-icons/io5";
import { useMusicPlayer } from "@/context/useMusicPlayer";
import MusicPlayerMain from "@/components/MusicPlayerMain/page";
import { useQuery, useMutation } from "@tanstack/react-query";
import { playlistRouter } from "@/core/api/apiRoutes";
import { postData } from "@/core/api/apiHandler";
import { Heart } from "lucide-react";

export default function Playlist() {
  const params = useParams<{ id: string }>();

  const {
    songs,
    setSongs,
    currentSong: currSong,
    isPlayling: isPlaying,
    playSong: playing,
    togglePlay,
  } = useMusicPlayer();

  const [playlistName, setPlaylistName] = useState<string>("");

  const [likedSongs, setLikedSongs] = useState<number[]>([]);

  const playlistId = params.id;
  const { data, isFetched } = useQuery({
    queryKey: ["songs", playlistId],
    queryFn: async () => {
      const response = await fetch(`/api/session/${playlistId}`, {
        method: "GET",
      });

      if (!response.ok) {
        throw new Error("Failed to few songs");
      }
      return response.json();
    },
    enabled: !!playlistId,
  });

  const likePlaylist = useMutation({
    mutationKey: ["like", playlistId],
    mutationFn: async () => {
      return await postData(playlistRouter.like, {}, { name: playlistName, songs });
    },
  });
  useEffect(() => {
    if (data) {
      setPlaylistName(data.playlist_name);
      setSongs(data.songs);
    }
  }, [data]);

  if (!songs) return null;

  const isPlaylistSong = Boolean(currSong && songs.some((song) => song.ID === currSong.ID));

  const toggleLike = (songId: number) => {
    setLikedSongs((prev) =>
      prev.includes(songId) ? prev.filter((id) => id !== songId) : [...prev, songId],
    );
  };

  const handlePlaylistPlay = () => {
    if (isPlaylistSong) {
      togglePlay();
    } else {
      playing(songs[0]);
    }
  };

  return (
    <>
      <div className="min-h-screen bg-[#090B0A] text-[#F4F5F0]">
        <section className="relative overflow-hidden">
          <div className="absolute inset-0 bg-linear-to-b from-[#414a35] via-[#20251d] to-[#090B0A]" />

          <div className="relative flex flex-col items-start gap-6 px-6 pb-8 pt-10 md:flex-row md:items-end md:gap-8 md:px-10 md:pt-16">
            <div className="flex h-48 w-48 shrink-0 items-center justify-center rounded-xl bg-linear-to-br from-[#C7F36B] via-[#829b49] to-[#20251d] shadow-2xl md:h-60 md:w-60">
              <span className="text-8xl font-bold text-[#090B0A] md:text-9xl">♫</span>
            </div>

            <div className="flex flex-col gap-3">
              <p className="text-sm font-medium">Public Playlist</p>

              <h1 className="text-4xl font-extrabold tracking-tight md:text-6xl">
                {playlistName ?? "Playlist Name"}
              </h1>

              <p className="max-w-xl text-sm text-[#C0C4BB] md:text-base">
                Your personalized music collection, created with Music Agent.
              </p>

              <div className="flex flex-wrap items-center gap-2 text-sm">
                <span className="font-semibold">Music Agent</span>
                <span className="text-[#A8ADA3]">·</span>

                <span className="text-[#A8ADA3]">{songs.length} songs</span>
                <span className="text-[#A8ADA3]">·</span>

                <span className="text-[#A8ADA3]">ID: {playlistId}</span>
              </div>
            </div>
          </div>
        </section>

        <section className="px-6 py-6 pb-32 md:px-10">
          <div className="mb-8 flex items-center gap-5">
            <button
              onClick={handlePlaylistPlay}
              aria-label={isPlaylistSong && isPlaying ? "Pause playlist" : "Play playlist"}
              className="flex h-14 w-14 items-center justify-center rounded-full bg-[#C7F36B] text-xl text-[#090B0A] transition hover:scale-105 hover:bg-[#d5ff80]"
            >
              {isPlaylistSong && isPlaying ? <FaPause /> : <FaPlay className="ml-1" />}
            </button>
            <Heart size={20} onClick={() => likePlaylist.mutate()} />
            <button
              aria-label="More playlist options"
              className="text-2xl text-[#A8ADA3] transition hover:text-white"
            >
              <FaEllipsisH />
            </button>
          </div>

          <div className="w-full">
            <div className="grid grid-cols-[32px_minmax(0,1fr)_80px] items-center gap-4 border-b border-[#343A31] px-4 py-3 text-sm text-[#A8ADA3] md:grid-cols-[40px_minmax(0,1fr)_minmax(120px,1fr)_100px]">
              <span>#</span>
              <span>Title</span>
              <span className="hidden md:block">Reason</span>

              <span className="flex items-center justify-end">
                <IoTimeOutline size={20} />
              </span>
            </div>

            <div className="mt-2 flex flex-col">
              {songs.map((song, index) => {
                const isLiked = likedSongs.includes(song.ID);
                const isCurrentSong = currSong?.ID === song.ID;
                return (
                  <div
                    key={song.ID}
                    className="group grid grid-cols-[32px_minmax(0,1fr)_80px] items-center gap-4 rounded-lg px-4 py-3 transition hover:bg-[#1B201A] md:grid-cols-[40px_minmax(0,1fr)_minmax(120px,1fr)_100px]"
                  >
                    <div className="flex items-center justify-center">
                      <span
                        className={`text - sm ${
                          isCurrentSong ? "text-[#C7F36B]" : "text-[#A8ADA3]"
                        } group - hover: hidden`}
                      >
                        {isCurrentSong && isPlaying ? "♫" : index + 1}
                      </span>
                      <button
                        onClick={() => playing(song)}
                        aria-label={
                          isCurrentSong && isPlaying
                            ? `Pause ${song.Title} `
                            : `Play ${song.Title} `
                        }
                        className="hidden text-white group-hover:block"
                      >
                        {isCurrentSong && isPlaying ? <FaPause size={12} /> : <FaPlay size={12} />}
                      </button>
                    </div>
                    <div className="flex min-w-0 items-center gap-3">
                      <div className="flex h-12 w-12 shrink-0 items-center justify-center rounded-md bg-linear-to-br from-[#30392a] to-[#151914] text-xl text-[#C7F36B]">
                        ♫
                      </div>

                      <div className="min-w-0">
                        <p
                          className={`truncate font - medium transition ${
                            isCurrentSong
                              ? "text-[#C7F36B]"
                              : "text-[#F4F5F0] group-hover:text-[#C7F36B]"
                          } `}
                        >
                          {song.Title}
                        </p>

                        <p className="truncate text-sm text-[#A8ADA3]">{song.Artist}</p>
                      </div>
                    </div>
                    <span className="hidden truncate text-sm text-[#A8ADA3] md:block">
                      {song.Reason}
                    </span>
                    <div className="flex items-center justify-end gap-3">
                      <button
                        onClick={() => toggleLike(song.ID)}
                        aria-label={isLiked ? `Unlike ${song.Title} ` : `Like ${song.Title} `}
                        className={`transition ${
                          isLiked
                            ? "text-[#C7F36B]"
                            : "text-transparent group-hover:text-[#A8ADA3] hover:text-[#C7F36B]"
                        } `}
                      >
                        <FaHeart size={15} />
                      </button>
                      <span className="text-sm text-[#A8ADA3]">{song.Duration}</span>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
          <div className="mt-8 border-t border-[#343A31] pt-5">
            <p className="text-sm text-[#A8ADA3]">Made for you by Music Agent</p>
          </div>
        </section>
      </div>
      <MusicPlayerMain songs={songs} />
    </>
  );
}
