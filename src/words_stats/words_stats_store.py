from collections import defaultdict
from threading import Thread
from queue import Queue
import time


class WordsStatsStore:

    def __init__(self):
        self.words_stats = defaultdict(lambda: 0)
        self.stats_report_queue = Queue()
        self.running = False

    def update_counts(self, counts: dict):
        self.stats_report_queue.put(counts)

    def get_count(self, word: str) -> int:
        return self.words_stats[word]

    def start(self):
        self.running = True
        worker = Thread(target=self.__counts_updating_handler)
        worker.start()

    def stop(self):
        self.running = False

    def __counts_updating_handler(self):
        while self.running:
            if not self.stats_report_queue.empty():
                counts = self.stats_report_queue.get()

                for word, count in counts.items():
                    self.words_stats[word] += count
            else:
                time.sleep(0.5)
