from typing import Optional


class NetworkError(Exception):
    """
    Bad network
    """

    def __init__(self, msg):
        self.message = msg
        super().__init__(f"NetworkError: {self.message}")
