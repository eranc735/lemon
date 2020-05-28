from .report_task import TaskType, TaskMessage
from .words_processor import WordsProcessor
from .words_stats import WordsStatsStore
from .word_breakers import WordBreaker


class WordsCountService:

    def __init__(self, word_processor: WordsProcessor, word_stats_store: WordBreaker):
        self.word_processor = word_processor
        self.word_stats_store = word_stats_store

    @staticmethod
    def get_instance():
        return instace

    def get_word_count(self, word: str):
        return word_stats_store.get_count(word)

    def report(self, task_type: TaskType, content: str):
        task = TaskMessage(task_type=task_type, content=content)
        self.word_processor.submit_task(task)

word_stats_store = WordsStatsStore()
word_stats_store.start()
word_breaking_handler = WordBreaker(max_num_of_workers=5, words_stats=word_stats_store)
word_processor = WordsProcessor(max_num_of_workers=5, word_stats_store=word_stats_store,
                                words_breaker=word_breaking_handler)
instace = WordsCountService(word_processor, word_stats_store)
