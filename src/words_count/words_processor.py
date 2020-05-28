import logging

from concurrent.futures import ThreadPoolExecutor
from words_count.report_task import TaskMessage, TaskType
from words_count.tasks_handlers.base_handler import BaseHandler
from words_count.tasks_handlers.file_handler import FileHandler


class WordsProcessor:

    def __init__(self, max_num_of_workers, word_stats_store, words_breaker):
        self.threads_pool = ThreadPoolExecutor(max_workers=max_num_of_workers)
        self.word_stats_store = word_stats_store
        self.word_breaking_handler = words_breaker
        self.handlers_by_type = {
            TaskType.FILE: FileHandler(self.word_breaking_handler)
        }

    def submit_task(self, task: TaskMessage):
        self.threads_pool.submit(self.__handle_task, task)

    def __handle_task(self, task: TaskMessage):
        try:
            handler = self.__get_handler_by_type(task.task_type)
            if not handler:
                raise Exception(f'Handler not found: {task.task_type}')

            handler.handle(task)
        except Exception:
            logging.getLogger().exception(f'exception occurred while handling task {task.task_type}:{task.content}')

    def __get_handler_by_type(self, type: TaskType) -> BaseHandler:
        return self.handlers_by_type.get(type)



