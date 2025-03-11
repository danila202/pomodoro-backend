from pydantic_settings import BaseSettings
from loguru import logger

class Settings(BaseSettings):
    app_name: str = "pomodoro"
    docs_url: str | None = "/docs/"
    host: str = "0.0.0.0"
    port: int = 8000
    
    db_uri: str = "postgresql+asyncpg://user:password@db:5432/pomodoro"



settings = Settings()

logger.add(sink="logs", enqueue=True)
