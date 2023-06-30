from typing import Optional


class WalletError(Exception):

    def __init__(self, msg):
        self.message = msg
        super().__init__(f"WalletError: {self.message}")
