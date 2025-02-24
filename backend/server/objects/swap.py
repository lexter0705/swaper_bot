from pydantic import BaseModel

from server.objects.user import User


class SwapData(BaseModel):
    user: User
    token_from: str
    token_to: str