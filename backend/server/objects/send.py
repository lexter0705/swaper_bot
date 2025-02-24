from pydantic import BaseModel

from server.objects.user import User


class SendData(BaseModel):
    user: User
    to_address: str
    token_address: str