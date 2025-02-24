from tonutils.client import TonapiClient
from tonutils.wallet import WalletV4R2
from tonutils.jetton import JettonMaster, JettonWallet
from chain.tokens.base import Tokens
from chain.wallets.base import Wallet


class TonWallet(Wallet):
    def __init__(self, private_key: str, api_key: str, tokens: Tokens):
        self.__client = TonapiClient(api_key=api_key)
        self.__wallet = WalletV4R2.from_private_key(private_key=str.encode(private_key), client=self.__client)
        self.__tokens = tokens

    async def send(self, token: str, address_to: str, amount: int):
        if token == "TON":
            await self.__wallet.transfer(destination=address_to, amount=amount)
        token = self.__tokens.get_with_truth_ticket(token)
        await self.__wallet.transfer_jetton(destination=address_to, jetton_amount=amount, jetton_master_address=token.address,
                                            jetton_decimals=token.decimals)

    async def get_tokens_balance(self) -> dict:
        returned_dict = {"TON": await self.__wallet.get_balance(self.__client, self.__wallet.address)}
        for token in self.__tokens:
            token_wallet_address = await JettonMaster.get_wallet_address(
                client=self.__client,
                owner_address=self.__wallet.address,
                jetton_master_address=token.address,
            )
            token_wallet_data = await JettonWallet.get_wallet_data(
                client=self.__client,
                jetton_wallet_address=token_wallet_address,
            )
            returned_dict[token.ticket] = token_wallet_data.balance
        return returned_dict
