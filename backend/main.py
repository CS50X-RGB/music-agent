from fastapi import FastAPI
from app.routers.playlist_router import router as playlist_router
from app.routers.auth_router import router as user_router
from app.routers.feedback_router import router as feedback_router
app = FastAPI(title="Music Feedback API")

app.include_router(playlist_router)
app.include_router(user_router)
app.include_router(feedback_router)