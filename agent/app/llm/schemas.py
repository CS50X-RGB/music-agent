from pydantic import BaseModel


class MusicRequest(BaseModel):
    intent: str
    query : str
    search_type : str