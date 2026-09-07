from abc import ABC, abstractmethod
from datetime import datetime
import itertools

class Task:
    def __init__(self, id, title):
        self._id = id
        self._title = title
        self._created_at = datetime.now()
        self._completed = False

    def __str__(self):
        return f"{self._id}, {self._title}, {self._completed}, {self._created_at}"

    def get_id(self):
        return self._id

    def complete(self):
        self._completed = True

    def rename(self, new_title):
        if not new_title:
            raise ValueError("Invalid title")
        self._title = new_title

class TaskManager:
    # Initialize a counter starting at 1
    _id_iter = itertools.count(1)

    def __init__(self):
        self._tasks = []
        # self._task_id = next(self._id_iter)

    def _add_task(self, task):
        self._tasks.append(task)

    def create_task(self, title):
        task = Task(next(TaskManager._id_iter), title)
        self._add_task(task)

    def list_tasks(self):
        return self._tasks

    def get_task_by_id(self, task_id):
        task = next((t for t in self._tasks if t.get_id() == task_id), None)
        if not Task:
            raise ValueError("Obj not found")
        return task

    def complete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        task.complete()
        
    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        del task

if __name__ == '__main__':
    pass