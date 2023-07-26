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
