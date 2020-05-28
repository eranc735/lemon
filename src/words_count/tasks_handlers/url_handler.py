import requests

from words_count.tasks_handlers.base_handler import BaseHandler
from words_count.report_task import TaskMessage


class FileHandler(BaseHandler):

    def __init__(self, word_breakinh_handler):
        super().__init__(word_breakinh_handler)

    def handle(self, task: TaskMessage):
        resp = requests.get(url=task.content, stream=True)
        for line in resp.iter_lines():
            self.submit_to_word_break(line)