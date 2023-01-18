import hashlib


class Calculate:

    @staticmethod
    def dHash256(h: hex) -> bytes:
        return hashlib.sha256(hashlib.sha256(h).digest()).digest()
