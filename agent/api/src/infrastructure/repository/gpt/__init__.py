from abc import ABC, abstractmethod


class GPTRepository(ABC):

    @abstractmethod
    def setup(self, config):
        raise NotImplementedError

    @abstractmethod
    def answer(self, prompt) -> str:
        raise NotImplementedError
