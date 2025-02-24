import requests

from chain.tokens.base import Tokens
from chain.tokens.base_token import Token


class DeDustTokens(Tokens):
    def __init__(self):
        self.__tokens: list[Token] = []
        self.__set_tokens()

    def __set_tokens(self):
        for token in requests.get("https://api.dedust.io/v2/assets").json():
            if token["type"] == "jetton":
                self.__tokens.append(Token(token["symbol"], token["decimals"], token["address"]))

    def get_with_truth_ticket(self, ticket: str) -> Token:
        for token in self.__tokens:
            if token.ticket == ticket:
                return token
        raise Exception(f"Ticket {ticket} not exists")

    def __getitem__(self, item: int) -> Token:
        return self.__tokens[item]

    def __len__(self):
        return len(self.__tokens)
