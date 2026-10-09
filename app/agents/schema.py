from pydantic import BaseModel
from typing import Literal

class MusicTask(BaseModel):
    agent : str
    operation : str
    query : str
    search_type: Literal["artist", "song"] | None = None
    depends_on : int | None = None
    

class MusicPlan(BaseModel):
    tasks : list[MusicTask]


class PlaylistSong(BaseModel):
    title : str
    artist : str
    reason : str
    video_id : str | None = None
    url : str | None = None
    embed_url : str | None = None
    
class Playlist(BaseModel):
    name: str
    songs : list[PlaylistSong]