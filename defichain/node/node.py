from defichain.logger import Logger
from defichain.exceptions.http.ServiceUnavailable import ServiceUnavailable
from defichain.exceptions.http.WrongParmeters import WrongParameters

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
from .modules.proposals import Proposals
from .modules.rawtransactions import Rawtransactions
from .modules.spv import Spv
from .modules.stats import Stats
from .modules.tokens import Tokens
from .modules.util import Util
from .modules.vault import Vault
from .modules.wallet import Wallet
from .modules.zmq import Zmq


class Node:
    """
    This is the main interface to communicate with your Defichain Node.

    User and password are required to connect to the node and can be found in defi.conf.
    Before returning a node object, the connection to the node is tested via ping.

    If your wallet is already imported use: wallet_name to specify to use this wallet.
    if your wallet is not imported use: wallet_path to import the wallet and use it.

    :param user: (required) user witch is set in your defi.conf
    :type user: str
    :param password: (required) password witch is set in your defi.conf
    :type password: str
    :param url: (optional) the url or ip at which your node can be reached (default=localhost)
    :type url: str
    :param port: (optional) the port at which your node can be reached (default=8554)
    :type port: int
    :param wallet_name: (optional) if your wallet is already imported, enter the name here (default="")
    :type wallet_name: str
    :param wallet_path: (optional) if your wallet is not imported you can specify the path here:
                        it will be imported and becomes usable under the same parameter
    :type wallet_path: str
    :param wallet_password: (optional) password for wallet if it needs to be decrypted (default="")
    :type wallet_password: str
    :param wallet_timeout: (optional) time to elapse after the wallet is locked again (default=60)
    :type wallet_timeout: int
    :param protocol: (optional) the protocol which is used for the request (default=http)
    :type protocol: str
    :param logger: (optional) Logger Object
    :type logger: :ref:`Logger`
    :return: Node (object) The object to interact with your Defichain Node

    :example:

            >>> from defichain import Node
            >>> node = Node(user="user", password="password", url="127.0.0.1", port=8554, wallet_name="myWallet", wallet_password="yourPassword", wallet_timeout=60)
            >>> blockcount = node.blockchain.getblockcount()  #  returns block height of the latest block
            >>> print(blockcount)
    """

    def __init__(self, user: str, password: str, url: str = "127.0.0.1", port: int = 8554, wallet_name: str = "",
                 wallet_path: str = None, wallet_password: str = "", wallet_timeout: int = 60,
                 protocol: str = "http", logger: Logger = None):

        # Parameter Check
        if wallet_name != "" and wallet_path is not None:
            raise WrongParameters(f"Only one parameter of wallet_name or wallet_path may be given at a time!")
        elif wallet_name == "" and wallet_path is not None:
            wallet_name = wallet_path

        # Setup URL
        self.url = f"{protocol}://{user}:{password}@{url}:{port}/wallet/{wallet_name}"

        # Setup all different modules
        self._rpc = RPC(self.url, logger)
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
        self.proposals = Proposals(self)
        self.rawtransactions = Rawtransactions(self)
        self.spv = Spv(self)
        self.stats = Stats(self)
        self.tokens = Tokens(self)
        self.util = Util(self)
        self.vault = Vault(self)
        self.wallet = Wallet(self)
        self.zmq = Zmq(self)

        # Test Connection to Node
        self.test_connection()

        # Check if only one wallet
        wallets = self.wallet.listwallets()
        if len(wallets) == 1:  # Only one wallet is loaded
            url = f"{protocol}://{user}:{password}@{url}:{port}/wallet/{wallets[0]}"
            self._rpc.update_url(url)
        # If more than one wallet is loaded the default wallet "" will be used. If you want tu use a specific wallet you
        # have zu specify the wallet in the wallet_name parameter
        elif len(wallets) > 1 and not "" in wallets:
            msg = "Warning: You have not specified an wallet in the wallet_name parameter. If you use an method where " \
                  "an wallet is needed an error will accrue!"
            print(msg)
            if logger:
                logger.error("NodeWarning", msg)

        # Prepare Wallet
        self.load_wallet(wallet_path)
        self.decrypt_wallet(wallet_password, wallet_timeout)

    def decrypt_wallet(self, wallet_password: str, wallet_timeout: int):
        """
        Decrypts wallet for a specific time if a password is given

        :param wallet_password: wallet password
        :type wallet_password: str
        :param wallet_timeout: time to elapse until wallet is locked again
        :type wallet_timeout: int
        """
        if wallet_password != "":
            self.wallet.walletpassphrase(wallet_password, wallet_timeout)

    def load_wallet(self, wallet_path: str):
        """
        Loads wallet into the Node

        :param wallet_path: Path where the wallet is located in the filesystem
        :type wallet_path: str
        """
        if not wallet_path in self.wallet.listwallets():
            if wallet_path is not None:
                self.wallet.loadwallet(wallet_path)
                print(f"Wallet has bean loaded: {wallet_path}")

    def test_connection(self):
        """
        Tests Connection to Defichain Node and raises ServiceUnavailable exception if no connection occurred

        :exception: ServiceUnavailable
        """
        try:
            self.network.ping()
        except ServiceUnavailable as e:
            raise ServiceUnavailable(f"RPC_CLIENT_INVALID_IP_OR_SUBNET: Invalid IP/Subnet {e}")

        except Exception as e:
            raise Exception(e)
