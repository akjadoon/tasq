from enum import Enum
from typing import List


class Priority(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5


class Task:
    next_id = 1
    def __init__(self, title: str, description: str = "", priority: Priority = None, dependencies: List[Task] = []):
        self.id = Task.next_id
        Task.next_id += 1 
        
        self.title = title
        self.description = description
        self.priority = priority
        self.dependencies = dependencies

