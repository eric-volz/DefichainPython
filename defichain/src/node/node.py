from .rpc import RPC

from .modules.accounts import Accounts
from .modules.blockchain import Blockchain
from .modules.control import Control
from .modules.generating import Generating
from .modules.loan import Loan
from .modules.masternodes import Masternodes
from .modules.mining import Mining
from .modules.network import Network
from .modules.oracles import Oracles
from .modules.poolpair import Poolpair
from .modules.rawtransactions import Rawtransactions
from .modules.spv import Spv
from .modules.tokens import Tokens
from .modules.util import Util
from .modules.vault import Vault
from .modules.wallet import Wallet
from .modules.zmq import Zmq


class Node:
    def __init__(self, user, password, url="127.0.0.1", port=8554, wallet_path="", protocol="http"):
        self.url = f"{protocol}://{user}:{password}@{url}:{port}{wallet_path}"
        self._rpc = RPC(self.url)

        self.accounts = Accounts(self)
        self.blockchain = Blockchain(self)
        self.control = Control(self)
        self.generating = Generating(self)
        self.icxorderbook = None
        self.loan = Loan(self)
        self.masternodes = Masternodes(self)
        self.mining = Mining(self)
        self.network = Network(self)
        self.oracles = Oracles(self)
        self.poolpair = Poolpair(self)
        self.rawtransactions = Rawtransactions(self)
        self.spv = Spv(self)
        self.tokens = Tokens(self)
        self.util = Util(self)
        self.vault = Vault(self)
        self.wallet = Wallet(self)
        self.zmq = Zmq(self)
