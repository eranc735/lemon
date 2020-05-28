from words_count.tasks_handlers.base_handler import BaseHandler
from words_count.report_task import TaskMessage


class FileHandler(BaseHandler):

    def __init__(self, word_breaking_handler):
        super().__init__(word_breaking_handler)

    def handle(self, task: TaskMessage):
        with open(task.content, 'r') as f:
            for line in f:
                self.submit_to_word_break(line)
