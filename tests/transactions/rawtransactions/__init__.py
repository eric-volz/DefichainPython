from defichain.networks import DefichainMainnet
from defichain.transactions.rawtransactions import Transaction, TxP2PKHInput, TxP2WPKHInput, TxP2SHInput
from defichain.transactions.rawtransactions import TxOutput, TxAddressOutput, TxDataOutput, TxDefiOutput
from defichain.transactions.defitx import UtxosToAccount
from defichain.transactions.rawtransactions import estimate_fee


class Addresses:
    P2PKH: str = "8P2Y9mePZEWDFZje5azzrdEcCfaHYXQf9g"
    P2SH: str = "dKjQW9MaCCswbWnuSGXrjWGT5Mhd7bW5eF"
    P2WPKH: str = "df1q29x7wpn8flcqgscre4xfjgp99mppcmaus83uzt"


class TestInputs:
    TXID: str = "3dbcfc98d3237ece39a59e02f07ed47338936bf1bb86477cdfa0861079a21c06"
    VOUT: int = 1
    VALUE: int = 1000

    P2PKH_Input = TxP2PKHInput(TXID, VOUT, Addresses.P2PKH)
    P2PKH_Input_Serialized = "061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc3d0100000000ffffffff"
    P2SH_Input = TxP2SHInput(TXID, VOUT, Addresses.P2WPKH, VALUE)
    P2SH_Input_Serialized = "061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc3d0100000017160014514de706" \
                            "674ff0044303cd4c9920252ec21c6fbcffffffff"
    P2WPKH_Input = TxP2WPKHInput(TXID, VOUT, Addresses.P2WPKH, VALUE)
    P2WPKH_Input_Serialized = "061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc3d0100000000ffffffff"



_p2wpkhAddressOutput = TxAddressOutput(500, "df1q29x7wpn8flcqgscre4xfjgp99mppcmaus83uzt")


class TestFee:
    P2PKH_Input_Tx = Transaction([TestInputs.P2PKH_Input], [TestOutputs.P2WPKH_Address_Output])
    P2SH_Input_Tx = Transaction([TestInputs.P2SH_Input], [TestOutputs.P2WPKH_Address_Output])
    P2WPKH_Input_Tx = Transaction([TestInputs.P2WPKH_Input], [TestOutputs.P2WPKH_Address_Output])

    P2PKH_and_P2SH_Input_Tx = Transaction([TestInputs.P2PKH_Input, TestInputs.P2SH_Input],
                                          [TestOutputs.P2WPKH_Address_Output])
    P2PKH_and_P2WPKH_Input_Tx = Transaction([TestInputs.P2PKH_Input, TestInputs.P2WPKH_Input],
                                            [TestOutputs.P2WPKH_Address_Output])
    P2SH_and_P2WPKH_Input_Tx = Transaction([TestInputs.P2SH_Input, TestInputs.P2WPKH_Input],
                                           [TestOutputs.P2WPKH_Address_Output])

    P2PKH_and_P2SH_and_P2WPKH_Input_Tx = Transaction([TestInputs.P2PKH_Input, TestInputs.P2SH_Input,
                                                      TestInputs.P2WPKH_Input], [TestOutputs.P2WPKH_Address_Output])
