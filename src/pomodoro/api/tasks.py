from typing import Annotated, Final

from fastapi import APIRouter, status, Depends

from src.pomodoro.dependecy import create_task_service
from src.pomodoro.schema.task import TaskShemaCreate, TaskSchema
from src.pomodoro.schema.base import ListModel
from src.pomodoro.service import TaskService

TASK_ROUTER: Final = APIRouter(prefix="/task", tags=["task"])


@TASK_ROUTER.get("/")
async def fetch_tasks(
    task_service: Annotated[TaskService, Depends(create_task_service)]
) -> ListModel[TaskSchema]:
    return await task_service.fetch_tasks()


@TASK_ROUTER.get("/{task_id}")
async def fetch_task(
    task_service: Annotated[TaskService, Depends(create_task_service)],
    task_id: int
) -> TaskSchema:
    return await task_service.fetch_task(task_id=task_id)


@TASK_ROUTER.post("/")
async def create_task(
    data: TaskShemaCreate,
    task_service: Annotated[TaskService, Depends(create_task_service)],
) -> int:
    return await task_service.create_task(task=data)