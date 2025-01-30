from dataclasses import dataclass

from repository import TaskRepository
from schema.task import TaskSchema


@dataclass
class TaskService:
    task_repository: TaskRepository

    def get_tasks(self):

        tasks = self.task_repository.get_tasks()
        tasks_schema = [TaskSchema.model_validate(task) for task in tasks]
        return tasks_schema
