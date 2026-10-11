from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from app.model.user import User
from app.repositories.user_repository import UserRepository
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()
        
    def register(self,db : Session,email : str,password : str):
        existing_user = self.user_repo.get_by_email(email)
        
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already exists"
            )
        
        user = User(email=email,password=hash_password(password))
        
        user = self.user_repo.create(db,user)
        
        token = create_access_token(str(user.id),user.email)
        
        return {
            "access_token" : token,
            "token_type" : "Bearer"
        }
    
    def login(self,db: Session,email : str,password : str) -> dict:
        user = self.user_repo.get_by_email(db,email)
        
        if user is None or not verify_password(password,user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
                headers={"WWW-Authenticate" : "Bearer"}
            )
        
        token = create_access_token(str(user.id),user.email)
        
        return {
            "access_token" : token,
            "token_type" : "Bearer"
        }