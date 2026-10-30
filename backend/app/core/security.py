from pwdlib import PasswordHash
from datetime import datetime,timedelta,timezone
import jwt
from app.core.config import settings
import traceback

def create_access_token(user_id : str,user_email : str,name : str) -> str:
    payload = {
        "sub" : user_id ,
        "email" : user_email,
        "name" : name,
        "exp" : datetime.now(timezone.utc) + timedelta(hours=settings.expire_time_hrs),
    }
    
    return jwt.encode(
        payload=payload,
        key=settings.secret_key,
        algorithm=settings.algorithm
    )


def decode_access_token(token: str):
    payload = jwt.decode(
        jwt=token,
        key=settings.secret_key,
        algorithms=[settings.algorithm]
    )

    return payload



password_hash = PasswordHash.recommended()

def hash_password(password : str) -> str:
    return password_hash.hash(password)

def verify_password(plain_pass: str,hashed_pass : str) -> bool:
    return password_hash.verify(plain_pass,hashed_pass)