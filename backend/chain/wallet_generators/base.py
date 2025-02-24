import abc


class WalletGenerator(abc.ABC):
    @abc.abstractmethod
    def generate(self) -> str:
        pass
