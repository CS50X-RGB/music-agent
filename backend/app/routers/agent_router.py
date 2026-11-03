from fastapi import APIRouter,Depends
from backend.app.core.dependencies import get_current_user
from backend.app.model.user import User
from backend.app.schemas.agent import AgentRequest,AgentResponse
from backend.app.services.agent_service import AgentService


router = APIRouter(prefix="/agent",tags=['Music Agent'])
agent_service = AgentService()

@router.post("/generate",response_class=AgentResponse)
def generate_playlist(data : AgentRequest):
    status,msg = agent_service.generate_playlist(data.prompt)
    return AgentResponse(status=status,response=msg)