from fastapi import Depends

from database import get_db_session

from repository import TaskRepository
from service import TaskService


def get_tasks_repository() -> TaskRepository:
    db_session = get_db_session()
    return TaskRepository(db_session)


def get_task_service(
    task_repository: TaskRepository = Depends(get_tasks_repository),
) -> TaskService:
    return TaskService(
        task_repository=task_repository,

    )
