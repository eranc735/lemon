from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from words_count.words_stats import WordsStatsStore


class WordBreaker:

    def __init__(self, max_num_of_workers, words_stats: WordsStatsStore):
        self.workers_pool = ThreadPoolExecutor(max_workers=max_num_of_workers)
        self.words_stats = words_stats

    def submit_breaking_task(self, text):
        self.workers_pool.submit(self.__count_words, text)

    def __count_words(self, text):
        words = text.split()
        words_count = defaultdict(lambda: 0)
        for word in words:
            words_count[word] += 1

        self.words_stats.update_counts(words_count)

