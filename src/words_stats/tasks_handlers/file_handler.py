import logging
from collections import defaultdict

from words_stats.tasks_handlers.base_handler import BaseHandler
from words_stats.report_task import Task
from words_stats.words_stats_store import WordsStatsStore


class FileHandler(BaseHandler):

    def __init__(self, words_stats_store: WordsStatsStore):
        super().__init__(words_stats_store=words_stats_store)

    def handle(self, task: Task):
        words_count = defaultdict(lambda: 0)

        try:
            with open(task.content, 'r') as f:
                for line in f:
                    words = line.split()
                    for word in words:
                        word = self.word_normalization(word)
                        words_count[word] += 1

        except FileNotFoundError:
            logging.getLogger().exception(f'Could not find file {task.content}')

        return words_count
