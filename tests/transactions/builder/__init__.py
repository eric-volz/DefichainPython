from defichain import Wallet, Ocean, TxBuilder
from defichain.networks import DefichainMainnet
from defichain.transactions.utils import BuildAddressAmounts


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


builder_p2pkh = TxBuilder(Keys.account.get_p2pkh(), Keys.account, Ocean())
builder_p2sh = TxBuilder(Keys.account.get_p2sh(), Keys.account, Ocean())
builder_p2wpkh = TxBuilder(Keys.account.get_p2wpkh(), Keys.account, Ocean())


class TestAccounts:
    pass


class TestData:
    pass


class TestGovernance:
    pass


class TestLoans:
    pass


class TestMasternode:
    pass


class TestPool:
    pass


class TestTxBuilder:
    pass


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
