import abc

from chain.tokens.base_token import Token


class Tokens(abc.ABC):
    @abc.abstractmethod
    def __getitem__(self, item: int) -> Token:
        pass

    @abc.abstractmethod
    def __len__(self) -> int:
        pass

    @abc.abstractmethod
    def get_with_truth_ticket(self, ticket: str) -> Token:
        pass