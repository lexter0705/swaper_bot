import abc


class Encryptor(abc.ABC):
    @abc.abstractmethod
    def encrypt(self, data: str, key: str) -> str:
        pass

    @abc.abstractmethod
    def decrypt(self, data: str, key: str) -> str:
        pass
