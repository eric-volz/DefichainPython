from typing import Any

from defichain.exceptions.transactions import AddressError
from defichain.transactions.constants import DefiTxType
from defichain.transactions.address import Address
from defichain.transactions.utils import Converter, Token, Calculate
from ..builddefitx import BuildDefiTx
from .baseinput import TokenBalanceInt32
from .basedefitx import BaseDefiTx


class SetLoanScheme(BaseDefiTx):
    pass


class DestroyLoanScheme(BaseDefiTx):
    pass


class SetDefaultLoanScheme(BaseDefiTx):
    pass


class SetCollateralToken(BaseDefiTx):
    pass


class SetLoanToken(BaseDefiTx):
    pass


class UpdateLoanToken(BaseDefiTx):
    pass


class TakeLoan(BaseDefiTx):
    """
    Builds the defi transaction: Take Loan

    :param vaultId: (required) id of vault used for loan
    :type vaultId: str
    :param addressTo: (required) address to transfer tokens
    :type addressTo: str
    :param amounts: (required) AddressAmount
    :type amounts: str | [str]
    """

    @staticmethod
    def deserialize(network: Any, hex: str) -> "TakeLoan":
        position = 0

        vaultId = Converter.bytes_to_hex(bytes(reversed(Converter.hex_to_bytes(hex[position: position + 64]))))
        position += 64

        lenghtAddressTo = Converter.hex_to_int(hex[position: position + 2]) * 2
        position += 2

        addressTo = Address.from_scriptPublicKey(network, hex[position: position + lenghtAddressTo])
        position += lenghtAddressTo

        numberOfAmounts = Converter.hex_to_int(hex[position: position + 2])
        position += 2

        tokenBalances = []
        for _ in range(numberOfAmounts):
            tokenId = Converter.hex_to_int(hex[position: position + 8])
            position += 8
            amount = Converter.hex_to_int(hex[position: position + 16])
            position += 16
            tokenBalance = TokenBalanceInt32(tokenId, amount)
            tokenBalances.append(f"{tokenBalance.get_amount()}@{tokenBalance.get_tokenId()}")

        return TakeLoan(vaultId, addressTo.get_address(), tokenBalances)

    def __init__(self, vaultId: str, addressTo: str, amounts: "str | [str]"):
        self._vaultId, self._addressTo, self._amounts = None, None, None
        self._network = None
        self.set_vaultId(vaultId)
        self.set_addressTo(addressTo)
        self.set_amounts(amounts)

    def __bytes__(self) -> bytes:
        # Convert to Bytes
        defiTxType = Converter.hex_to_bytes(self.get_defiTxType())
        vaultId = bytes(reversed(Converter.hex_to_bytes(self.get_vaultId())))
        addressTo = Converter.hex_to_bytes(Address.from_address(self.get_addressTo()).get_scriptPublicKey())

        tokenAmounts = []
        for amount in self.get_amounts():
            amountSplit = amount.split("@")
            tokenAmounts.append(TokenBalanceInt32(int(amountSplit[1]), int(amountSplit[0])).bytes())

        lengthAddressTo = Converter.int_to_bytes(len(addressTo), 1)
        numberOfAmounts = Converter.hex_to_bytes(Calculate.write_varInt(len(self.get_amounts())))

        # Build DepositToVaultDefiTx
        result = defiTxType
        result += vaultId
        result += lengthAddressTo
        result += addressTo
        result += numberOfAmounts
        for amount in tokenAmounts:
            result += amount

        return BuildDefiTx.build_defiTx(result)

    def to_json(self) -> {}:
        json = {}
        json.update({"defiTxType": {"typeName": DefiTxType.from_hex(self.get_defiTxType()),
                                    "typeHex": self.get_defiTxType()}})
        json.update({"vaultId": self.get_vaultId()})
        json.update({"addressTo": self.get_addressTo()})
        json.update({"amounts": self.get_amounts()})
        return json

    # Get Information
    def get_defiTxType(self) -> str:
        return DefiTxType.OP_DEFI_TX_TAKE_LOAN

    def get_vaultId(self) -> str:
        return self._vaultId

    def get_addressTo(self) -> str:
        return self._addressTo

    def get_amounts(self) -> str:
        return self._amounts

    # Set Information
    def set_vaultId(self, vaultId: str) -> None:
        self._vaultId = vaultId

    def set_addressTo(self, addressTo: str) -> None:
        address = Address.from_address(addressTo)
        self._network = address.get_network()
        self._addressTo = addressTo

    def set_amounts(self, amounts: str) -> None:
        if not isinstance(amounts, list):
            amounts = [amounts]
        self._amounts = []
        for amount in amounts:
            self._amounts.append(f'{amount.split("@")[0]}@{Token.checkAndConvert(self._network, amount.split("@")[1])}')


class PaybackLoan(BaseDefiTx):
    """TODO: MVP"""
    pass


class PaybackLoanV2(BaseDefiTx):
    pass