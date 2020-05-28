from words_count.tasks_handlers.base_handler import BaseHandler
from words_count.report_task import TaskMessage


class StringHandler(BaseHandler):

    def __init__(self, word_breaking_handler):
        super().__init__(word_breaking_handler)

    def handle(self, task: TaskMessage):
        for line in task.content.split('\n'):
            self.submit_to_word_break(line)
