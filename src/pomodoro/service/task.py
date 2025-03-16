from dataclasses import dataclass

from src.pomodoro.repositories.redis_ import AbstractRedisClient
from src.pomodoro.repositories.task import AbstractTaskRepository
from src.pomodoro.schema.task import TaskSchema, TaskShemaCreate
from src.pomodoro.schema.base import ListModel


@dataclass
class TaskService:
    task_repository: AbstractTaskRepository
    redis_client: AbstractRedisClient

    async def fetch_tasks(self) -> ListModel[TaskSchema]:
        tasks = await self.task_repository.fetch_all_tasks()
        
        return ListModel(
            data=tasks
        )
        
    async def create_task(self, task: TaskShemaCreate) -> int:
        return await self.task_repository.create_task(task=task)
        
    async def fetch_task(self, task_id: int) -> TaskSchema:
        task_from_cache = await self.redis_client.fetch_key(str(task_id))
        
        if not task_from_cache:
            task = await self.task_repository.fetch_task(task_id=task_id)
            result = TaskSchema(
                id=task.id, 
                name=task.name,
                pomodoro_count=task.pomodoro_count,
                category_id=task.category_id,
            )
            data_stored = result.model_dump()
            
            await self.redis_client.set_key(str(task_id), data_stored)
            print("Value from DB")
            return result
        print("Value from cache")
        
        return TaskSchema(**task_from_cache)
    
