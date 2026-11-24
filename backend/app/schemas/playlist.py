from pydantic import BaseModel, Field


class PlaylistSongCreate(BaseModel):
    id: str
    title: str = Field(min_length=1, max_length=300)
    artist: str = Field(min_length=1, max_length=300)
    reason: str
    duration: str
    url: str | None = None


class PlaylistCreate(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    songs: list[PlaylistSongCreate]
