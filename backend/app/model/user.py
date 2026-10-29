import uuid
from datetime import datetime,timezone

from sqlalchemy import DateTime,String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped,mapped_column,relationship
from app.model.playlist import Playlist

from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    
    id : Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    name : Mapped[str] = mapped_column(
        String(40),
        unique=False,
        nullable=False
    ) 
    email : Mapped[str] = mapped_column(
        String(320),
        unique=True,
        index=True,
        nullable=False
    )
    password : Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )
    created_at : Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda : datetime.now(timezone.utc),
        nullable=False
    )
    
    playlists : Mapped[list["Playlist"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )