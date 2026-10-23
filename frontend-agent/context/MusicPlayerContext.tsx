"use client"

import { createContext, useEffect, useRef, useState, type ReactNode } from "react"
import { MusicPlayerContextType, Song } from "./MuiscPlayerTypes";

export const MusicPlayerContext = createContext<MusicPlayerContextType | null>(null);

export function MusicPlayerProvider({
    children
}: { children: ReactNode }) {
     const [songs, setSongs] = useState<Song[]>([]);
    const audioRef = useRef<HTMLAudioElement>(null);
    const [currSong, setCurrSong] = useState<Song | null>(null);
    const [isPlaying, setIsPlaying] = useState(false);

    const playing = (song: Song) => {
        if (currSong?.id === song.id) {
            setIsPlaying(isPlaying);
            return;
        }
        setCurrSong(song);
        setIsPlaying(true);
    }

    const togglePlay = () => {
        if (currSong)
            setIsPlaying((prev) => !prev);
    }

    const playNextSongs = () => {
        if(!songs || !currSong) return;

        const currentIndex = songs.findIndex((song) => song.id === currSong.id);

        if(currentIndex === -1) return;

        const nextSong = songs[currentIndex + 1];

        if(nextSong) playing(nextSong)
        else setIsPlaying(false);
    }


    useEffect(() => {
        const audio = audioRef.current;
        if (!audio || !currSong) return;
        if (isPlaying) {
            audio.play().catch((err) => {
                setIsPlaying(false);
                console.log(err)
            });
        } else {
            audio.pause();
        }
    }, [currSong, isPlaying])


    return (
        <MusicPlayerContext.Provider
            value={{
                currentSong: currSong,
                isPlayling: isPlaying,
                setSongs,
                playSong: playing,
                togglePlay,
                audioRef,
                songs
            }}
        >
            {children}
            <audio ref={audioRef} src={currSong?.audioUrl} preload="metadata" onEnded={playNextSongs} />
        </MusicPlayerContext.Provider>
    )
}

