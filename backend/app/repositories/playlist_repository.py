from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.model.playlist import Playlist,PlaylistSong


class PlaylistRepo:
    def create(self,db: Session,playlist: Playlist) -> Playlist:
        try:
            db.add(playlist)
            db.commit()
            db.refresh(playlist)
            return playlist
        except Exception:
            db.rollback()
            raise
        
    def get_by_id(self,db : Session,playlist_id : UUID) -> Playlist | None:
        return db.get(Playlist,playlist_id)
    
    def get_all(self,db : Session,user_id : UUID) -> list[Playlist]:
        statement = (
            select(Playlist).where(Playlist.user == user_id).order_by(Playlist.created_at.desc())
        )
        return list(db.scalar(statement=statement).all())
    
    
    def update(self,db : Session,playlist_id : UUID,updates : dict) -> Playlist | None:
        playlist = db.get(Playlist,playlist_id)
        
        if playlist is None:
            return None

        for field,value in updates.items():
            if field in {"name","original_prompt","status"}:
                setattr(playlist,field,value)
    
    def delete(self,db : Session,playlist_id : UUID) -> bool:
        playlist = db.get(Playlist,playlist_id)
        
        if playlist is None:
            return False

        try:
            db.delete(playlist)
            db.commit()
            return True
        except Exception:
            db.rollback()
            raise