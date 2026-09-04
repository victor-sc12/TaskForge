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

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, *args):
        self.tasks.extend(args)

    def list_tasks(self):
        return self.tasks

    def get_task_by_id(self, task_id):
        task = next((t for t in self.tasks if t.id == task_id), None)
        return task

    def complete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        task.complete()
        
    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        del task

if __name__ == '__main__':
    pass