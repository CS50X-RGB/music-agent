from uuid import UUID
from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session

from app.core.dependencies import get_db,get_current_user
from app.schemas.playlist import PlaylistCreate
from app.services.playlist_service import PlaylistService
from app.model.user import User

router = APIRouter(prefix='/playlist',tags=['Playlists'])
service = PlaylistService()

@router.post("/",status_code=status.HTTP_201_CREATED)
def create_playlist(
    data : PlaylistCreate,
    db : Session = Depends(get_db),
    user : User = Depends(get_current_user)
):
    return service.create_playlist(db,user.id,data)

@router.get("/my")
def get_my_playlists(db:Session = Depends(get_db),user : User = Depends(get_current_user)):
    playlists = service.get_playlists_by_user_id(db,user.id)
    if len(playlists) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No Playlists found"
        )
    return playlists

@router.get("/{playlist_id}")
def get_playlist(
    playlist_id : UUID,
    db : Session = Depends(get_db)
):
    playlist = service.get_playlist(db,playlist_id)
    if playlist is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Playlist not found"
        )
    return playlist