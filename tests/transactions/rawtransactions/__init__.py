import copy
from defichain.networks import DefichainMainnet
from defichain import Wallet
from defichain.transactions.utils import Converter
from defichain.transactions.rawtransactions import Transaction, TxP2PKHInput, TxP2WPKHInput, TxP2SHInput
from defichain.transactions.rawtransactions import TxAddressOutput, TxDataOutput, TxDefiOutput
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

    P2PKH_Input = TxP2PKHInput(TXID, VOUT, Addresses.P2PKH, VALUE)
    P2PKH_Input_Serialized = "061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc3d0100000000ffffffff"
    P2SH_Input = TxP2SHInput(TXID, VOUT, Addresses.P2WPKH, VALUE)
    P2SH_Input_Serialized = "061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc3d0100000017160014ad56321" \
                            "e69b7e2d30aeca9f49979ffc53084296fffffffff"
    P2WPKH_Input = TxP2WPKHInput(TXID, VOUT, Addresses.P2WPKH, VALUE)
    P2WPKH_Input_Serialized = "061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc3d0100000000ffffffff"


class TestOutputs:
    VALUE: int = 500
    DATA: str = "#ROADTO50"
    Data_Output: TxDataOutput = TxDataOutput(DATA)
    Data_Output_Serialized: str = "00000000000000000b6a0923524f4144544f353000"

    DefiTx = UtxosToAccount(Addresses.P2WPKH, 1)
    DefiTx_Serialized: str = "6a2a446654785501160014514de706674ff0044303cd4c9920252ec21c6fbc01000000000100000000000000"  # UtxoToAccount DefiTx
    DefiTx_Output: TxDefiOutput = TxDefiOutput(1, DefiTx)
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


class TestTx:
    inputs = [TestInputs.P2PKH_Input, TestInputs.P2SH_Input, TestInputs.P2WPKH_Input]
    outputs = [TestOutputs.P2PKH_Address_Output, TestOutputs.P2SH_Address_Output, TestOutputs.P2WPKH_Address_Output]
    specialOutputs = [TestOutputs.Data_Output, TestOutputs.DefiTx_Output]

    tx_unsigned = [Transaction([TestInputs.P2PKH_Input], [TestOutputs.P2PKH_Address_Output]),
                   Transaction([TestInputs.P2SH_Input], [TestOutputs.P2SH_Address_Output]),
                   Transaction([TestInputs.P2WPKH_Input], [TestOutputs.P2WPKH_Address_Output]),
                   Transaction([TestInputs.P2PKH_Input, TestInputs.P2SH_Input, TestInputs.P2WPKH_Input],
                               [TestOutputs.P2PKH_Address_Output, TestOutputs.P2SH_Address_Output,
                                TestOutputs.P2WPKH_Address_Output]),
                   Transaction([TestInputs.P2PKH_Input, TestInputs.P2SH_Input, TestInputs.P2WPKH_Input],
                               [TestOutputs.P2PKH_Address_Output, TestOutputs.P2SH_Address_Output,
                                TestOutputs.P2WPKH_Address_Output]),
                   Transaction([TestInputs.P2PKH_Input, TestInputs.P2SH_Input, TestInputs.P2WPKH_Input],
                               [TestOutputs.DefiTx_Output, TestOutputs.P2PKH_Address_Output,
                                TestOutputs.P2SH_Address_Output, TestOutputs.P2WPKH_Address_Output]),
                   Transaction([TestInputs.P2PKH_Input, TestInputs.P2SH_Input, TestInputs.P2WPKH_Input],
                               [TestOutputs.Data_Output, TestOutputs.P2PKH_Address_Output,
                                TestOutputs.P2SH_Address_Output, TestOutputs.P2WPKH_Address_Output])
                   ]
    serialized_unsigned = ['0400000001061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc3d0100000000fffffff'
                           'f01f4010000000000001976a914ad56321e69b7e2d30aeca9f49979ffc53084296f88ac0000000000',
                           '0400000001061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc3d0100000017160014a'
                           'd56321e69b7e2d30aeca9f49979ffc53084296fffffffff01f40100000000000017a91493a457d0e4cc789beb65'
                           'eb77742d35297652dafe870000000000',
                           '0400000001061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc3d0100000000fffffff'
                           'f01f401000000000000160014ad56321e69b7e2d30aeca9f49979ffc53084296f0000000000',
                           '0400000003061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc3d0100000000fffffff'
                           'f061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc3d0100000017160014ad56321e69'
                           'b7e2d30aeca9f49979ffc53084296fffffffff061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e2'
                           '3d398fcbc3d0100000000ffffffff03f4010000000000001976a914ad56321e69b7e2d30aeca9f49979ffc53084'
                           '296f88ac00f40100000000000017a91493a457d0e4cc789beb65eb77742d35297652dafe8700f40100000000000'
                           '0160014ad56321e69b7e2d30aeca9f49979ffc53084296f0000000000',
                           '0400000003061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc3d0100000000fffffff'
                           'f061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc3d0100000017160014ad56321e69'
                           'b7e2d30aeca9f49979ffc53084296fffffffff061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e2'
                           '3d398fcbc3d0100000000ffffffff03f4010000000000001976a914ad56321e69b7e2d30aeca9f49979ffc53084'
                           '296f88ac00f40100000000000017a91493a457d0e4cc789beb65eb77742d35297652dafe8700f40100000000000'
                           '0160014ad56321e69b7e2d30aeca9f49979ffc53084296f0000000000',
                           '0400000003061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc3d0100000000fffffff'
                           'f061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc3d0100000017160014ad56321e69'
                           'b7e2d30aeca9f49979ffc53084296fffffffff061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e2'
                           '3d398fcbc3d0100000000ffffffff0401000000000000002c6a2a446654785501160014ad56321e69b7e2d30aec'
                           'a9f49979ffc53084296f0100000000010000000000000000f4010000000000001976a914ad56321e69b7e2d30ae'
                           'ca9f49979ffc53084296f88ac00f40100000000000017a91493a457d0e4cc789beb65eb77742d35297652dafe87'
                           '00f401000000000000160014ad56321e69b7e2d30aeca9f49979ffc53084296f0000000000',
                           '0400000003061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc3d0100000000fffffff'
                           'f061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc3d0100000017160014ad56321e69'
                           'b7e2d30aeca9f49979ffc53084296fffffffff061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e2'
                           '3d398fcbc3d0100000000ffffffff0400000000000000000b6a0923524f4144544f353000f40100000000000019'
                           '76a914ad56321e69b7e2d30aeca9f49979ffc53084296f88ac00f40100000000000017a91493a457d0e4cc789be'
                           'b65eb77742d35297652dafe8700f401000000000000160014ad56321e69b7e2d30aeca9f49979ffc53084296f00'
                           '00000000']

    tx_signed = [tx.sign(DefichainMainnet, [Keys.privateKey]) for tx in copy.deepcopy(tx_unsigned)]

    serialized_signed = ['0400000001061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc3d010000006b483045022'
                         '10088ba38c156954d32fbc2db42443f8f228edd5348975792715062975731250fbf02206f878050d4ccf0065166df'
                         '792a8a13da9fd9d4586b8b3fe4c093e28e557a7621012103f110404297e471ad86d1aabc8a885bd4d1ec71bc3f31b'
                         'ef8ed2ff9ad30324600ffffffff01f4010000000000001976a914ad56321e69b7e2d30aeca9f49979ffc53084296f'
                         '88ac0000000000',
                         '04000000000101061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc3d010000001716001'
                         '4ad56321e69b7e2d30aeca9f49979ffc53084296fffffffff01f40100000000000017a91493a457d0e4cc789beb65'
                         'eb77742d35297652dafe87000247304402206f2caff4365c3c4b0c01258999a804b7e0d1a2fe28bbaf36bc656e9fb'
                         '3571dc5022078ad64f94f1e34eeec18cee48a3686bf05ee92f8500bb7b1aafb38e4f0c16f8f012103f110404297e4'
                         '71ad86d1aabc8a885bd4d1ec71bc3f31bef8ed2ff9ad3032460000000000',
                         '04000000000101061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc3d0100000000fffff'
                         'fff01f401000000000000160014ad56321e69b7e2d30aeca9f49979ffc53084296f000247304402206f2caff4365c'
                         '3c4b0c01258999a804b7e0d1a2fe28bbaf36bc656e9fb3571dc5022078ad64f94f1e34eeec18cee48a3686bf05ee9'
                         '2f8500bb7b1aafb38e4f0c16f8f012103f110404297e471ad86d1aabc8a885bd4d1ec71bc3f31bef8ed2ff9ad3032'
                         '460000000000',
                         '04000000000103061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc3d010000006b48304'
                         '502210088ba38c156954d32fbc2db42443f8f228edd5348975792715062975731250fbf02206f878050d4ccf00651'
                         '66df792a8a13da9fd9d4586b8b3fe4c093e28e557a7621012103f110404297e471ad86d1aabc8a885bd4d1ec71bc3'
                         'f31bef8ed2ff9ad30324600ffffffff061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc'
                         '3d0100000017160014ad56321e69b7e2d30aeca9f49979ffc53084296fffffffff061ca2791086a0df7c4786bbf16'
                         'b933873d47ef0029ea539ce7e23d398fcbc3d0100000000ffffffff03f4010000000000001976a914ad56321e69b7'
                         'e2d30aeca9f49979ffc53084296f88ac00f40100000000000017a91493a457d0e4cc789beb65eb77742d35297652d'
                         'afe8700f401000000000000160014ad56321e69b7e2d30aeca9f49979ffc53084296f00000247304402206f2caff4'
                         '365c3c4b0c01258999a804b7e0d1a2fe28bbaf36bc656e9fb3571dc5022078ad64f94f1e34eeec18cee48a3686bf0'
                         '5ee92f8500bb7b1aafb38e4f0c16f8f012103f110404297e471ad86d1aabc8a885bd4d1ec71bc3f31bef8ed2ff9ad'
                         '303246000247304402206f2caff4365c3c4b0c01258999a804b7e0d1a2fe28bbaf36bc656e9fb3571dc5022078ad6'
                         '4f94f1e34eeec18cee48a3686bf05ee92f8500bb7b1aafb38e4f0c16f8f012103f110404297e471ad86d1aabc8a88'
                         '5bd4d1ec71bc3f31bef8ed2ff9ad3032460000000000',
                         '04000000000103061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc3d010000006b48304'
                         '502210088ba38c156954d32fbc2db42443f8f228edd5348975792715062975731250fbf02206f878050d4ccf00651'
                         '66df792a8a13da9fd9d4586b8b3fe4c093e28e557a7621012103f110404297e471ad86d1aabc8a885bd4d1ec71bc3'
                         'f31bef8ed2ff9ad30324600ffffffff061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc'
                         '3d0100000017160014ad56321e69b7e2d30aeca9f49979ffc53084296fffffffff061ca2791086a0df7c4786bbf16'
                         'b933873d47ef0029ea539ce7e23d398fcbc3d0100000000ffffffff03f4010000000000001976a914ad56321e69b7'
                         'e2d30aeca9f49979ffc53084296f88ac00f40100000000000017a91493a457d0e4cc789beb65eb77742d35297652d'
                         'afe8700f401000000000000160014ad56321e69b7e2d30aeca9f49979ffc53084296f00000247304402206f2caff4'
                         '365c3c4b0c01258999a804b7e0d1a2fe28bbaf36bc656e9fb3571dc5022078ad64f94f1e34eeec18cee48a3686bf0'
                         '5ee92f8500bb7b1aafb38e4f0c16f8f012103f110404297e471ad86d1aabc8a885bd4d1ec71bc3f31bef8ed2ff9ad'
                         '303246000247304402206f2caff4365c3c4b0c01258999a804b7e0d1a2fe28bbaf36bc656e9fb3571dc5022078ad6'
                         '4f94f1e34eeec18cee48a3686bf05ee92f8500bb7b1aafb38e4f0c16f8f012103f110404297e471ad86d1aabc8a88'
                         '5bd4d1ec71bc3f31bef8ed2ff9ad3032460000000000',
                         '04000000000103061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc3d010000006b48304'
                         '502210088ba38c156954d32fbc2db42443f8f228edd5348975792715062975731250fbf02206f878050d4ccf00651'
                         '66df792a8a13da9fd9d4586b8b3fe4c093e28e557a7621012103f110404297e471ad86d1aabc8a885bd4d1ec71bc3'
                         'f31bef8ed2ff9ad30324600ffffffff061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc'
                         '3d0100000017160014ad56321e69b7e2d30aeca9f49979ffc53084296fffffffff061ca2791086a0df7c4786bbf16'
                         'b933873d47ef0029ea539ce7e23d398fcbc3d0100000000ffffffff0401000000000000002c6a2a44665478550116'
                         '0014ad56321e69b7e2d30aeca9f49979ffc53084296f0100000000010000000000000000f4010000000000001976a'
                         '914ad56321e69b7e2d30aeca9f49979ffc53084296f88ac00f40100000000000017a91493a457d0e4cc789beb65eb'
                         '77742d35297652dafe8700f401000000000000160014ad56321e69b7e2d30aeca9f49979ffc53084296f000002473'
                         '04402206f2caff4365c3c4b0c01258999a804b7e0d1a2fe28bbaf36bc656e9fb3571dc5022078ad64f94f1e34eeec'
                         '18cee48a3686bf05ee92f8500bb7b1aafb38e4f0c16f8f012103f110404297e471ad86d1aabc8a885bd4d1ec71bc3'
                         'f31bef8ed2ff9ad303246000247304402206f2caff4365c3c4b0c01258999a804b7e0d1a2fe28bbaf36bc656e9fb3'
                         '571dc5022078ad64f94f1e34eeec18cee48a3686bf05ee92f8500bb7b1aafb38e4f0c16f8f012103f110404297e47'
                         '1ad86d1aabc8a885bd4d1ec71bc3f31bef8ed2ff9ad3032460000000000',
                         '04000000000103061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc3d010000006b48304'
                         '502210088ba38c156954d32fbc2db42443f8f228edd5348975792715062975731250fbf02206f878050d4ccf00651'
                         '66df792a8a13da9fd9d4586b8b3fe4c093e28e557a7621012103f110404297e471ad86d1aabc8a885bd4d1ec71bc3'
                         'f31bef8ed2ff9ad30324600ffffffff061ca2791086a0df7c4786bbf16b933873d47ef0029ea539ce7e23d398fcbc'
                         '3d0100000017160014ad56321e69b7e2d30aeca9f49979ffc53084296fffffffff061ca2791086a0df7c4786bbf16'
                         'b933873d47ef0029ea539ce7e23d398fcbc3d0100000000ffffffff0400000000000000000b6a0923524f4144544f'
                         '353000f4010000000000001976a914ad56321e69b7e2d30aeca9f49979ffc53084296f88ac00f4010000000000001'
                         '7a91493a457d0e4cc789beb65eb77742d35297652dafe8700f401000000000000160014ad56321e69b7e2d30aeca9'
                         'f49979ffc53084296f00000247304402206f2caff4365c3c4b0c01258999a804b7e0d1a2fe28bbaf36bc656e9fb35'
                         '71dc5022078ad64f94f1e34eeec18cee48a3686bf05ee92f8500bb7b1aafb38e4f0c16f8f012103f110404297e471'
                         'ad86d1aabc8a885bd4d1ec71bc3f31bef8ed2ff9ad303246000247304402206f2caff4365c3c4b0c01258999a804b'
                         '7e0d1a2fe28bbaf36bc656e9fb3571dc5022078ad64f94f1e34eeec18cee48a3686bf05ee92f8500bb7b1aafb38e4'
                         'f0c16f8f012103f110404297e471ad86d1aabc8a885bd4d1ec71bc3f31bef8ed2ff9ad3032460000000000']

    fee = [500, 500, 500, 1500, 1500, 1499, 1500]

    txid = ['4568d799658181e80b64f2999aa1c3c11dfcf7acb19af340d16efe9f707d5ec9',
            'f38ab4800a319d5a2f8ce719449af9306460a1ebc94bfca051316fd6e3f1f9a3',
            'fa1f2e39c7140b3863fc7870fb36b4da41b076fde196c157056142ea7718c9af',
            '9f88f4eac4ffefc17243f30f46320b6c968b94ff91e55cb03880b576d903a7b9',
            '9f88f4eac4ffefc17243f30f46320b6c968b94ff91e55cb03880b576d903a7b9',
            '253f8020a94d1cfcbe6d054c7af5bb7e3d263ea1e63135bb0bfcead0d96ab647',
            '4af86bf393f5b205e079e0d6921a919ee47161ccf85fe58b5302ce88dc6d3d27']

    unspent_inputs = ['c95e7d709ffe6ed140f39ab1acf7fc1dc1c3a19a99f2640be881816599d768450000000000ffffffff',
                      'a3f9f1e3d66f3151a0fc4bc9eba1606430f99a4419e78c2f5a9d310a80b48af30000000017160014ad56321e69b7e2d3'
                      '0aeca9f49979ffc53084296fffffffff',
                      'afc91877ea42610557c196e1fd76b041dab436fb7078fc63380b14c7392e1ffa0000000000ffffffff',
                      'b9a703d976b58038b05ce591ff948b966c0b32460ff34372c1efffc4eaf4889f0000000000ffffffff',
                      'b9a703d976b58038b05ce591ff948b966c0b32460ff34372c1efffc4eaf4889f0100000017160014ad56321e69b7e2d3'
                      '0aeca9f49979ffc53084296fffffffff',
                      'b9a703d976b58038b05ce591ff948b966c0b32460ff34372c1efffc4eaf4889f0200000000ffffffff',
                      'b9a703d976b58038b05ce591ff948b966c0b32460ff34372c1efffc4eaf4889f0000000000ffffffff',
                      'b9a703d976b58038b05ce591ff948b966c0b32460ff34372c1efffc4eaf4889f0100000017160014ad56321e69b7e2d3'
                      '0aeca9f49979ffc53084296fffffffff',
                      'b9a703d976b58038b05ce591ff948b966c0b32460ff34372c1efffc4eaf4889f0200000000ffffffff',
                      '47b66ad9d0eafc0bbb3531e6a13e263d7ebbf57a4c056dbefc1c4da920803f250100000000ffffffff',
                      '47b66ad9d0eafc0bbb3531e6a13e263d7ebbf57a4c056dbefc1c4da920803f250200000017160014ad56321e69b7e2d3'
                      '0aeca9f49979ffc53084296fffffffff',
                      '47b66ad9d0eafc0bbb3531e6a13e263d7ebbf57a4c056dbefc1c4da920803f250300000000ffffffff',
                      '273d6ddc88ce02538be55ff8cc6171e49e911a92d6e079e005b2f593f36bf84a0100000000ffffffff',
                      '273d6ddc88ce02538be55ff8cc6171e49e911a92d6e079e005b2f593f36bf84a0200000017160014ad56321e69b7e2d3'
                      '0aeca9f49979ffc53084296fffffffff',
                      '273d6ddc88ce02538be55ff8cc6171e49e911a92d6e079e005b2f593f36bf84a0300000000ffffffff']
