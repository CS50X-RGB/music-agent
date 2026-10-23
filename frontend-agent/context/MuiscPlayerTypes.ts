export type Song = {
    id: number,
    title: string,
    artist: string,
    album: string,
    duration: string,
    audioUrl: string,
    cover?: string
}

export type MusicPlayerContextType = {
    songs: Song[] | null,
    currentSong: Song | null,
    setSongs: React.Dispatch<React.SetStateAction<Song[]>>;
    isPlayling: boolean,
    playSong: (song: Song) => void,
    togglePlay: () => void,
    audioRef: React.RefObject<HTMLAudioElement | null>;
}
