from fastapi import Depends

from src.pomodoro.database.db import create_session

from src.pomodoro.repositories.task import SQLTaskRepository
from src.pomodoro.service import TaskService
from sqlalchemy.ext.asyncio import AsyncSession

def create_tasks_repository(
    session: AsyncSession = Depends(create_session)
    ) -> SQLTaskRepository:
    
        return SQLTaskRepository(session)


def create_task_service(
    task_repository: SQLTaskRepository = Depends(create_tasks_repository),
) -> TaskService:
    return TaskService(
        task_repository=task_repository,
    )
