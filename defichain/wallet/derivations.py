from typing import (
    Tuple, Optional
)

from defichain.exceptions.wallet.DerivationError import DerivationError

HARDENED: Tuple[str, str] = ("'", "")


class Derivation:
    """
    Hierarchical Deterministic Wallet Derivation's

    :param path: Derivation path.
    :type path: str
    :param semantic: Extended semantic, defaults to ``P2PKH``.
    :type semantic: str

    :returns: Derivation -- Derivation instance.

    >>> from defichain.wallet import Derivation
    >>> Derivation()
    <hdwallet.derivations.Derivation object at 0x000001EBC58E9F70>
    >>> str(Derivation())
    "\0\0\0\0"
    >>> str(Derivation(path="m/44'/0'/0'/0/0", semantic="p2pkh"))
    "m/44'/0'/0'/0/0"

    .. note::
        Do not forget all derivation paths are start swith 'm/' prefix.
    """

    PATH: str = "\0\0\0\0"
    SEMANTIC: str = "p2pkh"

    def __str__(self) -> str:
        return self.PATH

    def __init__(self, path: Optional[str] = None, semantic: str = "p2pkh"):

        if path:
            if not isinstance(path, str):
                raise DerivationError("Bad derivation path, Please import only str type!")
            elif path[0:2] != "m/":
                raise DerivationError("Bad path, please insert like this str type of \"m/0'/0\" path!")

            self.PATH = "m"
            for index in path.lstrip("m/").split("/"):
                self.PATH += f"/{int(index[:-1])}'" if "'" in index else f"/{int(index)}"

        self.SEMANTIC = semantic

    @classmethod
    def from_path(cls, path: str) -> "Derivation":
        """
        Derivation from path.

        :param path: Derivation path.
        :type path: str, Derivation

        :returns: Derivation -- Derivation instance.

        >>> from defichain.wallet import Derivation
        >>> derivation = Derivation()
        >>> derivation.from_path(path="m/44'/0'/'0/0/0")
        <hdwallet.derivation.Derivation object at 0x000001E8BFB98D60>
        """

        if not isinstance(path, str):
            raise DerivationError("Bad derivation path, Please import only str type!")
        if path[0:2] != "m/":
            raise DerivationError("Bad path, please insert like this str type of \"m/0'/0\" path!")

        new_path = "m"
        for index in path.lstrip("m/").split("/"):
            new_path += f"/{int(index[:-1])}'" if "'" in index else f"/{int(index)}"

        return Derivation(path=new_path)

    def from_index(self, index: int, hardened: bool = False) -> "Derivation":
        """
        Derivation from path.

        :param index: Derivation index.
        :type index: int
        :param hardened: Hardened address, default to ``False``.
        :type hardened: bool

        :returns: Derivation -- Derivation instance.

        >>> from defichain.wallet import Derivation
        >>> derivation = Derivation()
        >>> derivation.from_index(index=44, hardened=True)
        >>> derivation.from_index(index=0, hardened=True)
        >>> derivation.from_index(index=0, hardened=True)
        >>> derivation.from_index(index=0)
        >>> derivation.from_index(index=0)
        <hdwallet.derivation.Derivation object at 0x000001E8BFB98D60>
        """

        if not isinstance(index, int):
            raise DerivationError("Bad derivation index, Please import only int type!")

        if self.PATH == "\0\0\0\0":
            self.PATH = ""
        self.PATH += (
            (f"/{index}'" if hardened else f"/{index}")
            if self.PATH.startswith("m/") else
            (f"m/{index}'" if hardened else f"m/{index}")
        )
        return self

    def clean_derivation(self) -> "Derivation":
        """
        Clean derivation path or indexes.

        :returns: Derivation -- Derivation instance.

        >>> from defichain.wallet import Derivation
        >>> derivation = Derivation()
        >>> derivation.from_path(path="m/44'/0'/'0/0/0")
        >>> str(derivation)
        "m/44'/0'/'0/0/0"
        >>> derivation.clean_derivation()
        <hdwallet.wallet.HDWallet object at 0x000001E8BFB98D60>
        >>> str(derivation)
        "\0\0\0\0"
        """

        self.PATH = "\0\0\0\0"
        return self
