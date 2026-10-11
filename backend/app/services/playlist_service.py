from uuid import UUID
from sqlalchemy.orm import Session
from app.model.playlist import Playlist,PlaylistSong
from app.repositories.playlist_repository import PlaylistRepo
from app.schemas.playlist import PlaylistCreate

class PlaylistService:
    def __init__(self):
        self.repo = PlaylistRepo()
        
    def create_playlist(
        self,
        db: Session,
        user : str,
        data: PlaylistCreate,
    ) -> Playlist:
        playlist = Playlist(
            user_id=user,
            name=data.name,
            original_prompt=data.original_prompt,
            songs=[
                PlaylistSong(
                    title=song.title,
                    artist=song.artist,
                    reason=song.reason,
                    url=song.url,
                    embed_url=song.embed_url,
                    position=index,
                )
                for index, song in enumerate(data.songs)
            ],
        )

        return self.repository.create(db, playlist)
    
    def get_playlist(self,db : Session,playlist_id : UUID) -> Playlist | None:
        return self.repo.get_by_id(db,playlist_id)

    def get_playlists_by_user_id(self,db : Session,user_id : UUID) -> list[Playlist] | None:
        return self.repo.get_all(db,user_id)