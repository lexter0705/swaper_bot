from base64 import urlsafe_b64encode

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from chain.encryptors.base import Encryptor


class EncryptorWithoutSalt(Encryptor):
    def encrypt(self, data: str, key: str) -> str:
        __kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b"",
            iterations=100000,
            backend=default_backend()
        )
        key = urlsafe_b64encode(__kdf.derive(str.encode(key)))
        cipher_suite = Fernet(key)
        encrypted_msg = cipher_suite.encrypt(str.encode(data))
        return str(encrypted_msg)

    def decrypt(self, data: str, key: str) -> str:
        __kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b"",
            iterations=100000,
            backend=default_backend()
        )
        key = urlsafe_b64encode(__kdf.derive(str.encode(key)))
        cipher_suite = Fernet(key)
        encrypted_msg = cipher_suite.decrypt(data)
        return str(encrypted_msg)
