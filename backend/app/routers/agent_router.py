from fastapi import APIRouter

from backend.app.schemas.agent import AgentRequest, AgentResponse
from backend.app.services.agent_service import AgentService

router = APIRouter(prefix="/agent", tags=["Music Agent"])
agent_service = AgentService()


@router.post("/generate", response_model=AgentResponse)
def generate_playlist(data: AgentRequest):
    status, msg = agent_service.generate_playlist(data.prompt)
    return AgentResponse(status=status, reponse=msg)
