import os

from pydantic_settings import BaseSettings,SettingsConfigDict
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,sessionmaker

class Settings(BaseSettings):
    database_url : str
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

settings = Settings()

engine = create_engine(settings.database_url,pool_pre_ping=True)

SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)

class Base(DeclarativeBase):
    pass

# - Settings loads configuration from environment variables.
# - engine manages connections to PostgreSQL.
# - Base will be the parent class for your SQLAlchemy database models.
# We'll use SessionLocal through FastAPI dependency injection when building endpoints.