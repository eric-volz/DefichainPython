from defichain.networks import DefichainMainnet
from defichain import Wallet
from defichain.transactions.utils import Converter
from defichain.transactions.rawtransactions import Transaction, TxP2PKHInput, TxP2WPKHInput, TxP2SHInput
from defichain.transactions.rawtransactions import TxAddressOutput
from defichain.transactions.defitx import UtxosToAccount


class Keys:
    mnemonic = "zone myth seat market badge hamster puppy worry mind attend heavy churn upgrade heart scan address " \
               "across mix spread add boss armed desert mixed"
    wallet: Wallet = Wallet(DefichainMainnet)
    wallet.from_mnemonic(mnemonic)
    privateKey: str = wallet.private_key()
    wif: str = wallet.wif()


class Addresses:
    P2PKH: str = Keys.wallet.p2pkh_address()
    P2SH: str = Keys.wallet.p2sh_address()
    P2WPKH: str = Keys.wallet.p2wpkh_address()


class TestInputs:
    TXID: str = "3dbcfc98d3237ece39a59e02f07ed47338936bf1bb86477cdfa0861079a21c06"
    VOUT: int = 1
    VALUE: int = 1000

    P2PKH_Input = TxP2PKHInput(TXID, VOUT, Addresses.P2PKH)
    P2PKH_Input_Serialized = "061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc3d0100000000ffffffff"
    P2SH_Input = TxP2SHInput(TXID, VOUT, Addresses.P2WPKH, VALUE)
    P2SH_Input_Serialized = "061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc3d0100000017160014ad56321" \
                            "e69b7e2d30aeca9f49979ffc53084296fffffffff"
    P2WPKH_Input = TxP2WPKHInput(TXID, VOUT, Addresses.P2WPKH, VALUE)
    P2WPKH_Input_Serialized = "061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc3d0100000000ffffffff"


class TestOutputs:
    VALUE: int = 500
    DATA: str = "#ROADTO50"
    Data_Output_Serialized: str = "00000000000000000b6a0923524f4144544f353000"

    DefiTx = UtxosToAccount(Addresses.P2WPKH, 1)
    DefiTx_Serialized: str = "6a2a446654785501160014514de706674ff0044303cd4c9920252ec21c6fbc01000000000100000000000000"  # UtxoToAccount DefiTx
    DefiTx_Output_Serialized: str = "01000000000000002c6a2a446654785501160014ad56321e69b7e2d30aeca9f49979ffc53084296f" \
                                    "0100000000010000000000000000"

    P2PKH_Address_Output = TxAddressOutput(VALUE, Addresses.P2PKH)
    P2PKH_Address_Output_Serialized = "f4010000000000001976a914ad56321e69b7e2d30aeca9f49979ffc53084296f88ac00"
    P2SH_Address_Output = TxAddressOutput(VALUE, Addresses.P2SH)
    P2SH_Address_Output_Serialized = "f40100000000000017a91493a457d0e4cc789beb65eb77742d35297652dafe8700"
    P2WPKH_Address_Output = TxAddressOutput(VALUE, Addresses.P2WPKH)
    P2WPKH_Address_Output_Serialized = "f401000000000000160014ad56321e69b7e2d30aeca9f49979ffc53084296f00"


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


class TestSign:
    Data: str = "#ROADTO50"
    SigHash: int = 1
    DataBytes: bytes = Converter.hex_to_bytes(Converter.str_to_hex(Data))
    SigHashBytes: bytes = Converter.int_to_bytes(SigHash, 4)
    LegacySignature: str = "3045022100e5249785adcb636419f09eee671140dc849d9a1dc66ea53f0d99c638cf43124a0220013527b7da" \
                           "35e20f7810632f9e2e1baae4062ca96fc25fbc94127294d2be9d9e01"
    SegwitSignature: str = "304402200eb225e931074883443b7d02ff85312fd5c323ac7ea22180d88b951ff93b627002200b21bde8faa0" \
                           "8971435b94342d119343c43fadb42163f1f09f95a621f4d89afe01"
