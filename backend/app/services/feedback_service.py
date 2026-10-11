from uuid import UUID
from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from app.model.feedback import SongFeedback
from app.repositories.feedback_repository import FeedbackRepository

class FeedbackService:
    
    def __init__(self):
        self.repo = FeedbackRepository()
        
    def submit_feedback(self,db: Session,user_id: UUID,song_id : UUID,feedback_type : str) -> SongFeedback:
        song = self.repo.get_song(db,song_id)
        
        if song is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Song not found"
            )
        
        feedback = self.repo.get_by_user_and_song(db,user_id,song_id)
        
        if feedback:
            feedback.feedback_type = feedback_type
        else:
            feedback = SongFeedback(
                user_id,
                song_id,
                feedback_type
            )
        return self.repo.save(db,feedback)