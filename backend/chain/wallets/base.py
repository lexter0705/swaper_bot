import abc


class Wallet(abc.ABC):
    @abc.abstractmethod
    async def send(self, token: str, address_to: str, amount: int):
        pass

    @abc.abstractmethod
    async def get_tokens_balance(self) -> dict:
        pass