import uuid
from datetime import datetime,timezone


from sqlalchemy import (
    DateTime,
    ForeignKey,
    String,
    Text
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped,mapped_column,relationship
from app.core.database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.model.user import User
    from app.model.feedback import SongFeedback

class Playlist(Base):
    __tablename__ = "playlists"
    
    id : Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    name : Mapped[str] = mapped_column(String(200),nullable=False)
    original_prompt : Mapped[str] = mapped_column(String(200),nullable=False)
    status : Mapped[str] = mapped_column(String(20),default='pending',nullable=False)
    created_at : Mapped[datetime] = mapped_column(DateTime(timezone=True),default=lambda : datetime.now(timezone.utc),nullable=False)
    user : Mapped["User"] = relationship(
        back_populates='playlists'
    )
    songs : Mapped[list["PlaylistSong"]] = relationship(
        back_populates='playlist',
        cascade="all, delete-orphan",
        order_by="PlaylistSong.position"
    )
    user_id : Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id",ondelete="CASCADE"),
        nullable=False,
        index=True
    )

class PlaylistSong(Base):
    __tablename__= "playlist_songs"
    
    id : Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    playlist_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("playlists.id",ondelete="CASCADE"),
        nullable=False,
        index=True
    )
    title : Mapped[str] = mapped_column(
        String(300),
        nullable=False,
    )
    artist : Mapped[str] = mapped_column(
        String(300),
        nullable=False
    )
    reason : Mapped[str] = mapped_column(
        Text,
        nullable=True,
    )
    url : Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )
    embed_url : Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )
    position : Mapped[int] = mapped_column(
        nullable=False,
    )
    playlist : Mapped['Playlist'] = relationship(
        back_populates="songs"
    )
    feedback : Mapped[list["SongFeedback"]] = relationship(
        back_populates="song",
        cascade="all, delete-orphan"
    )