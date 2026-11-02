from fastapi import APIRouter,Depends
from backend.app.core.dependencies import get_current_user
from backend.app.model.user import User
from backend.app.schemas.agent import AgentRequest,AgentResponse
from backend.app.services.agent_service import AgentService
from agent.backend.app.graph.workflow import app as graph

router = APIRouter(prefix="/agent",tags=['Music Agent'])
agent_service = AgentService(graph=graph)

@router.post("/generate",response_class=AgentResponse)
def generate_playlist(data : AgentRequest,current_user : User = Depends(get_current_user)):
    response = agent_service.generate_playlist(data.prompt)
    return AgentResponse(response)