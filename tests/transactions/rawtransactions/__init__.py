from defichain.networks import DefichainMainnet
from defichain.transactions.rawtransactions import Transaction, TxP2WPKHInput, TxP2SHInput, TxAddressOutput


_p2shInput = TxP2SHInput("3dbcfc98d3237ece39a59e02f07ed47338936bf1bb86477cdfa0861079a21c06", 1,
                         "df1q29x7wpn8flcqgscre4xfjgp99mppcmaus83uzt", 1000)

_p2wpkhInput = TxP2WPKHInput("3dbcfc98d3237ece39a59e02f07ed47338936bf1bb86477cdfa0861079a21c06", 1,
                             "df1q29x7wpn8flcqgscre4xfjgp99mppcmaus83uzt", 1000)


_p2wpkhAddressOutput = TxAddressOutput(500, "df1q29x7wpn8flcqgscre4xfjgp99mppcmaus83uzt")


class TestFee:
    P2SH_Input_Tx = Transaction([_p2shInput], [_p2wpkhAddressOutput])
    P2WPKH_Input_Tx = Transaction([_p2wpkhInput], [_p2wpkhAddressOutput])


