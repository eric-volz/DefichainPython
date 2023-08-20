from .connection import Connection
from .modules import *


class DefichainData:
    """
    Main DefichainData object
    """

    def __init__(self, url: str = "https://api.defichain-data.com/"):
        self.url = url

        self._conn = Connection(self.url)

        self.data = Data(self)
