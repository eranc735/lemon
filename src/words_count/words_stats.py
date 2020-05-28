from collections import defaultdict
from threading import Thread
from queue import Queue
import time


class WordsStatsStore:

    def __init__(self):
        self.words_count = defaultdict(lambda: 0)
        self.counts_queue = Queue()
        self.running = False

    def update_counts(self, counts: dict):
        self.counts_queue.put(counts)

    def get_count(self, word: str) -> int:
        x = self.words_count[word]
        return x

    def start(self):
        self.running = True
        worker = Thread(target=self.__counts_updating_handler)
        worker.start()

    def stop(self):
        self.running = False

    def __counts_updating_handler(self):
        while self.running:
            if not self.counts_queue.empty():
                counts = self.counts_queue.get()
                for word, count in counts.items():
                    self.words_count[word] += count
            else:
                time.sleep(0.5)
