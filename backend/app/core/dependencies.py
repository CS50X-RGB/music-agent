from collections.abc import Generator
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from uuid import UUID
import jwt
from fastapi import Depends,HTTPException,status
from fastapi.security import HTTPAuthorizationCredentials,HTTPBearer
from sqlalchemy.orm import Session
from app.core.config import settings
from app.model.user import User
from app.repositories.user_repository import UserRepository

bearer_scheme = HTTPBearer(auto_error=False)
user_repo = UserRepository()


def get_db() -> Generator[Session,None,None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
def get_current_user(creds : HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
                     db : Session = Depends(get_db)) -> User:
    unauth = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing auth token",
        headers={"WWW-Authenticate": "Bearer"}
    )
    if creds in None:
        raise unauth
    
    try:
        payload = jwt.decode(creds.credentials,settings.secret_key,algorithms=[settings.algorithm])
        user_id = UUID(payload['sub'])
    except (jwt.InvalidTokenError,KeyError,ValueError):
        raise unauth
    
    user = user_repo.get_by_id(db,user_id)
    
    if user is None:
        raise unauth
    
    return user