from pydantic import BaseModel, Field

class PlaylistSongCreate(BaseModel):
    title: str = Field(min_length=1, max_length=300)
    artist: str = Field(min_length=1, max_length=300)
    reason: str
    video_id: str | None = None
    url: str | None = None
    embed_url: str | None = None


class PlaylistCreate(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    user_id : str
    original_prompt: str
    songs: list[PlaylistSongCreate]