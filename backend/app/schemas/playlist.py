from pydantic import BaseModel, Field


class PlaylistSongCreate(BaseModel):
    ID: str
    Title: str = Field(min_length=1, max_length=300)
    Artist: str = Field(min_length=1, max_length=300)
    Reason: str
    Duration: str
    AudioUrl: str | None = None


class PlaylistCreate(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    session_id: str
    songs: list[PlaylistSongCreate]
