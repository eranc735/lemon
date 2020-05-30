from .report_task import TaskType, Task
from .words_stats_processor import WordsStatsProcessor
from .words_stats_store import WordsStatsStore


class WordsStatsService:

    def __init__(self, word_processor: WordsStatsProcessor, word_stats_store: WordsStatsStore):
        self.word_processor = word_processor
        self.word_stats_store = word_stats_store

    @staticmethod
    def get_instance():
        return instace

    def get_word_count(self, word: str):
        return word_stats_store.get_count(word)

    def report(self, task_type: TaskType, content: str):
        task = Task(task_type=task_type, content=content)
        self.word_processor.submit_task(task)


word_stats_store = WordsStatsStore()
word_stats_store.start()
word_processor = WordsStatsProcessor(max_num_of_workers=5, word_stats_store=word_stats_store)
instace = WordsStatsService(word_processor, word_stats_store)
