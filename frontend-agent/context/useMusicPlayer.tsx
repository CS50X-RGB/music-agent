import { useContext } from "react";
import { MusicPlayerContext } from "./MusicPlayerContext";
export function useMusicPlayer() {

    const ctx = useContext(MusicPlayerContext);

    if (!ctx) throw new Error("useMusicPlayer must be used inside MusicPlayerProvider");

    return ctx;
}