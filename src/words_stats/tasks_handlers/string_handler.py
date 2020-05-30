from collections import defaultdict

from words_stats.tasks_handlers.base_handler import BaseHandler
from words_stats.report_task import Task


class StringHandler(BaseHandler):

    def __init__(self, words_stats_store):
        super().__init__(words_stats_store=words_stats_store)

    def handle(self, task: Task):
        words_count = defaultdict(lambda: 0)

        for line in task.content.split('\n'):
            words = line.split()
            for word in words:
                word = self.word_normalization(word)
                words_count[word] += 1

        return words_count
