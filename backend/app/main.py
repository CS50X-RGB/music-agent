from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.playlist_router import router as playlist_router
from app.routers.auth_router import router as user_router
from app.routers.feedback_router import router as feedback_router
from app.middleware.userMiddleware import UserMiddleware


app = FastAPI(title="Music Feedback API")

API_PREFIX = "/api/web/v1"
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*']
)
app.add_middleware(UserMiddleware)
app.include_router(playlist_router, prefix=API_PREFIX)
app.include_router(user_router, prefix=API_PREFIX)
app.include_router(feedback_router, prefix=API_PREFIX)