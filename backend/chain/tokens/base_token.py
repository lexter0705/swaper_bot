from dataclasses import dataclass


@dataclass(frozen=True)
class Token:
    ticket: str
    decimals: int
    address: str