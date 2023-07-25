import pytest

from defichain.networks import DefichainMainnet
from defichain.transactions.defitx import DefiTx, UtxosToAccount, AccountToUtxos, AccountToAccount, AnyAccountToAccount, \
    SetFutureSwap

from . import Addresses, TestAccounts


@pytest.mark.transactions
def test_utxo_to_account():  # 01
    utxo_to_account_p2pkh: UtxosToAccount = UtxosToAccount(address=Addresses.P2PKH, amount=TestAccounts.value,
                                                           tokenId=TestAccounts.tokenId)
    utxo_to_account_p2sh: UtxosToAccount = UtxosToAccount(address=Addresses.P2SH, amount=TestAccounts.value,
                                                          tokenId=TestAccounts.tokenId)
    utxo_to_account_p2wpkh: UtxosToAccount = UtxosToAccount(address=Addresses.P2WPKH, amount=TestAccounts.value,
                                                            tokenId=TestAccounts.tokenId)

    assert utxo_to_account_p2pkh.serialize() == TestAccounts.utxo_to_account_p2pkh_serialized
    assert utxo_to_account_p2sh.serialize() == TestAccounts.utxo_to_account_p2sh_serialized
    assert utxo_to_account_p2wpkh.serialize() == TestAccounts.utxo_to_account_p2wpkh_serialized

    assert DefiTx.deserialize(DefichainMainnet, TestAccounts.utxo_to_account_p2pkh_serialized).serialize() == \
           TestAccounts.utxo_to_account_p2pkh_serialized
    assert DefiTx.deserialize(DefichainMainnet, TestAccounts.utxo_to_account_p2sh_serialized).serialize() == \
           TestAccounts.utxo_to_account_p2sh_serialized
    assert DefiTx.deserialize(DefichainMainnet, TestAccounts.utxo_to_account_p2wpkh_serialized).serialize() == \
           TestAccounts.utxo_to_account_p2wpkh_serialized


@pytest.mark.transactions
def test_account_to_utxo():  # 02
    account_to_utxo_p2pkh: AccountToUtxos = AccountToUtxos(addressFrom=Addresses.P2PKH, value=TestAccounts.value,
                                                           mintingOutputsStart=TestAccounts.mintingOutputsStart)
    account_to_utxo_p2sh: AccountToUtxos = AccountToUtxos(addressFrom=Addresses.P2SH, value=TestAccounts.value,
                                                          mintingOutputsStart=TestAccounts.mintingOutputsStart)
    account_to_utxo_p2wpkh: AccountToUtxos = AccountToUtxos(addressFrom=Addresses.P2WPKH, value=TestAccounts.value,
                                                            mintingOutputsStart=TestAccounts.mintingOutputsStart)

    assert account_to_utxo_p2pkh.serialize() == TestAccounts.account_to_utxo_p2pkh_serialized
    assert account_to_utxo_p2sh.serialize() == TestAccounts.account_to_utxo_p2sh_serialized
    assert account_to_utxo_p2wpkh.serialize() == TestAccounts.account_to_utxo_p2wpkh_serialized

    assert DefiTx.deserialize(DefichainMainnet, TestAccounts.account_to_utxo_p2pkh_serialized).serialize() == \
           TestAccounts.account_to_utxo_p2pkh_serialized
    assert DefiTx.deserialize(DefichainMainnet, TestAccounts.account_to_utxo_p2sh_serialized).serialize() == \
           TestAccounts.account_to_utxo_p2sh_serialized
    assert DefiTx.deserialize(DefichainMainnet, TestAccounts.account_to_utxo_p2wpkh_serialized).serialize() == \
           TestAccounts.account_to_utxo_p2wpkh_serialized


@pytest.mark.transactions
def test_account_to_account():  # 03
    account_to_account_p2pkh: AccountToAccount = AccountToAccount(addressFrom=Addresses.P2PKH,
                                                                  addressAmountTo=TestAccounts.addressAmounts)
    account_to_account_p2sh: AccountToAccount = AccountToAccount(addressFrom=Addresses.P2SH,
                                                                 addressAmountTo=TestAccounts.addressAmounts)
    account_to_account_p2wpkh: AccountToAccount = AccountToAccount(addressFrom=Addresses.P2WPKH,
                                                                   addressAmountTo=TestAccounts.addressAmounts)

    assert account_to_account_p2pkh.serialize() == TestAccounts.account_to_account_p2pkh_serialized
    assert account_to_account_p2sh.serialize() == TestAccounts.account_to_account_p2sh_serialized
    assert account_to_account_p2wpkh.serialize() == TestAccounts.account_to_account_p2wpkh_serialized

    assert DefiTx.deserialize(DefichainMainnet, TestAccounts.account_to_account_p2pkh_serialized).serialize() == \
           TestAccounts.account_to_account_p2pkh_serialized
    assert DefiTx.deserialize(DefichainMainnet, TestAccounts.account_to_account_p2sh_serialized).serialize() == \
           TestAccounts.account_to_account_p2sh_serialized
    assert DefiTx.deserialize(DefichainMainnet, TestAccounts.account_to_account_p2wpkh_serialized).serialize() == \
           TestAccounts.account_to_account_p2wpkh_serialized
