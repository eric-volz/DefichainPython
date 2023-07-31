import copy
from defichain.networks import DefichainMainnet
from defichain import Wallet
from defichain.transactions.utils import BuildAddressAmounts


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


class TestAccounts:
    value: int = 1000
    tokenId: int = 0
    mintingOutputsStart: int = 2

    addressAmounts = BuildAddressAmounts()
    addressAmounts.add(Addresses.P2PKH, 0, 1)
    addressAmounts.add(Addresses.P2PKH, "BTC", 1)
    addressAmounts.add(Addresses.P2PKH, "TSLA", 1)
    addressAmounts = addressAmounts.build()

    utxo_to_account_p2pkh_serialized: str = "6a2d4466547855011976a914ad56321e69b7e2d30aeca9f49979ffc53084296f88ac0100" \
                                            "000000e803000000000000"
    utxo_to_account_p2sh_serialized: str = "6a2b44665478550117a91493a457d0e4cc789beb65eb77742d35297652dafe87010000000" \
                                           "0e803000000000000"
    utxo_to_account_p2wpkh_serialized: str = "6a2a446654785501160014ad56321e69b7e2d30aeca9f49979ffc53084296f010000000" \
                                             "0e803000000000000"

    account_to_utxo_p2pkh_serialized: str = "6a2d44665478621976a914ad56321e69b7e2d30aeca9f49979ffc53084296f88ac010000" \
                                            "0000e80300000000000002"
    account_to_utxo_p2sh_serialized: str = "6a2b446654786217a91493a457d0e4cc789beb65eb77742d35297652dafe870100000000e" \
                                           "80300000000000002"
    account_to_utxo_p2wpkh_serialized: str = "6a2a4466547862160014ad56321e69b7e2d30aeca9f49979ffc53084296f0100000000e" \
                                             "80300000000000002"

    account_to_account_p2pkh_serialized: str = "6a4c5f44665478421976a914ad56321e69b7e2d30aeca9f49979ffc53084296f88ac0" \
                                               "11976a914ad56321e69b7e2d30aeca9f49979ffc53084296f88ac0300000000010000" \
                                               "0000000000020000000100000000000000710000000100000000000000"
    account_to_account_p2sh_serialized: str = "6a4c5d446654784217a91493a457d0e4cc789beb65eb77742d35297652dafe87011976" \
                                              "a914ad56321e69b7e2d30aeca9f49979ffc53084296f88ac0300000000010000000000" \
                                              "0000020000000100000000000000710000000100000000000000"
    account_to_account_p2wpkh_serialized: str = "6a4c5c4466547842160014ad56321e69b7e2d30aeca9f49979ffc53084296f011976" \
                                                "a914ad56321e69b7e2d30aeca9f49979ffc53084296f88ac03000000000100000000" \
                                                "000000020000000100000000000000710000000100000000000000"


class TestGovernance:
    proposalId: str = "1f4039ab714cf73ff1d92b58608ed20a73a799cde88c103b679bdafd83eb472b"
    masternodeId: str = "d590154d5b106d910cfc07850830b2ddd6f12094d89c2ed69a6e1a836ec7a0fd"
    decision: () = ("yes", "No", "neutral")

    vote_yes_serialized: str = "6a46446654784f2b47eb83fdda9b673b108ce8cd99a7730ad28e60582bd9f13ff74c71ab39401ffda0c76" \
                               "e831a6e9ad62e9cd89420f1d6ddb230088507fc0c916d105b4d1590d501"
    vote_no_serialized: str = "6a46446654784f2b47eb83fdda9b673b108ce8cd99a7730ad28e60582bd9f13ff74c71ab39401ffda0c76e" \
                              "831a6e9ad62e9cd89420f1d6ddb230088507fc0c916d105b4d1590d502"
    vote_neutral_serialized: str = "6a46446654784f2b47eb83fdda9b673b108ce8cd99a7730ad28e60582bd9f13ff74c71ab39401ffda" \
                                   "0c76e831a6e9ad62e9cd89420f1d6ddb230088507fc0c916d105b4d1590d503"


class TestLoans:
    vaultId: str = "ce39e5134cc16f4d2afc73c93098c88289e7f92d4d380909ac85c7a02d783200"
    amounts: [] = ["1@66", "1@TSLA"]

    takeloan_p2pkh_serialized: str = "6a4c5844665478580032782da0c785ac0909384d2df9e78982c89830c973fc2a4d6fc14c13e539c" \
                                     "e1976a914ad56321e69b7e2d30aeca9f49979ffc53084296f88ac02420000000100000000000000" \
                                     "710000000100000000000000"
    takeloan_p2sh_serialized: str = "6a4c5644665478580032782da0c785ac0909384d2df9e78982c89830c973fc2a4d6fc14c13e539ce" \
                                    "17a91493a457d0e4cc789beb65eb77742d35297652dafe8702420000000100000000000000710000" \
                                    "000100000000000000"
    takeloan_p2wpkh_serialized: str = "6a4c5544665478580032782da0c785ac0909384d2df9e78982c89830c973fc2a4d6fc14c13e539" \
                                      "ce160014ad56321e69b7e2d30aeca9f49979ffc53084296f024200000001000000000000007100" \
                                      "00000100000000000000"

    paybackloan_p2pkh_serialized: str = "6a4c5844665478480032782da0c785ac0909384d2df9e78982c89830c973fc2a4d6fc14c13e5" \
                                        "39ce1976a914ad56321e69b7e2d30aeca9f49979ffc53084296f88ac02420000000100000000" \
                                        "000000710000000100000000000000"
    paybackloan_p2sh_serialized: str = "6a4c5644665478480032782da0c785ac0909384d2df9e78982c89830c973fc2a4d6fc14c13e53" \
                                       "9ce17a91493a457d0e4cc789beb65eb77742d35297652dafe8702420000000100000000000000" \
                                       "710000000100000000000000"
    paybackloan_p2wpkh_serialized: str = "6a4c5544665478480032782da0c785ac0909384d2df9e78982c89830c973fc2a4d6fc14c13e" \
                                         "539ce160014ad56321e69b7e2d30aeca9f49979ffc53084296f024200000001000000000000" \
                                         "00710000000100000000000000"


class TestMasternode:
    mn_id: str = "995915f151be03337b5d0021d1cf0a5f8589f2d318db375f76625f550b135596"
    operatorAddress: str = "8WZsy6xubp4sn3CiMBQCz6CzBN3JdtpVNj"
    ownerAddress: str = "8VzWANbjh6GUZ48xorXuLg1ygh81w8ZSD9"
    rewardAddress: str = "df1qv2ld40h77h6jyc8v8z89hlgz82th08vfdvece3"
    timeLock: () = (0, 5, 10)

    create_massternode_timelock_0_serialized: str = "6a1a446654784301a9d692734b0130b71f39d1705aca21868b4950e4"
    create_massternode_timelock_5_serialized: str = "6a1c446654784301a9d692734b0130b71f39d1705aca21868b4950e40401"
    create_massternode_timelock_10_serialized: str = "6a1c446654784301a9d692734b0130b71f39d1705aca21868b4950e40802"

    resign_masternode_serialized: str = "6a2544665478529655130b555f62765f37db18d3f289855f0acfd121005d7b3303be51f1155999"

    update_masternode_serialized: str = "6a4c6b446654786d9655130b555f62765f37db18d3f289855f0acfd121005d7b3303be51f115" \
                                        "599903010114a386a4920ac131a0f506dea101d9f4a699f0da49020114a9d692734b0130b71f" \
                                        "39d1705aca21868b4950e403041462bedabefef5f52260ec388e5bfd023a97779d89"


class TestPool:
    addressFrom: str = Addresses.P2WPKH
    tokenFrom: str = "BTC"
    amountFrom: int = 1000
    addressTo: str = Addresses.P2PKH
    tokenTo: str = 0
    tokenTo2: str = 66
    maxPrice: int = 999999999
    pools: [] = ["BTC-DFI", "DFI-DUSD", "DUSD-MSTR"]

    poolswap_serialized: str = "6a4c504466547873160014ad56321e69b7e2d30aeca9f49979ffc53084296f02e8030000000000001976a" \
                               "914ad56321e69b7e2d30aeca9f49979ffc53084296f88ac000900000000000000ffe0f50500000000"
    compositeswap_serialized: str = "6a4c544466547869160014ad56321e69b7e2d30aeca9f49979ffc53084296f02e803000000000000" \
                                    "1976a914ad56321e69b7e2d30aeca9f49979ffc53084296f88ac420900000000000000ffe0f50500" \
                                    "00000003051147"

    addressAmount: {} = {Addresses.P2WPKH: ["100000000@DFI", "1070@BTC"]}

    addpoolliquidity_serialized: str = "6a4c4d446654786c01160014ad56321e69b7e2d30aeca9f49979ffc53084296f020000000000e" \
                                       "1f50500000000020000002e04000000000000160014ad56321e69b7e2d30aeca9f49979ffc530" \
                                       "84296f"

    removeAmount = "1@BTC-DFI"

    removepoolliquidity_serialized: str = "6a254466547872160014ad56321e69b7e2d30aeca9f49979ffc53084296f05010000000000" \
                                          "0000"


class TestVaults:
    ownerAddress: str = Addresses.P2WPKH
    schemeId: str = "MIN150"

    createvault_serialized: str = "6a234466547856160014ad56321e69b7e2d30aeca9f49979ffc53084296f064d494e313530"

    vaultId: str = "5cbe99407674a689fa9b8a522462b7a4b3e7893f61453ce3fa77f1307f7d0600"
    addressFrom: str = Addresses.P2WPKH
    amount: str = "1@DUSD"

    deposittovault_serialized: str = "6a45446654785300067d7f30f177fae33c45613f89e7b3a4b76224528a9bfa89a674764099be5c1" \
                                     "60014ad56321e69b7e2d30aeca9f49979ffc53084296f0f0100000000000000"

    addressTo: str = Addresses.P2WPKH

    withdrawfromvault_serialized: str = "6a45446654784a00067d7f30f177fae33c45613f89e7b3a4b76224528a9bfa89a674764099be" \
                                        "5c160014ad56321e69b7e2d30aeca9f49979ffc53084296f0f0100000000000000"
