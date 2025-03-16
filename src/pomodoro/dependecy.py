from fastapi import Depends

from src.pomodoro.database.db import create_session

from src.pomodoro.repositories.redis_ import AbstractRedisClient
from src.pomodoro.database.redis_connection import make_redis_client
from src.pomodoro.repositories.task import AbstractTaskRepository, SQLTaskRepository
from src.pomodoro.service import TaskService
from sqlalchemy.ext.asyncio import AsyncSession

def create_task_repository(
    session: AsyncSession = Depends(create_session)
    ) -> SQLTaskRepository:
    
        return SQLTaskRepository(session)


def create_task_service(
    task_repository: AbstractTaskRepository = Depends(create_task_repository),
    redis_client: AbstractRedisClient = Depends(make_redis_client),
) -> TaskService:
    return TaskService(task_repository=task_repository, redis_client=redis_client)
    
    