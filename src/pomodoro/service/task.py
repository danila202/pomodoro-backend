from dataclasses import dataclass

from src.pomodoro.repositories.task import AbstractTaskRepository
from src.pomodoro.schema.task import TaskSchema, TaskShemaCreate
from src.pomodoro.schema.base import ListModel


@dataclass
class TaskService:
    task_repository: AbstractTaskRepository

    async def fetch_tasks(self) -> ListModel[TaskSchema]:
        tasks = await self.task_repository.fetch_all_tasks()
        
        return ListModel(
            data=tasks
        )
        
    async def create_task(self, task: TaskShemaCreate) -> int:
        return await self.task_repository.create_task(task=task)
        
    async def fetch_task(self, task_id: int) -> TaskSchema:
        task = await self.task_repository.fetch_task(task_id=task_id)
        return TaskSchema(
            id=task.id,
            name=task.name,
            pomodoro_count=task.pomodoro_count,
            category_id=task.category_id,
        )
