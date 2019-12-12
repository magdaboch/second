from src.abstract_word import AbstractWord
from src.word import Word
from words_from_file.words_from_file import WordFromFile as Word

if __name__ == '__main__':
    word = Word()
    if not isinstance(word, AbstractWord):
        raise ValueError('Class needs to be AbstractWord instance')
    print(word.get_random_word())



