from chain.dexes.ton.base import TonDexWorker
from chain.tokens.base import Tokens


class StonFiWorker(TonDexWorker):
    def __init__(self, private_key: str, api_key: str, tokens: Tokens):
        super().__init__(private_key, api_key, tokens)

    async def ton_to_token(self, token_ticket_to: str, amount: int):
        token = self.tokens.get_with_truth_ticket(token_ticket_to)
        await self.wallet.stonfi_swap_ton_to_jetton(token.address, amount, jetton_decimals=token.decimals)

    async def token_to_ton(self, token_ticket_from: str, amount: int):
        token = self.tokens.get_with_truth_ticket(token_ticket_from)
        await self.wallet.stonfi_swap_jetton_to_ton(token.address, amount, jetton_decimals=token.decimals)

    async def token_to_token(self, token_ticket_from: str, token_ticket_to: str, amount: int):
        token_from = self.tokens.get_with_truth_ticket(token_ticket_from)
        token_to = self.tokens.get_with_truth_ticket(token_ticket_to)
        await self.wallet.stonfi_swap_jetton_to_jetton(token_from.address, token_to.address, amount,
                                                       from_jetton_decimals=token_from.decimals,
                                                       to_jetton_decimals=token_to.decimals)