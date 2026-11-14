from datetime import datetime
from typing import Literal
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class FeedbackCreate(BaseModel):
    feedback_type : Literal["like","dislike"]
    
class FeedbackResponse(BaseModel):
    id : UUID
    song_id : UUID
    feedback_type : Literal["like","dislike"]
    created_at : datetime
    model_config = ConfigDict(from_attributes=True)