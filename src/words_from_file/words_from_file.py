from random import randint
import os

from src.abstract_word import AbstractWord


class WordFromFile(AbstractWord):
    def get_path(self):
        return os.path.abspath(os.path.dirname(__file__))

    def get_word(self) -> str:
        rand_index = randint(1, self.get_words_count())
        return get_words_from_line(rand_index)

    def get_words_from_line(self, line_number: int) -> str:
        with open(f'{self.get_path()}/words.txt') as file:
            for i in range(1, line_number + 1):
                word = file.readline()

        return word

    def get_words_count(self) -> int:
        words_in_file = 0
        with open(f'{self.get_path()}/words.txt', 'r') as file:
            while file.readline():
                words_in_file += 1

        return words_in_file

    def get_random_word(self):
        return self.get_word()


if __name__ == '__main__':
    words = WordFromFile()
    print(words.get_word())