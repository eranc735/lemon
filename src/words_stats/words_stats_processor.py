import logging

from concurrent.futures import ThreadPoolExecutor
from words_stats.report_task import Task, TaskType
from words_stats.tasks_handlers.base_handler import BaseHandler
from words_stats.tasks_handlers.file_handler import FileHandler
from words_stats.tasks_handlers.string_handler import StringHandler
from words_stats.tasks_handlers.url_handler import URLHandler


class WordsStatsProcessor:

    def __init__(self, max_num_of_workers, word_stats_store):
        self.threads_pool = ThreadPoolExecutor(max_workers=max_num_of_workers)
        self.word_stats_store = word_stats_store
        self.handlers_by_type = {
            TaskType.FILE: FileHandler(self.word_stats_store),
            TaskType.TEXT: StringHandler(self.word_stats_store),
            TaskType.URL: URLHandler(self.word_stats_store)
        }

    def submit_task(self, task: Task):
        self.threads_pool.submit(self.__handle_task, task)

    def __handle_task(self, task: Task):
        try:
            handler = self.__get_handler_by_type(task.task_type)
            if not handler:
                raise Exception(f'Handler not found: {task.task_type}')

            handler.handle_task(task)
        except Exception:
            logging.getLogger().exception(f'exception occurred while handling task {task.task_type}:{task.content}')

    def __get_handler_by_type(self, type: TaskType) -> BaseHandler:
        return self.handlers_by_type.get(type)



