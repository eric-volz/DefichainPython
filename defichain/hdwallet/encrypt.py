import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES


class AESCipher(object):

    def __init__(self, key):
        self._bs = AES.block_size
        self._key = hashlib.sha256(key.encode()).digest()

    def get_block_size(self) -> int:
        return self._bs

    def get_key(self) -> str:
        return self._key.hex()

    def _get_bytes_key(self) -> bytes:
        return self._key

    def encrypt(self, raw:  str) -> str:
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self._get_bytes_key(), AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode())).hex()

    def decrypt(self, enc: str) -> str:
        enc = base64.b64decode(bytes.fromhex(enc))
        iv = enc[:AES.block_size]
        cipher = AES.new(self._get_bytes_key(), AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.get_block_size() - len(s) % self.get_block_size()) * \
            chr(self.get_block_size() - len(s) % self.get_block_size())

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]
