from multiprocessing import Process
from defichain.exceptions.ServiceUnavailable import ServiceUnavailable
from defichain.exceptions.WrongParmeters import WrongParameters

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
    """
    This is the main interface to communicate with your Defichain Node.
    """
    def __init__(self, user, password, url="127.0.0.1", port=8554, wallet_name="", wallet_path=None, wallet_password="",
                 wallet_timeout=60, protocol="http"):
        """
        Set parameters as needed: just the user and password for your node are mandatory.

        :param user: (required) user witch is set in your defi.conf
        :param password: (required) password witch is set in your defi.conf
        :param url: (optional) the url or ip at which your node can be reached
        :param port: (optional) the port at which your node can be reached
        :param wallet_name: (optional) if your wallet is already imported, enter the name here
        :param wallet_path: (optional) if your wallet is not imported you can specify the path here:
                            it will be imported and becomes usable under the same parameter
        :param wallet_password: (optional) password for wallet if it needs to be decrypted
        :param wallet_timeout: (optional) time to elapse after the wallet is locked again
        :param protocol: (optional) the protocol which is used for the request
        """
        # Parameter Check
        if wallet_name != "" and wallet_path is not None:
            raise WrongParameters(f"Only one parameter of wallet_name or wallet_path may be given at a time!")
        elif wallet_name == "" and wallet_path is not None:
            wallet_name = wallet_path

        # Setup URL
        self.url = f"{protocol}://{user}:{password}@{url}:{port}/wallet/{wallet_name}"

        # Setup all different modules
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

        # Test Connection to Node
        self.test_connection()

        # Prepare Wallet
        self.load_wallet(wallet_path)
        self.decrypt_wallet(wallet_password, wallet_timeout)

    def load_wallet(self, wallet_path):
        """
        Loads wallet into the Node
        :param wallet_path: Path where the wallet is located in the filesystem
        """
        if not wallet_path in self.wallet.listwallets():
            if wallet_path is not None:
                self.wallet.loadwallet(wallet_path)
                print(f"Wallet has bean loaded: {wallet_path}")

    def decrypt_wallet(self, wallet_password, wallet_timeout):
        """
        Decrypts wallet for a specific time if a password is given
        :param wallet_password: wallet password
        :param wallet_timeout: time to elapse until wallet is locked again
        """
        if wallet_password != "":
            self.wallet.walletpassphrase(wallet_password, wallet_timeout)

    def test_connection(self):
        """
        Tests Connection to Defichain Node and raises ServiceUnavailable Exception if no connection occurred
        """
        p = Process(target=self.network.ping, name='ping')
        p.start()
        p.join(timeout=3)
        p.terminate()

        if p.exitcode is None:
            raise ServiceUnavailable("RPC_CLIENT_INVALID_IP_OR_SUBNET: Invalid IP/Subnet")
