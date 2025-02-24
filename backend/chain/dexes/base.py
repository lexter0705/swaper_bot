import abc

from chain.tokens.base import Tokens


class DexWorker(abc.ABC):
    def __init__(self, tokens: Tokens):
        self.__tokens = tokens

    @abc.abstractmethod
    async def swap(self, token_ticket_from: str, token_ticket_to: str, amount: int):
        pass

    @property
    def tokens(self):
        return self.__tokens

