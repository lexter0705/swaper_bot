from tonutils.client import TonapiClient
from tonutils.wallet import WalletV4R2

from chain.wallet_generators.base import WalletGenerator


class TonWalletGenerator(WalletGenerator):
    def __init__(self, api_key: str):
        self.__client = TonapiClient(api_key)

    def generate(self) -> str:
        _, _, private_key, _ = WalletV4R2.create(self.__client)
        return str(private_key)
