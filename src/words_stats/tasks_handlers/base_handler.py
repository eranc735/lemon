import abc
import re

from words_stats.words_stats_store import WordsStatsStore
from ..report_task import Task

alphabet_only_pattern = re.compile('[^a-zA-Z]')


class BaseHandler:

    def __init__(self, words_stats_store: WordsStatsStore):
        self.words_stats_store = words_stats_store

    @abc.abstractmethod
    def handle(self, task: Task):
        pass

    def handle_task(self, task: Task):
        counts = self.handle(task)
        self.words_stats_store.update_counts(counts)

    def word_normalization(self, word):
        return alphabet_only_pattern.sub('', word).lower()
