from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.schemas.auth import RegisterReq,LoginRequest,TokenReponse
from app.services.auth_service import AuthService


router = APIRouter(prefix='/auth',tags=['Authentication'])
auth_service = AuthService()

@router.post(
    "/register",
    response_model=TokenReponse,
    status_code=status.HTTP_201_CREATED
)
def register(
    data : RegisterReq,
    db : Session = Depends(get_db),
):
    return auth_service.register(db,data.email,data.password)

@router.post('/login',response_model=TokenReponse)
def login(
    data : LoginRequest,
    db : Session = Depends(get_db)
):
    return auth_service.login(db,data.email,data.password)