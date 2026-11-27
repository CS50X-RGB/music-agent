from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from agent.app.aws.s3 import s3
from backend.app.model.playlist import Playlist, PlaylistSong
from backend.app.repositories.playlist_repository import PlaylistRepo
from backend.app.schemas.playlist import PlaylistAll, PlaylistCreate


class PlaylistService:
    def __init__(self):
        self.repo = PlaylistRepo()
        self.s3 = s3

    def create_playlist(
        self,
        db: Session,
        user: UUID,
        data: PlaylistCreate,
    ) -> Playlist:
        playlist = Playlist(
            user_id=user,
            name=data.name,
            songs=[
                PlaylistSong(
                    title=song.Title,
                    album_cover=song.album_cover,
                    artist=song.Artist,
                    reason=song.Reason,
                    duration=song.Duration,
                    url=song.AudioUrl,
                    position=index,
                )
                for index, song in enumerate(data.songs)
            ],
        )
        # saving to aws saved state
        self.s3.move_session_to_saved(data.session_id)

        return self.repo.create(db, playlist)

    def get_playlist(self, db: Session, playlist_id: UUID) -> Playlist | None:
        stmt = (
            select(Playlist)
            .where(Playlist.id == playlist_id)
            .options(selectinload(Playlist.songs))
        )

        result = db.execute(stmt)
        playlist = result.scalars().first()

        return playlist

    def get_playlists_by_user_id(self, db: Session, user_id: UUID) -> list[PlaylistAll]:
        stmt = (
            select(Playlist)
            .where(Playlist.user_id == user_id)
            .options(selectinload(Playlist.songs))
        )

        playlists = db.execute(stmt).scalars().all()

        return [
            PlaylistAll(
                name=playlist.name,
                session_id=playlist.id,
                total_duration=self.calculate_playlist_duration(playlist.songs),
                total_songs=len(playlist.songs),
            )
            for playlist in playlists
        ]

    def calculate_playlist_duration(self, songs) -> int:
        total_seconds = 0

        for song in songs:
            minutes, seconds = map(int, song.duration.split(":"))
            total_seconds += minutes * 60 + seconds

        return total_seconds // 60
