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