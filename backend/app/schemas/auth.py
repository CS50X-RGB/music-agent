from pydantic import BaseModel,EmailStr,Field,ConfigDict
from uuid import UUID

class RegisterReq(BaseModel):
    email : EmailStr
    password : str = Field(min_length=8,max_length=128)
    name : str

class LoginRequest(BaseModel):
    email : EmailStr
    password : str

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    email: str
    name: str

class TokenReponse(BaseModel):
    access_token : str
    token_type : str = "bearer"
    user : UserResponse