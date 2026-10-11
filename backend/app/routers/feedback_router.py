from uuid import UUID
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user,get_db
from app.model.user import User
from app.schemas.feedback import FeedbackCreate,FeedbackResponse
from app.services.feedback_service import FeedbackService

router = APIRouter(tags=["Song Feedback"])
feedback_service = FeedbackService()

@router.put("/songs/{song_id}/feedback",response_class=FeedbackResponse)
def submit_feedback(song_id : UUID,data: FeedbackCreate,
                    db : Session = Depends(get_db),
                    current_user : User = Depends(get_current_user)):
    return feedback_service.submit_feedback(db,current_user.id,song_id,data.feedback_type)
