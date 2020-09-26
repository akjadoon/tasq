from typing import List, Callable

from .task import Task


class TaskForest:
    def __init__(self):
        self.tasks = []

    def add(self, t: Task):
        self.tasks.append(t)





