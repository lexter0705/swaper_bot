import abc

from tonutils.client import TonapiClient
from tonutils.wallet import WalletV4R2

from chain.dexes.base import DexWorker
from chain.tokens.base import Tokens


class TonDexWorker(DexWorker, abc.ABC):
    def __init__(self, private_key: str, api_key: str, tokens: Tokens):
        super().__init__(tokens)
        client = TonapiClient(api_key)
        self.__wallet = WalletV4R2.from_private_key(client, str.encode(private_key))
        self.__tokens = tokens

    async def swap(self, token_ticket_from: str, token_ticket_to: str, amount: int):
        if token_ticket_from == "TON":
            await self.ton_to_token(token_ticket_to, amount)
        elif token_ticket_to == "TON":
            await self.token_to_ton(token_ticket_from, amount)
        else:
            await self.token_to_token(token_ticket_from, token_ticket_to, amount)

    @abc.abstractmethod
    async def ton_to_token(self, token_ticket_to: str, amount: int):
        pass

    @abc.abstractmethod
    async def token_to_ton(self, token_ticket_from: str, amount: int):
        pass

    @abc.abstractmethod
    async def token_to_token(self, token_ticket_from: str, token_ticket_to: str, amount: int):
        pass

    @property
    def wallet(self):
        return self.__wallet