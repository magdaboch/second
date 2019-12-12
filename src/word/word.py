from random import randint

from src.abstract_word import AbstractWord


class Word(AbstractWord):
    __words = ('test', 'blabliblu', 'tarbabobra')

    def get_random_word(self) -> str:
        return self.__words[randint(0, len(self.__words) - 1)]
