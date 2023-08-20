from defichain import Wallet, Ocean, TxBuilder
from defichain.networks import DefichainMainnet
from defichain.transactions.rawtransactions import Transaction, TxP2WPKHInput
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
    addressAmountTo = BuildAddressAmounts()
    addressAmountTo.add(builder_p2pkh.get_address(), "DFI", 0.000001)
    addressAmountTo.add(builder_p2sh.get_address(), "DFI", 0.000001)
    addressAmountTo.add(builder_p2wpkh.get_address(), "DFI", 0.000001)

    utxo_to_account_serialized = "0400000000010149b8ea9b2b0224e44126b86bd1e2889a7dac0ec06fcfb0dc4dd13782e1c84fce01000" \
                                 "00000ffffffff02e8030000000000002c6a2a446654785501160014ad56321e69b7e2d30aeca9f49979" \
                                 "ffc53084296f0100000000e80300000000000000de37000000000000160014ad56321e69b7e2d30aeca" \
                                 "9f49979ffc53084296f000247304402202bb5f317aad5169d3a2c28fff5a2b2054919de11b1ca27b5c9" \
                                 "fdbe6e604a349c0220313ed9f1e8aa6299beb6de2d2b4f0257bce1a75d8a544bfac2e9f69976c8ab4f0" \
                                 "12103f110404297e471ad86d1aabc8a885bd4d1ec71bc3f31bef8ed2ff9ad3032460000000000"

    account_to_utxo_serialized = "0400000000010149b8ea9b2b0224e44126b86bd1e2889a7dac0ec06fcfb0dc4dd13782e1c84fce01000" \
                                 "00000ffffffff0500000000000000002c6a2a4466547862160014ad56321e69b7e2d30aeca9f49979ff" \
                                 "c53084296f01000000002c010000000000000200623b000000000000160014ad56321e69b7e2d30aeca" \
                                 "9f49979ffc53084296f0064000000000000001976a914ad56321e69b7e2d30aeca9f49979ffc5308429" \
                                 "6f88ac00640000000000000017a91493a457d0e4cc789beb65eb77742d35297652dafe8700640000000" \
                                 "0000000160014ad56321e69b7e2d30aeca9f49979ffc53084296f000247304402203a3d19170629e354" \
                                 "55c8169a213f08db2c9a3a4483a88b545fc0f2d9a48e1c9b02206bc53e2fc118d33f900ab01ee771fed" \
                                 "dd215108b73bd7009b58c51ce4e92a0fb012103f110404297e471ad86d1aabc8a885bd4d1ec71bc3f31" \
                                 "bef8ed2ff9ad3032460000000000"

    account_to_account_serialized = "0400000000010149b8ea9b2b0224e44126b86bd1e2889a7dac0ec06fcfb0dc4dd13782e1c84fce01" \
                                    "00000000ffffffff020000000000000000906a4c8d4466547842160014ad56321e69b7e2d30aeca9" \
                                    "f49979ffc53084296f031976a914ad56321e69b7e2d30aeca9f49979ffc53084296f88ac01000000" \
                                    "00640000000000000017a91493a457d0e4cc789beb65eb77742d35297652dafe8701000000006400" \
                                    "000000000000160014ad56321e69b7e2d30aeca9f49979ffc53084296f0100000000640000000000" \
                                    "000000623b000000000000160014ad56321e69b7e2d30aeca9f49979ffc53084296f000247304402" \
                                    "20317cb4dd19fb1d8d69e006f55ca6cd7e04697dad4ae8b6ac3c18e9990d538293022055712f1240" \
                                    "2da68ebfbc269e5e25186c8b6b3f0bdc0d07e020edc142587aaf3d012103f110404297e471ad86d1" \
                                    "aabc8a885bd4d1ec71bc3f31bef8ed2ff9ad3032460000000000"


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
    proposal_id = "1f4039ab714cf73ff1d92b58608ed20a73a799cde88c103b679bdafd83eb472b"
    mn_id = "977969d7aaa3748d1156f569368d997213a055d051fdb1ae744e979e714f415f"

    vote_yes_serialized = "0400000000010149b8ea9b2b0224e44126b86bd1e2889a7dac0ec06fcfb0dc4dd13782e1c84fce0100000000ff" \
                          "ffffff020000000000000000486a46446654784f2b47eb83fdda9b673b108ce8cd99a7730ad28e60582bd9f13f" \
                          "f74c71ab39401f5f414f719e974e74aeb1fd51d055a01372998d3669f556118d74a3aad76979970100aa3b0000" \
                          "00000000160014ad56321e69b7e2d30aeca9f49979ffc53084296f000247304402203e5b60ebcb8c287fc7b5a6" \
                          "68e4ff3263c511693a85a04164995a5dbabf6286700220710f8c1a5b31a5b6b0efd9368d7bd44d4a708ff215fb" \
                          "9783f78d250b359947f6012103f110404297e471ad86d1aabc8a885bd4d1ec71bc3f31bef8ed2ff9ad30324600" \
                          "00000000"
    vote_no_serialized = "0400000000010149b8ea9b2b0224e44126b86bd1e2889a7dac0ec06fcfb0dc4dd13782e1c84fce0100000000fff" \
                         "fffff020000000000000000486a46446654784f2b47eb83fdda9b673b108ce8cd99a7730ad28e60582bd9f13ff7" \
                         "4c71ab39401f5f414f719e974e74aeb1fd51d055a01372998d3669f556118d74a3aad76979970200aa3b0000000" \
                         "00000160014ad56321e69b7e2d30aeca9f49979ffc53084296f0002473044022047b44ee8781ba055a862685691" \
                         "2a79de925ef14a72616bee333ebc6e344b6392022071e20cdabc89d3ec0817447c2c001f745e452ada307f2b600" \
                         "0d604a6ddd4619b012103f110404297e471ad86d1aabc8a885bd4d1ec71bc3f31bef8ed2ff9ad30324600000000" \
                         "00"
    vote_neutral_serialized = "0400000000010149b8ea9b2b0224e44126b86bd1e2889a7dac0ec06fcfb0dc4dd13782e1c84fce01000000" \
                              "00ffffffff020000000000000000486a46446654784f2b47eb83fdda9b673b108ce8cd99a7730ad28e6058" \
                              "2bd9f13ff74c71ab39401f5f414f719e974e74aeb1fd51d055a01372998d3669f556118d74a3aad7697997" \
                              "0300aa3b000000000000160014ad56321e69b7e2d30aeca9f49979ffc53084296f00024830450221009443" \
                              "17eec70221bba9f0aaf1e17891abd6282854965c50b3ac6b7b48e753452a022052f5df31d4913e886f18f2" \
                              "762b6c157e1412af36a6eaadef9f7da0e2d651aa13012103f110404297e471ad86d1aabc8a885bd4d1ec71" \
                              "bc3f31bef8ed2ff9ad3032460000000000"


class TestLoans:
    amounts = ["0.001@SPY", "0.0001@TSLA"]
    vault_id = "5cbe99407674a689fa9b8a522462b7a4b3e7893f61453ce3fa77f1307f7d0600"

    take_loan_serialized = "0400000000010149b8ea9b2b0224e44126b86bd1e2889a7dac0ec06fcfb0dc4dd13782e1c84fce0100000000f" \
                           "fffffff020000000000000000586a4c55446654785800067d7f30f177fae33c45613f89e7b3a4b76224528a9b" \
                           "fa89a674764099be5c160014ad56321e69b7e2d30aeca9f49979ffc53084296f021a000000a08601000000000" \
                           "0710000001027000000000000009a3b000000000000160014ad56321e69b7e2d30aeca9f49979ffc53084296f" \
                           "00024830450221009cbc87587a11d94a5d7ac2cbb546927d7c80ef717ac086dde3f12c6b7e6d030602202fb3b" \
                           "815dbd286bfe3f1ba2db52c60c3b67b7c6bb5dee98d1dd732f5f46570e1012103f110404297e471ad86d1aabc" \
                           "8a885bd4d1ec71bc3f31bef8ed2ff9ad3032460000000000"

    payback_loan_serialized = "0400000000010149b8ea9b2b0224e44126b86bd1e2889a7dac0ec06fcfb0dc4dd13782e1c84fce01000000" \
                              "00ffffffff020000000000000000586a4c55446654784800067d7f30f177fae33c45613f89e7b3a4b76224" \
                              "528a9bfa89a674764099be5c160014ad56321e69b7e2d30aeca9f49979ffc53084296f021a000000a08601" \
                              "0000000000710000001027000000000000009a3b000000000000160014ad56321e69b7e2d30aeca9f49979" \
                              "ffc53084296f0002473044022013634f57e363f1356401d802a6dc734a0d575f3382f4b78560c2e414d486" \
                              "2409022008436c9ab919fc8d0a51c3f82a5c309d9259b46b19971e1844ee429b9a8f340a012103f1104042" \
                              "97e471ad86d1aabc8a885bd4d1ec71bc3f31bef8ed2ff9ad3032460000000000"


class TestMasternode:
    operatorAddress = Addresses.P2PKH
    ownerAddress = Addresses.P2WPKH
    rewardAddress = Addresses.P2WPKH
    mn_id = "bb0b3fbf55ca4153601a0c636420b8107c1fbd7c745cd9fcf7b939f9a248c3f5"
    input = TxP2WPKHInput("bb0b3fbf55ca4153601a0c636420b8107c1fbd7c745cd9fcf7b939f9a248c3f5", 0, Addresses.P2WPKH,
                          2001100000000)

    createmasternode_serialized = "04000000000101f5c348a2f939b9f7fcd95c747cbd1f7c10b82064630c1a605341ca55bf3f0bbb0000" \
                                  "000000ffffffff0300ca9a3b000000001c6a1a446654784301ad56321e69b7e2d30aeca9f49979ffc5" \
                                  "3084296f0000204aa9d1010000160014ad56321e69b7e2d30aeca9f49979ffc53084296f00fadff505" \
                                  "00000000160014ad56321e69b7e2d30aeca9f49979ffc53084296f0002483045022100e8f6ef84400b" \
                                  "2699504f65c38eef15c480ff3b466a0c649a6436aef872ca22b702204e06f4590de172c7c9720d96b6" \
                                  "47e0f878b44499cadbe49fcff057d1e3b72fe7012103f110404297e471ad86d1aabc8a885bd4d1ec71" \
                                  "bc3f31bef8ed2ff9ad3032460000000000"

    resignmasternode_serialized = "0400000000010149b8ea9b2b0224e44126b86bd1e2889a7dac0ec06fcfb0dc4dd13782e1c84fce0100" \
                                  "000000ffffffff020000000000000000276a254466547852f5c348a2f939b9f7fcd95c747cbd1f7c10" \
                                  "b82064630c1a605341ca55bf3f0bbb00cb3b000000000000160014ad56321e69b7e2d30aeca9f49979" \
                                  "ffc53084296f00024830450221009f83118db2e647f62c334300243ad6e7e8ce10c999b0ebb19c2e2a" \
                                  "a8eb3fc344022048fe5f0737bb520e0da66bef2ec66bf672bb9a98c62e919bd9158c0ce61a007f0121" \
                                  "03f110404297e471ad86d1aabc8a885bd4d1ec71bc3f31bef8ed2ff9ad3032460000000000"

    updatemasternode_serialized = "0400000000010149b8ea9b2b0224e44126b86bd1e2889a7dac0ec06fcfb0dc4dd13782e1c84fce0100" \
                                  "000000ffffffff0200000000000000006e6a4c6b446654786df5c348a2f939b9f7fcd95c747cbd1f7c" \
                                  "10b82064630c1a605341ca55bf3f0bbb03010414ad56321e69b7e2d30aeca9f49979ffc53084296f02" \
                                  "0114ad56321e69b7e2d30aeca9f49979ffc53084296f030414ad56321e69b7e2d30aeca9f49979ffc5" \
                                  "3084296f00843b000000000000160014ad56321e69b7e2d30aeca9f49979ffc53084296f0002483045" \
                                  "022100bbfd15e70473bcd068084b70d10d8b99652b15b972ccce8148fcb2f39f136942022060b13920" \
                                  "62df2268febd4faf7513a43850a14f230d98cfd4a96a3bc92b4429f2012103f110404297e471ad86d1" \
                                  "aabc8a885bd4d1ec71bc3f31bef8ed2ff9ad3032460000000000"


class TestPool:
    addressFrom = Addresses.P2WPKH
    tokenFrom = "BTC"
    amountFrom = 0.00001
    addressTo = Addresses.P2WPKH
    tokenTo = "DFI"
    maxPrice = 999999999999
    pools = ["BTC-DFI"]

    addressAmountFrom = BuildAddressAmounts()
    addressAmountFrom.add(builder_p2pkh.get_address(), "DFI", 1)
    addressAmountFrom.add(builder_p2sh.get_address(), "BTC", 0.00000900)

    amount = "1@BTC-DFI"

    poolswap_serialized = "0400000000010149b8ea9b2b0224e44126b86bd1e2889a7dac0ec06fcfb0dc4dd13782e1c84fce0100000000ff" \
                          "ffffff020000000000000000506a4c4d4466547873160014ad56321e69b7e2d30aeca9f49979ffc53084296f02" \
                          "e803000000000000160014ad56321e69b7e2d30aeca9f49979ffc53084296f00ff0fa5d4e80000000000000000" \
                          "00000000a23b000000000000160014ad56321e69b7e2d30aeca9f49979ffc53084296f0002473044022047ae54" \
                          "3054577329232db52d4c751e57c90cbfca85550480e6ef0bcc6217b0c30220504807313852d5b3c322ae1f7df1" \
                          "c58d95865f8271e22b67dbe408b20b7917c6012103f110404297e471ad86d1aabc8a885bd4d1ec71bc3f31bef8" \
                          "ed2ff9ad3032460000000000"

    compositeswap_serialized = "0400000000010149b8ea9b2b0224e44126b86bd1e2889a7dac0ec06fcfb0dc4dd13782e1c84fce0100000" \
                               "000ffffffff020000000000000000526a4c4f4466547869160014ad56321e69b7e2d30aeca9f49979ffc5" \
                               "3084296f02e803000000000000160014ad56321e69b7e2d30aeca9f49979ffc53084296f00ff0fa5d4e80" \
                               "000000000000000000000010500a03b000000000000160014ad56321e69b7e2d30aeca9f49979ffc53084" \
                               "296f0002483045022100e5c90efa4faa569353d6909fe8a074fe08431dcef7a1d8f6a6ae4ed28492f6af0" \
                               "2206fc034dfbb74e6a4e195ebeca5f0b694186f88a34c6e91230bee98556feffc96012103f110404297e4" \
                               "71ad86d1aabc8a885bd4d1ec71bc3f31bef8ed2ff9ad3032460000000000"

    addpoolliquidity_serialized = "0400000000010149b8ea9b2b0224e44126b86bd1e2889a7dac0ec06fcfb0dc4dd13782e1c84fce0100" \
                                  "000000ffffffff0200000000000000006c6a4c69446654786c021976a914ad56321e69b7e2d30aeca9" \
                                  "f49979ffc53084296f88ac010000000000e1f5050000000017a91493a457d0e4cc789beb65eb77742d" \
                                  "35297652dafe8701020000008403000000000000160014ad56321e69b7e2d30aeca9f49979ffc53084" \
                                  "296f00863b000000000000160014ad56321e69b7e2d30aeca9f49979ffc53084296f00024730440220" \
                                  "3ea1ddcbe2d83bcb29d4b085dd2437ad8f551fca59f0e9da6d21c23431bd813e022059489220dea26d" \
                                  "7a525cd0a32729fb72788518c63dfa2b0d7bcd04d130af22d9012103f110404297e471ad86d1aabc8a" \
                                  "885bd4d1ec71bc3f31bef8ed2ff9ad3032460000000000"

    removepoolliquidity_serialized = "0400000000010149b8ea9b2b0224e44126b86bd1e2889a7dac0ec06fcfb0dc4dd13782e1c84fce0" \
                                     "100000000ffffffff020000000000000000276a254466547872160014ad56321e69b7e2d30aeca9" \
                                     "f49979ffc53084296f0500e1f5050000000000cb3b000000000000160014ad56321e69b7e2d30ae" \
                                     "ca9f49979ffc53084296f000247304402204acca74602c6d0428d38869b10a97831bde0f1c89ab1" \
                                     "c736f52c3cb1584ec37602201d7357fcd0192f923387a402c6c53cb5402eb6fd4edd401f6ab5073" \
                                     "ad4cd89a3012103f110404297e471ad86d1aabc8a885bd4d1ec71bc3f31bef8ed2ff9ad30324600" \
                                     "00000000"


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
