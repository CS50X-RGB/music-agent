from pydantic_settings import BaseSettings,SettingsConfigDict


class Settings(BaseSettings):
    secret_key : str
    algorithm: str = "HS256"
    expire_time_hrs : int = 24
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
    
settings = Settings()