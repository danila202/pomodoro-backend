import abc

from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from src.pomodoro.settings import logger
from src.pomodoro.database.models import Tasks
from src.pomodoro.schema.task import  TaskShemaCreate, TaskSchema
from src.pomodoro.repositories.base import AbstractSQLRepository


class AbstractTaskRepository(abc.ABC):
    
    @abc.abstractmethod
    async def fetch_all_tasks(self) -> list[TaskSchema]:
        raise NotImplementedError
    
    @abc.abstractmethod
    async def fetch_task(self, task_id: int) -> TaskSchema:
        raise NotImplementedError
    
    @abc.abstractmethod
    async def create_task(self, task: TaskShemaCreate) -> int:
        raise NotImplementedError


class SQLTaskRepository(AbstractSQLRepository, AbstractTaskRepository):

    def __init__(self, session: AsyncSession):
        super().__init__(session=session)


    async def create_task(self, task: TaskShemaCreate) -> int:
        new_task: Tasks = Tasks(
            name=task.name,
            pomodoro_count=task.pomodoro_count,
            category_id=task.category_id,
        )
        self.session.add(new_task)
        await self.session.flush()
        
        await self.session.commit()
        
        logger.info(f"create new task with id {new_task.id}")
        
        return new_task.id
        
    async def fetch_all_tasks(self, task_id: int | None = None) -> list[TaskSchema]:
        filters = []
        
        if task_id is not None:
            filters.append(Tasks.id==task_id)
        
        query = select(Tasks).where(and_(*filters))
        
        tasks = await self.session.execute(query)
        
        return [
            TaskSchema(
                id=task.id,
                name=task.name,
                pomodoro_count=task.pomodoro_count,
                category_id=task.category_id,
            )
            for task in tasks.scalars().all()
        ]
        
    async def fetch_task(self, task_id: int) -> TaskSchema:
        tasks: list[TaskSchema] = await self.fetch_all_tasks(task_id=task_id)

        if tasks:
            return tasks[0]
        
        raise IndexError


