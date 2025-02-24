
from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class UsersTable(Base):
    __tablename__ = 'users'
    id: int = Column(Integer, primary_key=True, unique=True, autoincrement=False)
    private_key: str = Column(String)
    public_key: str = Column(String)


def create_database():
    engine = create_engine('sqlite:///database.db')
    Base.metadata.create_all(engine)
