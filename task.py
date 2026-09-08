from datetime import datetime
import itertools

class Task:
    def __init__(self, id, title):
        self.__id = id
        self.__title = title
        self.__created_at = datetime.now()
        self.__completed = False

    def __str__(self):
        return f"{self.__id}, {self.__title}, {self.__completed}, {self.__created_at}"

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if not title:
            raise ValueError("Invalid title")

        self.__title = title

    def complete(self):
        if self.__completed:
            raise ValueError("Task already completed")
        
        self.__completed = True

class TaskManager:
    # Initialize a counter starting at 1
    _id_iter = itertools.count(1)

    def __init__(self):
        self.__tasks = []

    def create_task(self, title):
        task = Task(next(TaskManager._id_iter), title)
        self.__tasks.append(task)
        return task

    def get_task_by_id(self, task_id):
        task = next((t for t in self.__tasks if t.id == task_id), None)
        if not task:
            raise ValueError("Obj not found")
        return task

    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        self.__tasks.remove(task)

if __name__ == '__main__':
    pass