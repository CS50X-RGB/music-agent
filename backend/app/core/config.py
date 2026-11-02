from pydantic_settings import BaseSettings,SettingsConfigDict
from pathlib import Path


BACKEND_DIR = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    secret_key : str
    algorithm: str = "HS256"
    expire_time_hrs : int = 24
    model_config = SettingsConfigDict(
        env_file=BACKEND_DIR / ".env",
        extra="ignore"
    )
    
settings = Settings()