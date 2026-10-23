import { Song } from "@/context/MuiscPlayerTypes";
import { useMusicPlayer } from "@/context/useMusicPlayer";
import { useEffect, useState } from "react";
import {
    FaPlay,
    FaPause,
    FaStepBackward,
    FaStepForward,
    FaVolumeUp,
} from "react-icons/fa";
import { Input } from "@heroui/react";


export default function MusicPlayerMain({ songs }: { songs: Song[] }) {
    const {currentSong, isPlayling, playSong, togglePlay, audioRef } = useMusicPlayer();
    const [currTime, setCurrTime] = useState(0);
    const [duration, setDuration] = useState(0);
    const [vol, setVolume] = useState(0.7);
    
    const currentIndex = songs.findIndex((song) => song.id === currentSong?.id);

    const playNext = () => {
        if (!songs.length) return;
        const nextIndex = currentIndex < 0 ? 0 : (currentIndex + 1) % songs.length;

        playSong(songs[nextIndex]);
    }

    const playPrev = () => {
        if (!songs.length) return;
        const previousIndex = currentIndex < 0 ? 0 : (currentIndex - 1 + songs.length) % songs.length;

        playSong(songs[previousIndex]);
    }

    const handleVolumeChange = (value: number) => {
        setVolume(value);
    };
    useEffect(() => {
        if(!songs) return;
        const audio = audioRef?.current;
        if (!audio) return;

        const updateTime = () => setCurrTime(audio.currentTime);
        const updatedDuration = () => setDuration(audio.duration || 0);

        audio.addEventListener("timeupdate", updateTime);
        audio.addEventListener("loadedmetadata", updatedDuration);
        audio.addEventListener("durationchange", updatedDuration);



        return () => {
            audio.removeEventListener("timeupdate", updateTime);
            audio.removeEventListener("loadedmetadata", updatedDuration);
            audio.removeEventListener("durationchange", updatedDuration);
        };
    }, [audioRef, currentSong, vol]);


    useEffect(() => {
        if (audioRef?.current) audioRef.current.volume = vol;
    }, [vol, audioRef]);


    const formatTime = (seconds: number) => {
        if (!Number.isFinite(seconds)) return "0:00";
        return `${Math.floor(seconds / 60)}:${Math.floor(seconds % 60).toString().padStart(2, "0")}`;
    }

    if (!currentSong) return null;
    return (
        <footer className="fixed bottom-0 left-0 z-50 w-full border-t border-[#343A31] bg-[#141714]/95 px-4 py-3 text-[#F4F5F0] backdrop-blur-xl rounded-full md:px-6">
            <div className="mx-auto grid max-w-screen-2xl grid-cols-[0.5fr_1fr] items-center gap-4 md:grid-cols-[1fr_1.5fr_1fr]">
                <div className="flex min-w-0 items-center gap-3">
                    <div className={`flex h-12 w-12 shrink-0 items-center justify-center rounded-full bg-linear-to-br from-[#C7F36B] to-[#30392a] text-2xl text-[#090B0A] ${isPlayling ? "animate-spin rounded-full" : ""}`}>
                        ♫
                    </div>

                    <div className="min-w-0">
                        <p className="truncate text-sm font-semibold">
                            {currentSong.title}
                        </p>
                        <p className="truncate text-xs text-[#A8ADA3]">
                            {currentSong.artist}
                        </p>
                    </div>
                </div>
                <div className="flex flex-col items-center gap-2">
                    <div className="flex items-center gap-5">
                        <button
                            onClick={playPrev}
                            aria-label="Previous song"
                            className="text-[#A8ADA3] transition hover:text-[#C7F36B]"
                        >
                            <FaStepBackward />
                        </button>

                        <button
                            onClick={togglePlay}
                            aria-label={isPlayling ? "Pause" : "Play"}
                            className="flex h-9 w-9 items-center justify-center rounded-full bg-[#C7F36B] text-[#090B0A] transition hover:scale-105"
                        >
                            {isPlayling ? <FaPause /> : <FaPlay className="ml-0.5" />}
                        </button>

                        <button
                            onClick={playNext}
                            aria-label="Next song"
                            className="text-[#A8ADA3] transition hover:text-[#C7F36B]"
                        >
                            <FaStepForward />
                        </button>
                    </div>

                    <div className="flex w-full max-w-xl items-center gap-2 text-[10px] text-[#A8ADA3]">
                        <span>{formatTime(currTime)}</span>

                        <Input
                            type="range"
                            min={0}
                            max={duration || 1}
                            value={Math.min(currTime, duration || 1)}
                            onChange={(event) => {
                                const time = Number(event.target.value);
                                if (audioRef?.current) {
                                    audioRef.current.currentTime = time;
                                    setCurrTime(time);
                                }
                            }}
                            aria-label="Song progress"
                            className="h-1 min-w-0 flex-1 cursor-pointer accent-[#C7F36B]"
                        />

                        <span>{formatTime(duration)}</span>
                    </div>
                </div>

                <div className="hidden items-center justify-end gap-3 md:flex">
                    <FaVolumeUp className="text-[#A8ADA3]" />

                    <Input
                        type="range"
                        min={0}
                        max={1}
                        step={0.01}
                        value={vol}
                        onChange={(event) => handleVolumeChange(Number(event.target.value))}
                        aria-label="Volume"
                        className="w-24 cursor-pointer accent-[#C7F36B]"
                    />
                </div>
            </div>
        </footer>
    )
}