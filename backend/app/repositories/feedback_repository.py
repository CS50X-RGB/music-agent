from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session
from app.model.playlist import PlaylistSong
from app.model.feedback import SongFeedback

class FeedbackRepository:
    
    def get_song(self,db : Session,song_id : UUID) -> PlaylistSong | None:
        return db.get(PlaylistSong,song_id)
    
    def get_by_user_and_song(self,db: Session,user_id : UUID,song_id : UUID) -> SongFeedback | None:
        statement = select(SongFeedback).where(
            SongFeedback.user_id == user_id,
            SongFeedback.song_id == song_id
        )
        return db.scalar(statement)
    
    def save(self,db : Session,feedback : SongFeedback) -> SongFeedback:
        try:
            db.add(feedback)
            db.commit()
            db.refresh(feedback)
            return feedback
        except Exception:
            db.rollback()
            raise