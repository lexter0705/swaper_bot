from sqlalchemy import select, insert

from base import DatabaseWorker
from database.creator import UsersTable


class UserWorker(DatabaseWorker):
    def __init__(self, database_path: str):
        super().__init__(database_path)

    def add_new_user(self, public_key: str, private_key: str, user_id: str):
        request = insert(UsersTable).values(user_id=user_id, public_key=public_key, private_key=private_key)
        self.commit(request)

    def get_private_key_by_id(self, user_id: int) -> str:
        request = select(UsersTable.private_key).where(UsersTable.id == user_id)
        return self.connect.execute(request).first()[0]

    def get_public_key_by_id(self, user_id: int) -> str:
        request = select(UsersTable.public_key).where(UsersTable.id == user_id)
        return self.connect.execute(request).first()[0]
