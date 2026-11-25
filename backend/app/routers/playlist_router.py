from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session

from backend.app.core.dependencies import get_db
from backend.app.schemas.playlist import PlaylistCreate
from backend.app.services.playlist_service import PlaylistService

router = APIRouter(prefix="/playlist", tags=["Playlists"])
service = PlaylistService()


@router.post("/like", status_code=status.HTTP_201_CREATED)
def create_playlist(
    request: Request,
    data: PlaylistCreate,
    db: Session = Depends(get_db),
):
    user = request.state.user

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
        )
    user_id = UUID(user["id"])
    return service.create_playlist(db, user_id, data)


@router.get("/my")
def get_my_playlists(request: Request, db: Session = Depends(get_db)):
    user = request.state.user
    user_id = UUID(user["id"])
    playlists = service.get_playlists_by_user_id(db, user_id)
    if playlists and len(playlists) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No Playlists found"
        )
    return playlists


"""
@router.get("/{playlist_id}")
def get_playlist(playlist_id: UUID, db: Session = Depends(get_db)):
    playlist = service.get_playlist(db, playlist_id)
    if playlist is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Playlist not found"
        )
    return playlist
"""
