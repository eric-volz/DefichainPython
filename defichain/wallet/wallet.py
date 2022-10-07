from ecdsa.curves import SECP256k1
from ecdsa.ellipticcurve import Point
from ecdsa.keys import SigningKey, VerifyingKey

from ecdsa.ecdsa import int_to_string, string_to_int

from binascii import hexlify, unhexlify

from defichain.mnemonic import Mnemonic
from hashlib import sha256
from typing import Optional, Any, Union

import hmac
import ecdsa
import struct
import unicodedata
import hashlib
import base58

from .libs.ripemd160 import ripemd160
from .libs.ecc import S256Point, G
from .libs.bech32 import encode
from .libs.base58 import check_encode, check_decode, ensure_string

from defichain.networks.networks import Cryptocurrency

from .derivations import Derivation

from defichain.exceptions.wallet.DerivationError import DerivationError

from .utils import (
    get_bytes, is_entropy, is_mnemonic, get_entropy_strength, _unhexlify,
    get_mnemonic_language, get_mnemonic_strength, get_semantic
)

MIN_ENTROPY_LEN: int = 128
BIP32KEY_HARDEN: int = 0x80000000

CURVE_GEN: Any = ecdsa.ecdsa.generator_secp256k1
CURVE_ORDER: int = CURVE_GEN.order()
FIELD_ORDER: int = SECP256k1.curve.p()
INFINITY: Point = ecdsa.ellipticcurve.INFINITY


class Wallet:
    """
    Hierarchical Deterministic Wallet

    :param cryptocurrency: Cryptocurrency instance, defaults to ``None``.
    :type cryptocurrency: Cryptocurrency
    :param semantic: Extended semantic, defaults to ``P2PKH``.
    :type semantic: str
    :param use_default_path: Use default derivation path, defaults to ``False``.
    :type use_default_path: bool

    :returns: HDWallet -- Hierarchical Deterministic Wallet instance.

    .. note::
        To initialize HDWallet symbol or cryptocurrency is required.
    """

    def __init__(self, cryptocurrency: Any, semantic: Optional[str] = None, use_default_path: bool = True):
        self._cryptocurrency: Any = None
        if cryptocurrency:
            if not issubclass(cryptocurrency, Cryptocurrency):
                raise TypeError("Invalid Cryptocurrency type, the sub class must be Cryptocurrency instance.")
            self._cryptocurrency: Any = cryptocurrency

        self._strength: Optional[int] = None
        self._entropy: Optional[bytes] = None
        self._mnemonic: Optional[str] = None
        self._language: Optional[str] = None
        self._passphrase: Optional[str] = None

        self._use_default_path: bool = use_default_path
        self._parent_fingerprint: bytes = b"\0\0\0\0"
        self._i: Optional[bytes] = None
        self._path: str = "m"

        self._seed: Optional[bytes] = None
        self._private_key: Optional[bytes] = None
        self._key: Optional[SigningKey] = None
        self._verified_key: Optional[VerifyingKey] = None
        self._semantic: str = semantic
        self._from_class: bool = False
        self._path_class: str = "m"

        self._root_private_key: Optional[tuple] = None
        self._root_public_key: Optional[tuple] = None
        self._private_key: Optional[bytes] = None
        self._public_key: Optional[str] = None
        self._chain_code: Optional[bytes] = None
        self._depth: int = 0
        self._index: int = 0

        self._root_depth: int = 0
        self._root_parent_fingerprint: bytes = b"\0\0\0\0"
        self._root_index: int = 0

    def from_entropy(self, entropy: str, language: str = "english", passphrase: str = None) -> "Wallet":
        """
        Master from Entropy hex string.

        :param entropy: Entropy hex string.
        :type entropy: str
        :param language: Mnemonic language, default to ``english``.
        :type language: str
        :param passphrase: Mnemonic passphrase or password, default to ``None``.
        :type passphrase: str

        :returns: HDWallet -- Hierarchical Deterministic Wallet instance.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_entropy(entropy="ee535b143b0d9d1f87546f9df0d06b1a", language="english", passphrase=None)
        <wallet.wallet.HDWallet object at 0x000001E8BFB98D60>
        """

        if not is_entropy(entropy=entropy):
            raise ValueError("Invalid entropy.")
        if language and language not in ["english", "french", "italian", "japanese",
                                         "chinese_simplified", "chinese_traditional", "korean", "spanish"]:
            raise ValueError("Invalid language, choose only the following options 'english', 'french', 'italian', "
                             "'spanish', 'chinese_simplified', 'chinese_traditional', "
                             "'japanese' or 'korean' languages.")

        self._strength = get_entropy_strength(entropy=entropy)
        self._entropy, self._language = unhexlify(entropy), language
        self._passphrase = str(passphrase) if passphrase else str()
        mnemonic = Mnemonic(language=self._language).to_mnemonic(data=self._entropy)
        self._mnemonic = unicodedata.normalize("NFKD", mnemonic)
        self._seed = Mnemonic.to_seed(mnemonic=self._mnemonic, passphrase=self._passphrase)
        if self._semantic is None:
            self._semantic = "p2pkh"
        return self.from_seed(seed=hexlify(self._seed).decode())

    def from_mnemonic(self, mnemonic: str, language: str = None, passphrase: str = None) -> "Wallet":
        """
        Master from Mnemonic words.

        :param mnemonic: Mnemonic words.
        :type mnemonic: str
        :param language: Mnemonic language, default to ``None``.
        :type language: str
        :param passphrase: Mnemonic passphrase or password, default to ``None``.
        :type passphrase: str

        :returns: HDWallet -- Hierarchical Deterministic Wallet instance.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="sceptre capter séquence girafe absolu relatif fleur zoologie muscle sirop saboter parure", passphrase=None)
        <wallet.wallet.HDWallet object at 0x000001E8BFB98D60>
        """

        if not is_mnemonic(mnemonic=mnemonic, language=language):
            print(is_mnemonic(mnemonic=mnemonic, language=language))
            raise ValueError("Invalid mnemonic words.")

        self._mnemonic = unicodedata.normalize("NFKD", mnemonic)
        self._strength = get_mnemonic_strength(mnemonic=self._mnemonic)
        self._language = language if language else get_mnemonic_language(mnemonic=self._mnemonic)
        self._entropy = Mnemonic(language=self._language).to_entropy(self._mnemonic)
        self._passphrase = str(passphrase) if passphrase else str()
        self._seed = Mnemonic.to_seed(mnemonic=self._mnemonic, passphrase=self._passphrase)
        if self._semantic is None:
            self._semantic = "p2pkh"
        return self.from_seed(seed=hexlify(self._seed).decode())

    def from_seed(self, seed: str) -> "Wallet":
        """
        Master from Seed hex string.

        :param seed: Seed hex string.
        :type seed: str

        :returns: HDWallet -- Hierarchical Deterministic Wallet instance.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_seed(seed="8d5f4fe5b81a6a6a18b08603b6b3f59df9f4bbb25d10c55d23e0cbdc5ee385e5fddad9d7e6114f11afdec45928328081f9a598151a7613dc5f5a0c16a4612aa4")
        <wallet.wallet.HDWallet object at 0x000001E8BFB98D60>
        """

        self._seed = unhexlify(seed)
        self._i = hmac.new(b"@defichain/jellyfish-wallet-mnemonic", get_bytes(seed), hashlib.sha512).digest()
        il, ir = self._i[:32], self._i[32:]
        self._root_private_key = (il, ir)
        parse_il = int.from_bytes(il, "big")
        if parse_il == 0 or parse_il >= SECP256k1.order:
            raise ValueError("Bad seed, resulting in invalid key!")

        self._private_key, self._chain_code = il, ir
        self._key = ecdsa.SigningKey.from_string(self._private_key, curve=SECP256k1)
        self._verified_key = self._key.get_verifying_key()
        if self._use_default_path:
            self.from_path(path=self._cryptocurrency.DEFAULT_PATH)
        self._public_key = self.compressed()
        if self._from_class:
            self.from_path(path=self._path_class)
        if self._semantic is None:
            self._semantic = "p2pkh"
        return self

    def from_xprivate_key(self, xprivate_key: str, strict: bool = False) -> "Wallet":
        """
        Master from XPrivate Key.

        :param xprivate_key: Root or Non-Root XPrivate key.
        :type xprivate_key: str
        :param strict: Strict for must be root xprivate key, default to ``False``.
        :type strict: bool

        :returns: HDWallet -- Hierarchical Deterministic Wallet instance.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_xprivate_key(xprivate_key="xprv9s21ZrQH143K3xPGUzpogJeKtRdjHkK6muBJo8v7rEVRzT83xJgNcLpMoJXUf9wJFKfuHR4SGvfgdShh4t9VmjjrE9usBunK3LfNna31LGF")
        <wallet.wallet.HDWallet object at 0x000001E8BFB98D60>
        """

        _deserialize_xprivate_key = self._deserialize_xprivate_key(xprivate_key=xprivate_key)
        self._root_depth, self._root_parent_fingerprint, self._root_index = (
            int.from_bytes(_deserialize_xprivate_key[1], "big"),
            _deserialize_xprivate_key[2],
            struct.unpack(">L", _deserialize_xprivate_key[3])[0]
        )
        self._depth, self._parent_fingerprint, self._index = (
            int.from_bytes(_deserialize_xprivate_key[1], "big"),
            _deserialize_xprivate_key[2],
            struct.unpack(">L", _deserialize_xprivate_key[3])[0]
        )
        self._i = _deserialize_xprivate_key[5] + _deserialize_xprivate_key[4]
        self._root_private_key = (_deserialize_xprivate_key[5], _deserialize_xprivate_key[4])
        self._private_key, self._chain_code = self._i[:32], self._i[32:]
        self._key = ecdsa.SigningKey.from_string(_deserialize_xprivate_key[5], curve=SECP256k1)
        self._verified_key = self._key.get_verifying_key()
        if self._use_default_path:
            self.from_path(path=self._cryptocurrency.DEFAULT_PATH)
        if self._from_class:
            self.from_path(path=self._path_class)
        self._public_key = self.compressed()
        self._semantic = get_semantic(
            _cryptocurrency=self._cryptocurrency,
            version=_deserialize_xprivate_key[0],
            key_type="private_key"
        )
        return self

    def from_xpublic_key(self, xpublic_key: str, strict: bool = False) -> "Wallet":
        """
        Master from XPublic Key.

        :param xpublic_key: Root or Non-Root XPublic key.
        :type xpublic_key: str
        :param strict: Strict for must be root xpublic key, default to ``False``.
        :type strict: bool

        :returns: HDWallet -- Hierarchical Deterministic Wallet instance.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_xpublic_key(xpublic_key="xpub661MyMwAqRbcGSTjb2Mp3Sb4STUDhD2x986ubXKjQa2QsFTCVqzdA98qeZjcncHT1AaZcMSjiP1HJ16jH97q72RwyFfiNhmG8zQ6KBB5PaQ")
        <wallet.wallet.HDWallet object at 0x000001E8BFB98D60>
        """

        _deserialize_xpublic_key = self._deserialize_xpublic_key(xpublic_key=xpublic_key)
        self._root_depth, self._root_parent_fingerprint, self._root_index = (
            int.from_bytes(_deserialize_xpublic_key[1], "big"),
            _deserialize_xpublic_key[2],
            struct.unpack(">L", _deserialize_xpublic_key[3])[0]
        )
        self._depth, self._parent_fingerprint, self._index = (
            int.from_bytes(_deserialize_xpublic_key[1], "big"),
            _deserialize_xpublic_key[2],
            struct.unpack(">L", _deserialize_xpublic_key[3])[0]
        )
        self._chain_code = _deserialize_xpublic_key[4]
        self._verified_key = ecdsa.VerifyingKey.from_string(
            _deserialize_xpublic_key[5], curve=SECP256k1
        )
        self._root_public_key = (
            _deserialize_xpublic_key[5], _deserialize_xpublic_key[4]
        )
        if self._use_default_path:
            self.from_path(path=self._cryptocurrency.DEFAULT_PATH)
        if self._from_class:
            self.from_path(path=str(self._path_class).replace("'", ""))
        self._public_key = self.compressed()
        self._semantic = get_semantic(
            _cryptocurrency=self._cryptocurrency,
            version=_deserialize_xpublic_key[0],
            key_type="public_key"
        )
        return self

    def from_wif(self, wif: str) -> "Wallet":
        """
        Master from Wallet Important Format (WIF).

        :param wif: Wallet important format.
        :type wif: str

        :returns: HDWallet -- Hierarchical Deterministic Wallet instance.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_wif(wif="KzsHWUJsrTWUUhBGPfMMxLLydiH7NhEn6z7mKHXD5qNkUWaC4TEn")
        <wallet.wallet.HDWallet object at 0x000001E8BFB98D60>
        """

        raw = check_decode(wif)[:-1]
        if not raw.startswith(_unhexlify(self._cryptocurrency.WIF_SECRET_KEY)):
            raise ValueError(f"Invalid {self.cryptocurrency()} wallet important format.")

        self._private_key = raw.split(_unhexlify(self._cryptocurrency.WIF_SECRET_KEY), 1).pop()
        self._key = ecdsa.SigningKey.from_string(self._private_key, curve=SECP256k1)
        self._verified_key = self._key.get_verifying_key()
        self._public_key = self.compressed()
        return self

    def from_private_key(self, private_key: str) -> "Wallet":
        """
        Master from Private Key.

        :param private_key: Private key.
        :type private_key: str

        :returns: HDWallet -- Hierarchical Deterministic Wallet instance.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_private_key(private_key="6cd78b0d69eab1a47bfa53a52b9d8c4331e858b5d7a599270a95d9735fdb0b94")
        <wallet.wallet.HDWallet object at 0x000001E8BFB98D60>
        """

        self._private_key = unhexlify(private_key)
        self._key = ecdsa.SigningKey.from_string(self._private_key, curve=SECP256k1)
        self._verified_key = self._key.get_verifying_key()
        self._public_key = self.compressed()
        return self

    def from_public_key(self, public_key: str) -> "Wallet":
        """
        Master from Public Key.

        :param public_key: Public key.
        :type public_key: str

        :returns: HDWallet -- Hierarchical Deterministic Wallet instance.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_public_key(public_key="02f93f58b97c3bb616645c3dda256ec946d87c45baf531984c022dd0fd1503b0a8")
        <wallet.wallet.HDWallet object at 0x000001E8BFB98D60>
        """

        self._verified_key = ecdsa.VerifyingKey.from_string(
            unhexlify(public_key), curve=SECP256k1
        )
        self._public_key = self.compressed()
        return self

    def from_path(self, path: Union[str, Derivation]) -> "Wallet":
        """
        Derivation from Path.

        :param path: Derivation path.
        :type path: str, Derivation

        :returns: HDWallet -- Hierarchical Deterministic Wallet instance.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_xprivate_key(xprivate_key="xprv9s21ZrQH143K3xPGUzpogJeKtRdjHkK6muBJo8v7rEVRzT83xJgNcLpMoJXUf9wJFKfuHR4SGvfgdShh4t9VmjjrE9usBunK3LfNna31LGF")
        >>> wallet.from_path(path="m/44'/0'/'0/0/0")
        <wallet.wallet.HDWallet object at 0x000001E8BFB98D60>
        """

        if isinstance(path, Derivation):
            path = str(path)
        elif str(path)[0:2] != "m/":
            raise ValueError("Bad path, please insert like this type of path \"m/0'/0\"! ")

        self.clean_derivation()  # clean path derivation

        for index in path.lstrip("m/").split("/"):
            if "'" in index:
                self._derive_key_by_index(int(index[:-1]) + BIP32KEY_HARDEN)
                self._path += str("/" + index)
            else:
                self._derive_key_by_index(int(index))
                self._path += str("/" + index)
        return self

    def from_index(self, index: int, hardened: bool = False) -> "Wallet":
        """
        Derivation from Index.

        :param index: Derivation index.
        :type index: int
        :param hardened: Hardened address, default to ``False``.
        :type hardened: bool

        :returns: HDWallet -- Hierarchical Deterministic Wallet instance.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_xprivate_key(xprivate_key="xprv9s21ZrQH143K3xPGUzpogJeKtRdjHkK6muBJo8v7rEVRzT83xJgNcLpMoJXUf9wJFKfuHR4SGvfgdShh4t9VmjjrE9usBunK3LfNna31LGF")
        >>> wallet.from_index(index=44, hardened=True)
        >>> wallet.from_index(index=0, hardened=True)
        >>> wallet.from_index(index=0, hardened=True)
        >>> wallet.from_index(index=0)
        >>> wallet.from_index(index=0)
        <wallet.wallet.HDWallet object at 0x000001E8BFB98D60>
        """

        if not isinstance(index, int):
            raise ValueError("Bad index, Please import only integer number!")

        if hardened:
            self._path += ("/%d'" % index)
            self._derive_key_by_index(index + BIP32KEY_HARDEN)
        else:
            self._path += ("/%d" % index)
            return self._derive_key_by_index(index)

    def _derive_key_by_index(self, index) -> Optional["Wallet"]:

        if not self._root_private_key and not self._root_public_key:
            raise ValueError("You can't drive this master key.")

        i_str = struct.pack(">L", index)
        if index & BIP32KEY_HARDEN:
            if self._key is None:
                raise DerivationError("Hardened derivation path is invalid for xpublic key.")
            data = b"\0" + self._key.to_string() + i_str
        else:
            data = unhexlify(self.public_key()) + i_str

        if not self._chain_code:
            raise ValueError("You can't drive xprivate_key and private_key.")

        i = hmac.new(self._chain_code, data, hashlib.sha512).digest()
        il, ir = i[:32], i[32:]

        il_int = string_to_int(il)
        if il_int > CURVE_ORDER:
            return None

        if self._key:
            pvt_int = string_to_int(self._key.to_string())
            k_int = (il_int + pvt_int) % CURVE_ORDER
            if k_int == 0:
                return None
            secret = (b"\0" * 32 + int_to_string(k_int))[-32:]

            self._private_key, self._chain_code, self._depth, self._index, self._parent_fingerprint = (
                secret, ir, (self._depth + 1), index, unhexlify(self.finger_print())
            )
            self._key = ecdsa.SigningKey.from_string(self._private_key, curve=SECP256k1)
            self._verified_key = self._key.get_verifying_key()
        else:
            key_point = S256Point.parse(unhexlify(self.public_key()))
            left_point = il_int * G
            total = key_point + left_point

            self._chain_code, self._depth, self._index, self._parent_fingerprint = (
                ir, (self._depth + 1), index, unhexlify(self.finger_print())
            )
            self._verified_key = ecdsa.VerifyingKey.from_string(
                total.sec(), curve=SECP256k1
            )
        return self

    @staticmethod
    def _deserialize_xprivate_key(xprivate_key: str, encoded: bool = True) -> tuple:
        decoded_xprivate_key = check_decode(xprivate_key) if encoded else xprivate_key
        if len(decoded_xprivate_key) != 78:  # 156
            raise ValueError("Invalid xprivate key.")
        return (
            decoded_xprivate_key[:4], decoded_xprivate_key[4:5],
            decoded_xprivate_key[5:9], decoded_xprivate_key[9:13],
            decoded_xprivate_key[13:45], decoded_xprivate_key[46:]
        )

    @staticmethod
    def _deserialize_xpublic_key(xpublic_key: str, encoded: bool = True) -> tuple:
        decoded_xpublic_key = check_decode(xpublic_key) if encoded else xpublic_key
        if len(decoded_xpublic_key) != 78:  # 156
            raise ValueError("Invalid xpublic key.")
        return (
            decoded_xpublic_key[:4], decoded_xpublic_key[4:5],
            decoded_xpublic_key[5:9], decoded_xpublic_key[9:13],
            decoded_xpublic_key[13:45], decoded_xpublic_key[45:]
        )

    @staticmethod
    def _serialize_xkeys(version: bytes, depth: bytes, parent_fingerprint: bytes, index: bytes,
                         chain_code: bytes, data: bytes, encoded: bool = True) -> Optional[str]:
        try:
            raw = (version + depth + parent_fingerprint + index + chain_code + data)
            return check_encode(raw) if encoded else raw.hex()
        except TypeError:
            return None

    def root_xprivate_key(self, encoded: bool = True) -> Optional[str]:
        """
        Get Root XPrivate Key.

        :param encoded: Encoded root xprivate key, default to ``True``.
        :type encoded: bool

        :returns: str -- Root XPrivate Key.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_entropy(entropy="ee535b143b0d9d1f87546f9df0d06b1a")
        >>> wallet.from_path(path="m/44'/0'/'0/0/0")
        >>> wallet.root_xprivate_key()
        "xprv9s21ZrQH143K3xPGUzpogJeKtRdjHkK6muBJo8v7rEVRzT83xJgNcLpMoJXUf9wJFKfuHR4SGvfgdShh4t9VmjjrE9usBunK3LfNna31LGF"
        """

        if self._semantic is None:
            return None
        version = self._cryptocurrency.EXTENDED_PRIVATE_KEY.__getattribute__(
            self._semantic.upper()
        )
        if version is None:
            raise NotImplementedError(
                f"{self.__class__.__name__} is not implemented for {self._cryptocurrency.NAME} {self._cryptocurrency.NETWORK} cryptocurrency."
            )
        if not self._i:
            return None
        secret_key, chain_code = self._i[:32], self._i[32:]
        depth = bytes(bytearray([self._root_depth]))
        parent_fingerprint = self._root_parent_fingerprint
        index = struct.pack(">L", self._root_index)
        data = b"\x00" + secret_key
        return self._serialize_xkeys(
            _unhexlify(version), depth, parent_fingerprint, index, chain_code, data, encoded
        )

    def root_xpublic_key(self, encoded: bool = True) -> Optional[str]:
        """
        Get Root XPublic Key.

        :param encoded: Encoded root xpublic key, default to ``True``.
        :type encoded: bool

        :returns: str -- Root XPublic Key.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_entropy(entropy="ee535b143b0d9d1f87546f9df0d06b1a")
        >>> wallet.from_path(path="m/44'/0'/'0/0/0")
        >>> wallet.root_xpublic_key()
        "xpub661MyMwAqRbcGSTjb2Mp3Sb4STUDhD2x986ubXKjQa2QsFTCVqzdA98qeZjcncHT1AaZcMSjiP1HJ16jH97q72RwyFfiNhmG8zQ6KBB5PaQ"
        """

        if self._semantic is None:
            return None
        version = self._cryptocurrency.EXTENDED_PUBLIC_KEY.__getattribute__(
            self._semantic.upper()
        )
        if version is None:
            raise NotImplementedError(
                f"{self.__class__.__name__} is not implemented for {self._cryptocurrency.NAME} {self._cryptocurrency.NETWORK} cryptocurrency."
            )
        if self._root_public_key:
            data, chain_code = (
                self._root_public_key[0], self._root_public_key[1]
            )
        elif not self._i:
            return None
        else:
            secret_key, chain_code = self._i[:32], self._i[32:]
            data = unhexlify(self.public_key(private_key=secret_key.hex()))
        depth = bytes(bytearray([self._root_depth]))
        parent_fingerprint = self._root_parent_fingerprint
        index = struct.pack(">L", self._root_index)
        return self._serialize_xkeys(
            _unhexlify(version), depth, parent_fingerprint, index, chain_code, data, encoded
        )

    def xprivate_key(self, encoded=True) -> Optional[str]:
        """
        Get XPrivate Key.

        :param encoded: Encoded xprivate key, default to ``True``.
        :type encoded: bool

        :returns: str -- Root XPrivate Key.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_entropy(entropy="ee535b143b0d9d1f87546f9df0d06b1a")
        >>> wallet.from_path(path="m/44'/0'/'0/0/0")
        >>> wallet.xprivate_key()
        "xprvA3BYGWQ9FmhyaNRRXB2f1LphNPnaY9T6gngw4BaTbkFtscSH4RCuJhgWUSKs9S6ciGioHd4TX4UeyUg53MkfN9Xh38xkS1j2Wb9YKsYpJHQ"
        """

        if self._semantic is None:
            return None
        version = self._cryptocurrency.EXTENDED_PRIVATE_KEY.__getattribute__(
            self._semantic.upper()
        )
        if version is None:
            raise NotImplementedError(
                f"{self.__class__.__name__} is not implemented for {self._cryptocurrency.NAME} {self._cryptocurrency.NETWORK} cryptocurrency."
            )
        depth = bytes(bytearray([self._depth]))
        parent_fingerprint = self._parent_fingerprint
        index = struct.pack(">L", self._index)
        chain_code = self._chain_code
        if self.private_key() is None:
            return None
        data = b"\x00" + unhexlify(self.private_key())
        return self._serialize_xkeys(
            _unhexlify(version), depth, parent_fingerprint, index, chain_code, data, encoded
        )

    def xpublic_key(self, encoded: bool = True) -> Optional[str]:
        """
        Get XPublic Key.

        :param encoded: Encoded xpublic key, default to ``True``.
        :type encoded: bool

        :returns: str -- XPublic Key.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_entropy(entropy="ee535b143b0d9d1f87546f9df0d06b1a")
        >>> wallet.from_path(path="m/44'/0'/'0/0/0")
        >>> wallet.xpublic_key()
        "xpub6GAtg1w369GGnrVtdCZfNUmRvRd4wcAx41cXrZz5A5nskQmRbxX9rVzzKiRU4JruirBrfm4KQXNSU7GfqL1tzZWpZYe9Zo4xKGJYohWoQe7"
        """

        if self._semantic is None:
            return None
        version = self._cryptocurrency.EXTENDED_PUBLIC_KEY.__getattribute__(
            self._semantic.upper()
        )
        if version is None:
            raise NotImplementedError(
                f"{self.__class__.__name__} is not implemented for {self._cryptocurrency.NAME} {self._cryptocurrency.NETWORK} cryptocurrency."
            )
        depth = bytes(bytearray([self._depth]))
        parent_fingerprint = self._parent_fingerprint
        index = struct.pack(">L", self._index)
        chain_code = self._chain_code
        data = unhexlify(self.public_key())
        return self._serialize_xkeys(
            _unhexlify(version), depth, parent_fingerprint, index, chain_code, data, encoded
        )

    def clean_derivation(self) -> "Wallet":
        """
        Clean derivation Path or Indexes.

        :returns: HDWallet -- Hierarchical Deterministic Wallet instance.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_xprivate_key(xprivate_key="xprv9s21ZrQH143K3xPGUzpogJeKtRdjHkK6muBJo8v7rEVRzT83xJgNcLpMoJXUf9wJFKfuHR4SGvfgdShh4t9VmjjrE9usBunK3LfNna31LGF")
        >>> wallet.from_path(path="m/44'/0'/'0/0/0")
        >>> wallet.path()
        "m/44'/0'/'0/0/0"
        >>> wallet.clean_derivation()
        <wallet.wallet.HDWallet object at 0x000001E8BFB98D60>
        >>> wallet.path()
        None
        """

        if self._root_private_key:
            self._path, self._path_class, self._depth, self._parent_fingerprint, self._index = (
                "m", "m", 0, b"\0\0\0\0", 0
            )
            self._private_key, self._chain_code = self._root_private_key
            self._key = ecdsa.SigningKey.from_string(self._private_key, curve=SECP256k1)
            self._verified_key = self._key.get_verifying_key()
        elif self._root_public_key:
            self._path, self._path_class, self._depth, self._parent_fingerprint, self._index = (
                "m", "m", 0, b"\0\0\0\0", 0
            )
            self._chain_code = self._root_public_key[1]
            self._verified_key = ecdsa.VerifyingKey.from_string(
                self._root_public_key[0], curve=SECP256k1
            )
        return self

    def uncompressed(self, compressed: Optional[str] = None) -> str:
        """
        Get Uncommpresed Public Key.

        :param compressed: Compressed public key, default to ``None``.
        :type compressed: str

        :returns: str -- Uncommpresed public key.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="venture fitness paper little blush april rigid where find volcano fetch crack label polar dash")
        >>> wallet.from_path(path="m/44'/0'/0'/0/0")
        >>> wallet.uncompressed()
        "f93f58b97c3bb616645c3dda256ec946d87c45baf531984c022dd0fd1503b0a875f63285a539213ac241fc4a88e7137ba1c8d897b1c1e5efb81bfc6b45a22d40"
        """

        p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
        public_key = unhexlify(compressed) if compressed else unhexlify(self.compressed())
        x = int.from_bytes(public_key[1:33], byteorder='big')
        y_sq = (pow(x, 3, p) + 7) % p
        y = pow(y_sq, (p + 1) // 4, p)
        if y % 2 != public_key[0] % 2:
            y = p - y
        y = y.to_bytes(32, byteorder='big')
        return (public_key[1:33] + y).hex()

    def compressed(self, uncompressed: Optional[str] = None) -> str:
        """
        Get Compresed Public Key.

        :param uncompressed: Uncompressed public key, default to ``None``.
        :type uncompressed: str

        :returns: str -- Commpresed public key.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="venture fitness paper little blush april rigid where find volcano fetch crack label polar dash")
        >>> wallet.from_path(path="m/44'/0'/0'/0/0")
        >>> wallet.compressed()
        "02f93f58b97c3bb616645c3dda256ec946d87c45baf531984c022dd0fd1503b0a8"
        """

        _verified_key = ecdsa.VerifyingKey.from_string(
            unhexlify(uncompressed), curve=SECP256k1
        ) if uncompressed else self._verified_key
        padx = (b"\0" * 32 + int_to_string(
            _verified_key.pubkey.point.x()))[-32:]
        if _verified_key.pubkey.point.y() & 1:
            ck = b"\3" + padx
        else:
            ck = b"\2" + padx
        return hexlify(ck).decode()

    def private_key(self) -> str:
        """
        Get Private Key.

        :returns: str -- Private key.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="venture fitness paper little blush april rigid where find volcano fetch crack label polar dash")
        >>> wallet.from_path(path="m/44'/0'/0'/0/0")
        >>> wallet.private_key()
        "6cd78b0d69eab1a47bfa53a52b9d8c4331e858b5d7a599270a95d9735fdb0b94"
        """

        return hexlify(self._key.to_string()).decode() if self._key else None

    def public_key(self, compressed: bool = True, private_key: Optional[str] = None) -> str:
        """
        Get Public Key.

        :param compressed: Compressed public key, default to ``True``.
        :type compressed: bool
        :param private_key: Private key hex string, default to ``None``.
        :type private_key: str

        :returns: str -- Public key.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="venture fitness paper little blush april rigid where find volcano fetch crack label polar dash")
        >>> wallet.from_path(path="m/44'/0'/0'/0/0")
        >>> wallet.public_key()
        "02f93f58b97c3bb616645c3dda256ec946d87c45baf531984c022dd0fd1503b0a8"
        """

        if private_key:
            key = ecdsa.SigningKey.from_string(
                unhexlify(private_key), curve=SECP256k1)
            verified_key = key.get_verifying_key()
            padx = (b"\0" * 32 + int_to_string(
                verified_key.pubkey.point.x()))[-32:]
            if verified_key.pubkey.point.y() & 1:
                ck = b"\3" + padx
            else:
                ck = b"\2" + padx
            return hexlify(ck).decode() if compressed else self.uncompressed(compressed=hexlify(ck).decode())
        return self.compressed() if compressed else self.uncompressed()

    def strength(self) -> Optional[int]:
        """
        Get Entropy strength.

        :returns: int -- Entropy strength.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="venture fitness paper little blush april rigid where find volcano fetch crack label polar dash")
        >>> wallet.strength()
        160
        """

        return self._strength if self._strength else None

    def entropy(self) -> Optional[str]:
        """
        Get Entropy hex string.

        :returns: str -- Entropy hex string.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="venture fitness paper little blush april rigid where find volcano fetch crack label polar dash")
        >>> wallet.entropy()
        "f24afe7fc1418815ee7fd256beb55518e7c34ecd"
        """

        return hexlify(self._entropy).decode() if self._entropy else None

    def mnemonic(self) -> Optional[str]:
        """
        Get Mnemonic words.

        :returns: str -- Mnemonic words.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="venture fitness paper little blush april rigid where find volcano fetch crack label polar dash")
        >>> wallet.mnemonic()
        "venture fitness paper little blush april rigid where find volcano fetch crack label polar dash"
        """

        return unicodedata.normalize("NFKD", self._mnemonic) if self._mnemonic else None

    def passphrase(self) -> Optional[str]:
        """
        Get Mnemonic passphrase.

        :returns: str -- Mnemonic passphrase.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="venture fitness paper little blush april rigid where find volcano fetch crack label polar dash", passphrase="password")
        >>> wallet.passphrase()
        "password"
        """

        return str(self._passphrase) if self._passphrase else None

    def language(self) -> Optional[str]:
        """
        Get Mnemonic language.

        :returns: str -- Mnemonic language.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="venture fitness paper little blush april rigid where find volcano fetch crack label polar dash", passphrase="password")
        >>> wallet.language()
        "english"
        """

        return str(self._language) if self._language else None

    def cryptocurrency(self) -> Optional[str]:
        """
        Get Cryptocurrency name.

        :returns: str -- Cryptocurrency name.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="venture fitness paper little blush april rigid where find volcano fetch crack label polar dash", passphrase="password")
        >>> wallet.cryptocurrency()
        "Bitcoin"
        """

        return str(self._cryptocurrency.NAME)

    def symbol(self) -> Optional[str]:
        """
        Get Cryptocurrency symbol.

        :returns: str -- Cryptocurrency symbol.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="venture fitness paper little blush april rigid where find volcano fetch crack label polar dash", passphrase="password")
        >>> wallet.symbol()
        "BTC"
        """

        return str(self._cryptocurrency.SYMBOL)

    def semantic(self) -> Optional[str]:
        """
        Get Extended semantic.

        :returns: str -- Extended semantic.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="venture fitness paper little blush april rigid where find volcano fetch crack label polar dash", passphrase="password")
        >>> wallet.semantic()
        "p2pkh"
        """

        return self._semantic if self._semantic else None

    def network(self) -> Optional[str]:
        """
        Get Cryptocurrency network type.

        :returns: str -- Cryptocurrency network type.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="venture fitness paper little blush april rigid where find volcano fetch crack label polar dash", passphrase="password")
        >>> wallet.network()
        "mainnet"
        """

        return str(self._cryptocurrency.NETWORK)

    def seed(self) -> Optional[str]:
        """
        Get Seed hex string.

        :returns: str -- Seed hex string.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="venture fitness paper little blush april rigid where find volcano fetch crack label polar dash", passphrase="password")
        >>> wallet.from_path(path="m/44'/0'/0'/0/0")
        >>> wallet.seed()
        "8d5f4fe5b81a6a6a18b08603b6b3f59df9f4bbb25d10c55d23e0cbdc5ee385e5fddad9d7e6114f11afdec45928328081f9a598151a7613dc5f5a0c16a4612aa4"
        """

        return hexlify(self._seed).decode() if self._seed else None

    def path(self) -> Optional[str]:
        """
        Get Derivation path.

        :returns: str -- Drivation path.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="venture fitness paper little blush april rigid where find volcano fetch crack label polar dash", passphrase="password")
        >>> wallet.from_path(path="m/44'/0'/0'/0/0")
        >>> wallet.path()
        "m/44'/0'/0'/0/0"
        """

        return str(self._path) if not self._path == "m" else None

    def chain_code(self) -> Optional[str]:
        """
        Get Chain code.

        :returns: str -- Chain code.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="venture fitness paper little blush april rigid where find volcano fetch crack label polar dash", passphrase="password")
        >>> wallet.from_path(path="m/44'/0'/0'/0/0")
        >>> wallet.chain_code()
        "ed45793b944d1f22522f2d6f48c487029fae2cfcd999ed23087a148bcdda6314"
        """

        return hexlify(self._chain_code).decode() if self._chain_code else None

    def hash(self, private_key: str = None):
        """
        Get Public Key Hash.

        :returns: str -- Identifier.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="venture fitness paper little blush april rigid where find volcano fetch crack label polar dash", passphrase="password")
        >>> wallet.from_path(path="m/44'/0'/0'/0/0")
        >>> wallet.hash()
        "4d887566d408dfe5ea8090f2b716f9639523ca89"
        """

        return hexlify(ripemd160(sha256(unhexlify(self.public_key(
            private_key=private_key if private_key else self.private_key()
        ))).digest())).decode("utf-8")

    def finger_print(self) -> str:
        """
        Get Finger print.

        :returns: str -- Finger print.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="venture fitness paper little blush april rigid where find volcano fetch crack label polar dash", passphrase="password")
        >>> wallet.from_path(path="m/44'/0'/0'/0/0")
        >>> wallet.finger_print()
        "4d887566"
        """

        return self.hash(self.private_key())[:8]

    def default_address(self) -> str:
        """
        Get P2WPKH nested in P2SH address.

        :returns: str -- P2WPKH nested in P2SH address.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="venture fitness paper little blush april rigid where find volcano fetch crack label polar dash", passphrase="password")
        >>> wallet.from_path(path="m/44'/0'/0'/0/0")
        >>> wallet._p2wpkh_in_p2sh_address()
        "3CCrxPrHNa6ePbnB7qjh7S3vaPx9qiLc3e"
        """
        return self._p2wpkh_in_p2sh_address()

    def legacy_address(self) -> str:
        """
        Get Pay to Public Key Hash (P2PKH) address.

        :returns: str -- P2PKH address.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="venture fitness paper little blush april rigid where find volcano fetch crack label polar dash", passphrase="password")
        >>> wallet.from_path(path="m/44'/0'/0'/0/0")
        >>> wallet._p2pkh_address()
        "184xW5gWDnhS7LriL2JAZs1XGTJjimz7pq"
        """
        return self._p2pkh_address()

    def bech32_address(self) -> str:
        """
        Get Pay to Witness Public Key Hash (P2WPKH) address.

        :returns: str -- P2WPKH address.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="venture fitness paper little blush april rigid where find volcano fetch crack label polar dash", passphrase="password")
        >>> wallet.from_path(path="m/44'/0'/0'/0/0")
        >>> wallet._p2wpkh_address()
        "bc1qfky82ek5pr07t65qjretw9hevw2j8j5fdrn5hc"
        """
        return self._p2wpkh_address()

    def _p2pkh_address(self) -> str:
        """
        Get Pay to Public Key Hash (P2PKH) address.

        :returns: str -- P2PKH address.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="venture fitness paper little blush april rigid where find volcano fetch crack label polar dash", passphrase="password")
        >>> wallet.from_path(path="m/44'/0'/0'/0/0")
        >>> wallet._p2pkh_address()
        "184xW5gWDnhS7LriL2JAZs1XGTJjimz7pq"
        """

        compressed_public_key = unhexlify(self.compressed())
        public_key_hash = ripemd160(sha256(compressed_public_key).digest())
        network_hash160_bytes = _unhexlify(self._cryptocurrency.PUBLIC_KEY_ADDRESS) + public_key_hash
        return ensure_string(base58.b58encode_check(network_hash160_bytes))

    def _p2sh_address(self) -> str:
        """
        Get Pay to Script Hash (P2SH) address.

        :returns: str -- P2SH address.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="venture fitness paper little blush april rigid where find volcano fetch crack label polar dash", passphrase="password")
        >>> wallet.from_path(path="m/44'/0'/0'/0/0")
        >>> wallet._p2sh_address()
        "3Jp6ad4ErhibQmhSRfavbPRiUyg2xTTT4j"
        """

        compressed_public_key = unhexlify(self.compressed())
        public_key_hash = hexlify(ripemd160(sha256(compressed_public_key).digest())).decode("utf-8")
        public_key_hash_script = unhexlify("76a914" + public_key_hash + "88ac")
        script_hash = ripemd160(sha256(public_key_hash_script).digest())
        network_hash160_bytes = _unhexlify(self._cryptocurrency.SCRIPT_ADDRESS) + script_hash
        return ensure_string(base58.b58encode_check(network_hash160_bytes))

    def _p2wpkh_address(self) -> Optional[str]:
        """
        Get Pay to Witness Public Key Hash (P2WPKH) address.

        :returns: str -- P2WPKH address.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="venture fitness paper little blush april rigid where find volcano fetch crack label polar dash", passphrase="password")
        >>> wallet.from_path(path="m/44'/0'/0'/0/0")
        >>> wallet._p2wpkh_address()
        "bc1qfky82ek5pr07t65qjretw9hevw2j8j5fdrn5hc"
        """

        compressed_public_key = unhexlify(self.compressed())
        public_key_hash = ripemd160(sha256(compressed_public_key).digest())
        if self._cryptocurrency.SEGWIT_ADDRESS.HRP is None:
            return None
        return ensure_string(encode(self._cryptocurrency.SEGWIT_ADDRESS.HRP, 0, public_key_hash))

    def _p2wpkh_in_p2sh_address(self) -> Optional[str]:
        """
        Get P2WPKH nested in P2SH address.

        :returns: str -- P2WPKH nested in P2SH address.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="venture fitness paper little blush april rigid where find volcano fetch crack label polar dash", passphrase="password")
        >>> wallet.from_path(path="m/44'/0'/0'/0/0")
        >>> wallet._p2wpkh_in_p2sh_address()
        "3CCrxPrHNa6ePbnB7qjh7S3vaPx9qiLc3e"
        """

        compressed_public_key = unhexlify(self.compressed())
        public_key_hash = hexlify(ripemd160(sha256(compressed_public_key).digest())).decode("utf-8")
        script_hash = ripemd160(sha256(unhexlify("0014" + public_key_hash)).digest())
        network_hash160_bytes = _unhexlify(self._cryptocurrency.SCRIPT_ADDRESS) + script_hash
        if self._cryptocurrency.SEGWIT_ADDRESS.HRP is None:
            return None
        return ensure_string(base58.b58encode_check(network_hash160_bytes))

    def _p2wsh_address(self) -> Optional[str]:
        """
        Get Pay to Witness Script Hash (P2WSH) address.

        :returns: str -- P2WSH address.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="venture fitness paper little blush april rigid where find volcano fetch crack label polar dash", passphrase="password")
        >>> wallet.from_path(path="m/44'/0'/0'/0/0")
        >>> wallet._p2wsh_address()
        "bc1qaj2xa9j6eegcxls3y8p6erw6vdgdxynasrd4hl3xuctht5edu3msdeshgf"
        """

        compressed_public_key = unhexlify("5121" + self.compressed() + "51ae")
        script_hash = sha256(compressed_public_key).digest()
        if self._cryptocurrency.SEGWIT_ADDRESS.HRP is None:
            return None
        return ensure_string(encode(self._cryptocurrency.SEGWIT_ADDRESS.HRP, 0, script_hash))

    def _p2wsh_in_p2sh_address(self) -> Optional[str]:
        """
        Get P2WSH nested in P2SH address.

        :returns: str -- P2WSH nested in P2SH address.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="venture fitness paper little blush april rigid where find volcano fetch crack label polar dash", passphrase="password")
        >>> wallet.from_path(path="m/44'/0'/0'/0/0")
        >>> wallet._p2wsh_in_p2sh_address()
        "38YMonfh2yLFRViLrM2kdvZx8ctcp1vbbV"
        """

        compressed_public_key = unhexlify("5121" + self.compressed() + "51ae")
        script_hash = unhexlify("0020" + sha256(compressed_public_key).hexdigest())
        script_hash = ripemd160(sha256(script_hash).digest())
        network_hash160_bytes = _unhexlify(self._cryptocurrency.SCRIPT_ADDRESS) + script_hash
        if self._cryptocurrency.SEGWIT_ADDRESS.HRP is None:
            return None
        return ensure_string(base58.b58encode_check(network_hash160_bytes))

    def wif(self) -> Optional[str]:
        """
        Get Wallet Important Format.

        :returns: str -- Wallet Important Format.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="venture fitness paper little blush april rigid where find volcano fetch crack label polar dash", passphrase="password")
        >>> wallet.from_path(path="m/44'/0'/0'/0/0")
        >>> wallet.wif()
        "KzsHWUJsrTWUUhBGPfMMxLLydiH7NhEn6z7mKHXD5qNkUWaC4TEn"
        """

        return check_encode(_unhexlify(self._cryptocurrency.WIF_SECRET_KEY) + self._key.to_string() + b"\x01") if self._key else None

    def dumps(self) -> dict:
        """
        Get All HDWallet imformations.

        :returns: dict -- All HDWallet imformations.

        >>> from defichain import Wallet
        >>> from defichain.networks import DefichainMainnet
        >>> wallet = Wallet(cryptocurrency=DefichainMainnet)
        >>> wallet.from_mnemonic(mnemonic="venture fitness paper little blush april rigid where find volcano fetch crack label polar dash", passphrase="password")
        >>> wallet.from_path(path="m/44'/0'/0'/0/0")
        >>> wallet.dumps()
        {'cryptocurrency': 'Bitcoin', 'symbol': 'BTC', 'network': 'mainnet', 'strength': 160, 'entropy': 'f24afe7fc1418815ee7fd256beb55518e7c34ecd', 'mnemonic': 'venture fitness paper little blush april rigid where find volcano fetch crack label polar dash', 'language': 'english', 'passphrase': None, 'seed': '8d5f4fe5b81a6a6a18b08603b6b3f59df9f4bbb25d10c55d23e0cbdc5ee385e5fddad9d7e6114f11afdec45928328081f9a598151a7613dc5f5a0c16a4612aa4', 'root_xprivate_key': 'xprv9s21ZrQH143K3xPGUzpogJeKtRdjHkK6muBJo8v7rEVRzT83xJgNcLpMoJXUf9wJFKfuHR4SGvfgdShh4t9VmjjrE9usBunK3LfNna31LGF', 'root_xpublic_key': 'xpub661MyMwAqRbcGSTjb2Mp3Sb4STUDhD2x986ubXKjQa2QsFTCVqzdA98qeZjcncHT1AaZcMSjiP1HJ16jH97q72RwyFfiNhmG8zQ6KBB5PaQ', 'xprivate_key': 'xprvA3BYGWQ9FmhyaNRRXB2f1LphNPnaY9T6gngw4BaTbkFtscSH4RCuJhgWUSKs9S6ciGioHd4TX4UeyUg53MkfN9Xh38xkS1j2Wb9YKsYpJHQ', 'xpublic_key': 'xpub6GAtg1w369GGnrVtdCZfNUmRvRd4wcAx41cXrZz5A5nskQmRbxX9rVzzKiRU4JruirBrfm4KQXNSU7GfqL1tzZWpZYe9Zo4xKGJYohWoQe7', 'uncompressed': 'f93f58b97c3bb616645c3dda256ec946d87c45baf531984c022dd0fd1503b0a875f63285a539213ac241fc4a88e7137ba1c8d897b1c1e5efb81bfc6b45a22d40', 'compressed': '02f93f58b97c3bb616645c3dda256ec946d87c45baf531984c022dd0fd1503b0a8', 'chain_code': 'ed45793b944d1f22522f2d6f48c487029fae2cfcd999ed23087a148bcdda6314', 'private_key': '6cd78b0d69eab1a47bfa53a52b9d8c4331e858b5d7a599270a95d9735fdb0b94', 'public_key': '02f93f58b97c3bb616645c3dda256ec946d87c45baf531984c022dd0fd1503b0a8', 'wif': 'KzsHWUJsrTWUUhBGPfMMxLLydiH7NhEn6z7mKHXD5qNkUWaC4TEn', 'identifier': '4d887566d408dfe5ea8090f2b716f9639523ca89', 'finger_print': '4d887566', 'path': "m/44'/0'/0'/0/0", 'addresses': {'p2pkh': '184xW5gWDnhS7LriL2JAZs1XGTJjimz7pq', 'p2sh': '3Jp6ad4ErhibQmhSRfavbPRiUyg2xTTT4j', 'p2wpkh': 'bc1qfky82ek5pr07t65qjretw9hevw2j8j5fdrn5hc', 'p2wpkh_in_p2sh': '3CCrxPrHNa6ePbnB7qjh7S3vaPx9qiLc3e', 'p2wsh': 'bc1qaj2xa9j6eegcxls3y8p6erw6vdgdxynasrd4hl3xuctht5edu3msdeshgf', 'p2wsh_in_p2sh': '38YMonfh2yLFRViLrM2kdvZx8ctcp1vbbV'}}
        """

        return dict(
            cryptocurrency=self.cryptocurrency(),
            symbol=self.symbol(),
            network=self.network(),
            strength=self.strength(),
            entropy=self.entropy(),
            mnemonic=self.mnemonic(),
            language=self.language(),
            passphrase=self.passphrase(),
            seed=self.seed(),
            root_xprivate_key=self.root_xprivate_key(),
            # root_xprivate_key_hex=self.root_xprivate_key(encoded=False),
            root_xpublic_key=self.root_xpublic_key(),
            # root_xpublic_key_hex=self.root_xpublic_key(encoded=False),
            xprivate_key=self.xprivate_key(),
            # xprivate_key_hex=self.xprivate_key(encoded=False),
            xpublic_key=self.xpublic_key(),
            # xpublic_key_hex=self.xpublic_key(encoded=False),
            uncompressed=self.uncompressed(),
            compressed=self.compressed(),
            chain_code=self.chain_code(),
            private_key=self.private_key(),
            public_key=self.public_key(),
            wif=self.wif(),
            finger_print=self.finger_print(),
            semantic=self.semantic(),
            path=self.path(),
            hash=self.hash(),
            addresses=dict(
                p2pkh=self._p2pkh_address(),
                p2wpkh=self._p2wpkh_address(),
                p2wpkh_in_p2sh=self._p2wpkh_in_p2sh_address()
            )
        )
