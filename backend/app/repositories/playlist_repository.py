from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.app.model.playlist import Playlist, PlaylistSong


class PlaylistRepo:
    def create(self, db: Session, playlist: Playlist) -> Playlist:
        try:
            db.add(playlist)
            db.commit()
            db.refresh(playlist)
            return playlist
        except Exception:
            db.rollback()
            raise

    def get_by_id(self, db: Session, playlist_id: UUID) -> Playlist | None:
        return db.get(Playlist, playlist_id)

    def get_all(self, db: Session, user_id: UUID) -> list[Playlist]:
        statement = (
            select(Playlist)
            .where(Playlist.user_id == user_id)
            .order_by(Playlist.created_at.desc())
        )
        return list(db.scalars(statement=statement).all())

    def update(self, db: Session, playlist_id: UUID, updates: dict) -> Playlist | None:
        playlist = db.get(Playlist, playlist_id)

        if playlist is None:
            return None

        for field, value in updates.items():
            if field in {"name", "original_prompt", "status"}:
                setattr(playlist, field, value)

    def delete(self, db: Session, playlist_id: UUID) -> bool:
        playlist = db.get(Playlist, playlist_id)

        if playlist is None:
            return False

        try:
            db.delete(playlist)
            db.commit()
            return True
        except Exception:
            db.rollback()
            raise


class PlaylistSongRepo:
    def create(self, db: Session, song: PlaylistSong) -> PlaylistSong:
        try:
            db.add(song)
            db.commit()
            db.refresh(song)
            return song
        except Exception:
            db.rollback()
            raise

    def add_to_playlist(
        self,
        db: Session,
        playlist_id: UUID,
        title: str,
        artist: str,
        reason: [str | None] = None,
        url: [str | None] = None,
        position: int = 0,
    ) -> PlaylistSong:

        song = PlaylistSong(
            playlist_id=playlist_id,
            title=title,
            artist=artist,
            reason=reason,
            url=url,
            position=position,
        )

        return self.create(db, song)
