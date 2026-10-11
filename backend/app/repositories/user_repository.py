from app.model.user import User
from sqlalchemy import select
from sqlalchemy.orm import Session

class UserRepository:
    
    def get_by_id(self,db : Session,user_id):
        return db.get(User,user_id)
    
    def get_by_email(self,db : Session,user_email : str):
        statement = select(User).where(User.email == user_email)
        return db.scalar(statement)
    
    def create(self,db: Session,user : User) -> User:
        try:
            db.add(user)
            db.commit()
            db.refresh(user)
            return user
        except Exception:
            db.rollback()
            raise