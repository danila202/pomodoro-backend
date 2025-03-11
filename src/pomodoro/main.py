from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.pomodoro.settings import settings
from src.pomodoro.database.db import create_tables, engine
from .api.tasks import TASK_ROUTER


@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa: ARG001
    await create_tables(engine)
    yield
    
    
def make_app() -> FastAPI:
    app = FastAPI(
        title= settings.app_name,
        docs_url=settings.docs_url,
        lifespan=lifespan,
    )
    app.include_router(TASK_ROUTER)
    return app
