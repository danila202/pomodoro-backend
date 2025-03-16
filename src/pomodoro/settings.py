from loguru import logger
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "pomodoro"
    docs_url: str | None = "/docs/"
    host: str = "0.0.0.0"
    port: int = 8000

    db_uri: str = "postgresql+asyncpg://user:password@db:5432/pomodoro"
    redis_uri: str = "redis://redis_container:6379/0"


settings = Settings()

logger.add(sink="logs", enqueue=True)
