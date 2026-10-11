from pydantic import BaseModel,EmailStr,Field

class RegisterReq(BaseModel):
    email : EmailStr
    password : str = Field(min_length=8,max_length=128)
    

class LoginRequest(BaseModel):
    email : EmailStr
    password : str

class TokenReponse(BaseModel):
    access_token : str
    token_type : str = "bearer"