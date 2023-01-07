from defichain.exceptions.transactions.notsupported import NotYetSupportedError

from defichain.networks import DefichainMainnet, DefichainTestnet, DefichainRegtest
from .bech32address import Bech32Address


class P2WSH(Bech32Address):
    """TODO: Implement P2WSH Address"""

    def __init__(self, network: DefichainMainnet or DefichainTestnet or DefichainRegtest, address: str):
        super().__init__(network, address)
        raise NotYetSupportedError()
