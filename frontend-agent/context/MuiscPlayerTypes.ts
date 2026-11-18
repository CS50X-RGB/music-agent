export type Song = {
  ID: number;
  Title: string;
  Artist: string;
  Reason: string;
  Duration: string;
  AudioUrl: string;
};

export type MusicPlayerContextType = {
  songs: Song[] | null;
  currentSong: Song | null;
  setSongs: React.Dispatch<React.SetStateAction<Song[]>>;
  isPlayling: boolean;
  playSong: (song: Song) => void;
  togglePlay: () => void;
  audioRef: React.RefObject<HTMLAudioElement | null>;
};
