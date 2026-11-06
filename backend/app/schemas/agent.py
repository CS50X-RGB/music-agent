from pydantic import BaseModel,Field
from typing import Any

class AgentRequest(BaseModel):
    prompt : str = Field(min_length=1,max_length=10000)


class AgentResponse(BaseModel):
    status : str
    reponse : dict[str,Any]