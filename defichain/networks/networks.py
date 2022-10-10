from types import SimpleNamespace
from typing import Any, Optional


class NestedNamespace(SimpleNamespace):
    def __init__(self, dictionary, **kwargs):
        super().__init__(**kwargs)
        for key, value in dictionary.items():
            if isinstance(value, dict):
                self.__setattr__(key, NestedNamespace(value))
            else:
                self.__setattr__(key, value)


class SegwitAddress(NestedNamespace):
    HRP: Optional[str] = None
    VERSION: int = 0x00


class CoinType(NestedNamespace):
    INDEX: int
    HARDENED: bool

    def __str__(self):
        return f"{self.INDEX}'" if self.HARDENED else f"{self.INDEX}"


class ExtendedKey(NestedNamespace):
    P2PKH: int
    P2SH: int

    P2WPKH: Optional[int] = None
    P2WPKH_IN_P2SH: Optional[int] = None

    P2WSH: Optional[int] = None
    P2WSH_IN_P2SH: Optional[int] = None


class ExtendedPrivateKey(ExtendedKey):
    pass


class ExtendedPublicKey(ExtendedKey):
    pass


class Network(NestedNamespace):
    NAME: str
    SYMBOL: str
    NETWORK: str
    SOURCE_CODE: Optional[str]
    COIN_TYPE: CoinType

    SCRIPT_ADDRESS: int
    PUBLIC_KEY_ADDRESS: int
    SEGWIT_ADDRESS: SegwitAddress

    EXTENDED_PRIVATE_KEY: ExtendedPrivateKey
    EXTENDED_PUBLIC_KEY: ExtendedPublicKey

    MESSAGE_PREFIX: Optional[str]
    DEFAULT_PATH: str
    WIF_SECRET_KEY: int


class DefichainMainnet(Network):
    NAME = "Defichain"
    SYMBOL = "DFI"
    NETWORK = "mainnet"
    SOURCE_CODE = "https://github.com/DeFiCh/ain"

    SCRIPT_ADDRESS = 0x5a
    PUBLIC_KEY_ADDRESS = 0x12
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "df",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x0488ade4,
        "P2SH": 0x0488ade4,
        "P2WPKH": 0x0488ade4,
        "P2WPKH_IN_P2SH": 0x0488ade4,
        "P2WSH": 0x0488ade4,
        "P2WSH_IN_P2SH": 0x0488ade4
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x0488b21e,
        "P2SH": 0x0488b21e,
        "P2WPKH": 0x0488b21e,
        "P2WPKH_IN_P2SH": 0x0488b21e,
        "P2WSH": 0x0488b21e,
        "P2WSH_IN_P2SH": 0x0488b21e
    })

    MESSAGE_PREFIX = "\x15Defi Signed Message:\n"
    DEFAULT_PATH = f"m/1129/0/0/0"
    WIF_SECRET_KEY = 0x80


class DefichainTestnet(Network):
    NAME = "Defichain"
    SYMBOL = "DFI"
    NETWORK = "testnet"
    SOURCE_CODE = "https://github.com/DeFiCh/ain"

    SCRIPT_ADDRESS = 0x80
    PUBLIC_KEY_ADDRESS = 0xf
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "tf",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x04358394,
        "P2SH": 0x04358394,
        "P2WPKH": 0x04358394,
        "P2WPKH_IN_P2SH": 0x04358394,
        "P2WSH": 0x04358394,
        "P2WSH_IN_P2SH": 0x04358394
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x043587cf,
        "P2SH": 0x043587cf,
        "P2WPKH": 0x043587cf,
        "P2WPKH_IN_P2SH": 0x043587cf,
        "P2WSH": 0x043587cf,
        "P2WSH_IN_P2SH": 0x043587cf
    })

    MESSAGE_PREFIX = "\x15Defi Signed Message:\n"
    DEFAULT_PATH = f"m/1129/0/0/0"
    WIF_SECRET_KEY = 0xef


class DefichainRegtest(Network):
    NAME = "Defichain"
    SYMBOL = "DFI"
    NETWORK = "regtest"
    SOURCE_CODE = "https://github.com/DeFiCh/ain"

    SCRIPT_ADDRESS = 0xc4
    PUBLIC_KEY_ADDRESS = 0x6f
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "bcrt",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x04358394,
        "P2SH": 0x04358394,
        "P2WPKH": 0x04358394,
        "P2WPKH_IN_P2SH": 0x04358394,
        "P2WSH": 0x04358394,
        "P2WSH_IN_P2SH": 0x04358394
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x043587cf,
        "P2SH": 0x043587cf,
        "P2WPKH": 0x043587cf,
        "P2WPKH_IN_P2SH": 0x043587cf,
        "P2WSH": 0x043587cf,
        "P2WSH_IN_P2SH": 0x043587cf
    })

    MESSAGE_PREFIX = "\x15Defi Signed Message:\n"
    DEFAULT_PATH = f"m/1129/0/0/0"
    WIF_SECRET_KEY = 0xef
