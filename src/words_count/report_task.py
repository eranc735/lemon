from enum import Enum


class TaskType(Enum):
    URL = 1
    FILE = 2
    TEXT = 3


class TaskMessage:

    def __init__(self, task_type: TaskType, content: str):
        self.task_type = task_type
        self.content = content
