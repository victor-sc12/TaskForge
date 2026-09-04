from abc import ABC, abstractmethod
from datetime import datetime
import itertools

class Task:
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.created_at = datetime.now()
        self.completed = False

    def __str__(self):
        return f"{self.id}, {self.title}, {self.completed}, {self.created_at}"

    def complete(self):
        self.completed = True

    def rename(self, new_title):
        self.title = new_title

class TaskRepository(ABC):
    @abstractmethod
    def add(self, task):
        pass

    @abstractmethod
    def get_by_id(self, task_id):
        pass

    @abstractmethod
    def list_all(self):
        pass

    @abstractmethod
    def update(self, task):
        pass

class InMemoryTaskRepository(TaskRepository):
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def get_by_id(self, task_id):
        task = next((t for t in self.tasks if t.id == task_id), None)
        return task
    
    def list_all(self):
        return self.tasks

    def update(self, updated_task):
        task = next((t for t in self.tasks if t.id == updated_task.id), None)
        task = updated_task

if __name__ == '__main__':
    pass