import abc

class AbstractWord(abc.ABC):

    @abc.abstractmethod
    def get_random_word(self) -> str:
        pass