from defichain.exceptions.transactions.notsupported import NotYetSupportedError

from defichain.networks import DefichainMainnet, DefichainTestnet, DefichainRegtest
from .base58address import Base58Address


class P2PKH(Base58Address):  # Legacy
    """ TODO: Implement P2PKH Address"""

    def __init__(self, network: DefichainMainnet or DefichainTestnet or DefichainRegtest, address: str):
        super().__init__(network, address)
        raise NotYetSupportedError()
