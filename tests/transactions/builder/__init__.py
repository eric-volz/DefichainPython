from defichain import Wallet, Ocean, TxBuilder
from defichain.networks import DefichainMainnet
from defichain.transactions.rawtransactions import Transaction
from defichain.transactions.utils import BuildAddressAmounts, Converter


class Keys:
    mnemonic = "zone myth seat market badge hamster puppy worry mind attend heavy churn upgrade heart scan address " \
               "across mix spread add boss armed desert mixed"
    wallet: Wallet = Wallet(DefichainMainnet)
    wallet.from_mnemonic(mnemonic)
    account = wallet.get_account(0)
    privateKey: str = wallet.private_key()
    wif: str = wallet.wif()


class Addresses:
    P2PKH: str = Keys.wallet.p2pkh_address()
    P2SH: str = Keys.wallet.p2sh_address()
    P2WPKH: str = Keys.wallet.p2wpkh_address()


ocean = Ocean()
builder_p2pkh = TxBuilder(Keys.account.get_p2pkh(), Keys.account, ocean)
builder_p2sh = TxBuilder(Keys.account.get_p2sh(), Keys.account, ocean)
builder_p2wpkh = TxBuilder(Keys.account.get_p2wpkh(), Keys.account, ocean)


class TestAccounts:
    pass


class TestData:
    string = "Hello DeFighters"
    hex = Converter.str_to_hex(string)

    addressAmountTo = BuildAddressAmounts()
    addressAmountTo.add(builder_p2pkh.get_address(), "DFI", 0.000001)
    addressAmountTo.add(builder_p2sh.get_address(), "DFI", 0.000001)
    addressAmountTo.add(builder_p2wpkh.get_address(), "DFI", 0.000001)

    hex_serialized = "0400000000010149b8ea9b2b0224e44126b86bd1e2889a7dac0ec06fcfb0dc4dd13782e1c84fce0100000000fffffff" \
                     "f050000000000000000226a203438363536633663366632303434363534363639363736383734363537323733006400" \
                     "0000000000001976a914ad56321e69b7e2d30aeca9f49979ffc53084296f88ac00640000000000000017a91493a457d" \
                     "0e4cc789beb65eb77742d35297652dafe87006400000000000000160014ad56321e69b7e2d30aeca9f49979ffc53084" \
                     "296f00403a000000000000160014ad56321e69b7e2d30aeca9f49979ffc53084296f0002483045022100e3841478525" \
                     "ee6227f0725a4721d0ca3b81742043bee2ad5cbe22518a3effb2802206f34d721767b7d29916123a770e44b0c6a440e" \
                     "d8b4e46fb8aed206311ae996be012103f110404297e471ad86d1aabc8a885bd4d1ec71bc3f31bef8ed2ff9ad3032460" \
                     "000000000"


class TestGovernance:
    pass


class TestLoans:
    pass


class TestMasternode:
    pass


class TestPool:
    pass


class TestTxBuilder:
    tx_serialized = "040000000001011f5bf7e7c3bb19f0859837bf0a2c2fa45122657dd6b8249c49cbad808aa5a9720100000000ffffffff" \
                    "020000000000000000446a424466547842160014e9678d52be85d48ee605909dd937136b0798ec880117a914b1e44951" \
                    "2e420ba5e2e66c08b427ac5f04c2c19d87010f000000cb90a8010000000000d8cac10500000000160014e9678d52be85" \
                    "d48ee605909dd937136b0798ec880002473044022014102e4032ad8dc30dbd74203dd678bec62efc857df19cd9295c66" \
                    "a1f0e52bd202207e5afe81ccc521c7d7a259d93445b4f2892298f3b092e2e199de277d683e8b19012103e536a76363d1" \
                    "e4b44f9548c9e53f9d7c2fd8d354e0009c71f7f1944db13733b200000000"
    tx = Transaction.deserialize(DefichainMainnet, tx_serialized)

    inputs_tx_serialized = "040000000149b8ea9b2b0224e44126b86bd1e2889a7dac0ec06fcfb0dc4dd13782e1c84fce0100000000fffff" \
                           "fff0000000000"


class TestUTXO:
    addressAmountTo = BuildAddressAmounts()
    addressAmountTo.add(builder_p2pkh.get_address(), "DFI", 0.000001)
    addressAmountTo.add(builder_p2sh.get_address(), "DFI", 0.000001)
    addressAmountTo.add(builder_p2wpkh.get_address(), "DFI", 0.000001)

    send_p2pkh_serialized = "04000000016ace77fe1b2845a2d4a5540b7a4947cc6b218d9e1fc623929e712bbeae77fc48000000006b4830" \
                            "45022100ee38b5d75ff88580deef2035286ba21c0ad152a75bccc7dc8bd4ab6b1f9bf5e7022008d6be66f613" \
                            "51eaaa2d4339d4532b83aa2922f9633d11dbbbea385f2ef584a0012103f110404297e471ad86d1aabc8a885b" \
                            "d4d1ec71bc3f31bef8ed2ff9ad30324600ffffffff02e803000000000000160014ad56321e69b7e2d30aeca9" \
                            "f49979ffc53084296f0007030000000000001976a914ad56321e69b7e2d30aeca9f49979ffc53084296f88ac" \
                            "0000000000"
    send_p2sh_serialized = "0400000000010149b8ea9b2b0224e44126b86bd1e2889a7dac0ec06fcfb0dc4dd13782e1c84fce00000000171" \
                           "60014ad56321e69b7e2d30aeca9f49979ffc53084296fffffffff02e803000000000000160014ad56321e69b7" \
                           "e2d30aeca9f49979ffc53084296f00f00200000000000017a91493a457d0e4cc789beb65eb77742d35297652d" \
                           "afe870002483045022100d2ec53b5c5ec6eeddf8bd49bcf2200e578878d33379c0931f3811a99b8e0ef960220" \
                           "5a6c4502b08b82ca66af864094ad381d3b35cb4940e998b0f63390ed80d68570012103f110404297e471ad86d" \
                           "1aabc8a885bd4d1ec71bc3f31bef8ed2ff9ad3032460000000000"
    send_p2wpkh_serialized = "0400000000010149b8ea9b2b0224e44126b86bd1e2889a7dac0ec06fcfb0dc4dd13782e1c84fce010000000" \
                             "0ffffffff01fc3b000000000000160014ad56321e69b7e2d30aeca9f49979ffc53084296f00024730440220" \
                             "609ccd9e43c25a071f48a07a8c74a88fc81eec2248f1cbdbbcdc325d09b7703b022064f78a43a1a88dd6d80" \
                             "9aa46205298885dc69259738c127a08c510ef1311a792012103f110404297e471ad86d1aabc8a885bd4d1ec" \
                             "71bc3f31bef8ed2ff9ad3032460000000000"

    sendall_serialized = "0400000000010149b8ea9b2b0224e44126b86bd1e2889a7dac0ec06fcfb0dc4dd13782e1c84fce0100000000fff" \
                         "fffff01fc3b000000000000160014ad56321e69b7e2d30aeca9f49979ffc53084296f00024730440220609ccd9e" \
                         "43c25a071f48a07a8c74a88fc81eec2248f1cbdbbcdc325d09b7703b022064f78a43a1a88dd6d809aa462052988" \
                         "85dc69259738c127a08c510ef1311a792012103f110404297e471ad86d1aabc8a885bd4d1ec71bc3f31bef8ed2f" \
                         "f9ad3032460000000000"

    sendmany_same_change_address_serialized = "0400000000010149b8ea9b2b0224e44126b86bd1e2889a7dac0ec06fcfb0dc4dd13782" \
                                              "e1c84fce0100000000ffffffff0464000000000000001976a914ad56321e69b7e2d30a" \
                                              "eca9f49979ffc53084296f88ac00640000000000000017a91493a457d0e4cc789beb65" \
                                              "eb77742d35297652dafe87006400000000000000160014ad56321e69b7e2d30aeca9f4" \
                                              "9979ffc53084296f006c3a000000000000160014ad56321e69b7e2d30aeca9f49979ff" \
                                              "c53084296f000247304402205b3bd7940eb6f607d82f41a917d9c91a1e94ff902a76f8" \
                                              "305385d462c2a5226302201ab0f9641f45d31461a436c22fff3408266eca974f054b49" \
                                              "f9979bfaa5e505e2012103f110404297e471ad86d1aabc8a885bd4d1ec71bc3f31bef8" \
                                              "ed2ff9ad3032460000000000"

    sendmany_different_change_address_serialized = "0400000000010149b8ea9b2b0224e44126b86bd1e2889a7dac0ec06fcfb0dc4dd" \
                                                   "13782e1c84fce0100000000ffffffff0464000000000000001976a914ad56321e" \
                                                   "69b7e2d30aeca9f49979ffc53084296f88ac00640000000000000017a91493a45" \
                                                   "7d0e4cc789beb65eb77742d35297652dafe87006400000000000000160014ad56" \
                                                   "321e69b7e2d30aeca9f49979ffc53084296f00693a0000000000001976a914ad5" \
                                                   "6321e69b7e2d30aeca9f49979ffc53084296f88ac0002483045022100c9849a80" \
                                                   "d3540124ddd6ad399cb6b872931df30922adf041365f5afac6e755880220611bd" \
                                                   "8decbd382a9581fee960b04188f0ded343c69ffbdf3b62d13f8651586be012103" \
                                                   "f110404297e471ad86d1aabc8a885bd4d1ec71bc3f31bef8ed2ff9ad303246000" \
                                                   "0000000"


class TestVault:
    pass


print(builder_p2wpkh.data.hex_data(TestData.hex, TestData.addressAmountTo.build(), Addresses.P2WPKH))
