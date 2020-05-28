import abc
from ..word_breakers import WordBreaker
from ..report_task import TaskMessage


class BaseHandler:

    def __init__(self, words_breaking_handler: WordBreaker):
        self.word_breaking_handler = words_breaking_handler

    @abc.abstractmethod
    def handle(self, task: TaskMessage):
        pass

    def submit_to_word_break(self, text: str):
        self.word_breaking_handler.submit_breaking_task(text)
