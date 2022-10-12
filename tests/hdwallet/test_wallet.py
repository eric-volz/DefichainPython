import pytest
import json
from defichain import Wallet
from defichain.networks import DefichainMainnet


class TestVectors:
    DEFAULT_1_ADDRESS: str
    BECH32_1_ADDRESS: str
    LEGACY_1_ADDRESS: str
    WIF_1_KEY: str
    UNCOMPRESSED_1: str
    COMPRESSED_1: str
    PRIVATE_1_KEY: str
    PUBLIC_1_KEY: str
    CHAIN_CODE_1: str
    HASH_1: str
    FINGER_PRINT_1: str
    DUMPS_1: str

    DEFAULT_2_ADDRESS: str
    BECH32_2_ADDRESS: str
    LEGACY_2_ADDRESS: str
    WIF_2_KEY: str
    UNCOMPRESSED_2: str
    COMPRESSED_2: str
    PRIVATE_2_KEY: str
    PUBLIC_2_KEY: str
    CHAIN_CODE_2: str
    HASH_2: str
    FINGER_PRINT_2: str
    DUMPS_2: str

    DEFAULT_PASSPHRASE_ADDRESS: str
    BECH32_PASSPHRASE_ADDRESS: str
    LEGACY_PASSPHRASE_ADDRESS: str
    WIF_PASSPHRASE_KEY: str
    UNCOMPRESSED_PASSPHRASE: str
    COMPRESSED_PASSPHRASE: str
    PRIVATE_PASSPHRASE_KEY: str
    PUBLIC_PASSPHRASE_KEY: str
    CHAIN_CODE_PASSPHRASE: str
    HASH_PASSPHRASE: str
    FINGER_PRINT_PASSPHRASE: str
    DUMPS_PASSPHRASE: str

    ENTROPY: str
    MNEMONIC: str
    SEED: str
    SEED_PASSPHRASE: str
    xPRIVATE_KEY: str
    xPUBLIC_KEY: str
    WIF: str
    PRIVATE_KEY: str
    PUBLIC_KEY: str
    PATH_1: str
    PATH_2: str
    INDEX_1: str
    INDEX_2: str
    INDEX_3: str
    INDEX_4: str

    ROOT_xPRIVATE_KEY: str
    ROOT_xPUBLIC_KEY: str
    ROOT_xPRIVATE_KEY_PASSPHRASE: str
    ROOT_xPUBLIC_KEY_PASSPHRASE: str
    STRENGHT: str
    PASSPHRASE: str
    LANGUAGE: str
    CRYPTOCURRENCY: str
    SYMBOL: str
    SEMANTIC: str
    NETWORK: str


class Vectors(TestVectors):
    DEFAULT_1_ADDRESS = "db1UZE7tyvZ8R6V4HavCeCifKzLUiFDqxa"
    BECH32_1_ADDRESS = "df1q2n54p3xnvk3djulmdvresl3p5xmzzn43zm264a"
    LEGACY_1_ADDRESS = "8Nppz7bUwsQHTrwJdKKeYVPaGS9mcZyf2J"
    WIF_1_KEY = "L2qGxrTTFxoU5vygbRDHz7g8aa1951ZvDwiTK46t8jCvH37C3GUN"
    UNCOMPRESSED_1 = "ff92aed3b7563d73da7c2c8810ec78182574e12a8210878b5d7b91ee0ae70f07baed4b3d4c6a1a7d720dfa1f7cf1d12bc97a5baee53dde8c2697a83cada6569c"
    COMPRESSED_1 = "02ff92aed3b7563d73da7c2c8810ec78182574e12a8210878b5d7b91ee0ae70f07"
    PRIVATE_1_KEY = "a77ba904f0a431f49be1c83bb8847b5d1002f551a5e0fda5f4954fd90d78807d"
    PUBLIC_1_KEY = "02ff92aed3b7563d73da7c2c8810ec78182574e12a8210878b5d7b91ee0ae70f07"
    CHAIN_CODE_1 = "dc75ac21bc729ea83d363d289746ec59d61b2d9c8f56bd61d6ef062dd9e8222b"
    HASH_1 = "54e950c4d365a2d973fb6b07987e21a1b6214eb1"
    FINGER_PRINT_1 = "54e950c4"
    t = "{'cryptocurrency': 'Defichain', 'symbol': 'DFI', 'network': 'mainnet', 'strength': 128, 'entropy': 'ee535b143b0d9d1f87546f9df0d06b1a', 'mnemonic': 'unusual onion shallow invite supply more bubble mistake over make bracket cry', 'language': 'english', 'passphrase': None, 'seed': '313a29e024ad78b0ce1d978c850c4e0284ec18caff25059449fd583e6f7aa265f1c2968cb2e5867fc6d51ad2a40c72ee451f3b81a36d5f3dc4ea4e94a25c8f79', 'root_xprivate_key': 'xprv9s21ZrQH143K3wyDj3RFDZ2NyueHmj42SkAhqN62guhz5hr5N2qzPKzLnzrRsYdi4DwoeBeqKyjizqdiSNr3yAn2yMMMwWoJQp2PsC4BPLp', 'root_xpublic_key': 'xpub661MyMwAqRbcGS3gq4xFagy7XwUnBBmsoy6JdkVeFFExxWBDuaAEw8JpeFVhYKJctV1ZXFdV6SPoN41MVkNMdTcZpxcqJoRWgJvede7ME9n', 'uncompressed': 'ff92aed3b7563d73da7c2c8810ec78182574e12a8210878b5d7b91ee0ae70f07baed4b3d4c6a1a7d720dfa1f7cf1d12bc97a5baee53dde8c2697a83cada6569c', 'compressed': '02ff92aed3b7563d73da7c2c8810ec78182574e12a8210878b5d7b91ee0ae70f07', 'chain_code': 'dc75ac21bc729ea83d363d289746ec59d61b2d9c8f56bd61d6ef062dd9e8222b', 'private_key': 'a77ba904f0a431f49be1c83bb8847b5d1002f551a5e0fda5f4954fd90d78807d', 'public_key': '02ff92aed3b7563d73da7c2c8810ec78182574e12a8210878b5d7b91ee0ae70f07', 'wif': 'L2qGxrTTFxoU5vygbRDHz7g8aa1951ZvDwiTK46t8jCvH37C3GUN', 'finger_print': '54e950c4', 'semantic': 'p2pkh', 'path': 'm/1129/0/0/0', 'hash': '54e950c4d365a2d973fb6b07987e21a1b6214eb1', 'addresses': {'legacy': '8Nppz7bUwsQHTrwJdKKeYVPaGS9mcZyf2J', 'bech32': 'df1q2n54p3xnvk3djulmdvresl3p5xmzzn43zm264a', 'default': 'db1UZE7tyvZ8R6V4HavCeCifKzLUiFDqxa'}}"
    DEFAULT_2_ADDRESS = "dFmeYSHXymdybpjUmNTsUfvX4vxcznXXux"
    BECH32_2_ADDRESS = "df1qtmy47ksc9t8z0avnn9xqelyy4u5ujcsjeqx99y"
    LEGACY_2_ADDRESS = "8Pj3UbHEYBtXUkxo9DFrz3a6ShssS3tmLr"
    WIF_2_KEY = "KzxppKqb9MT8GP94tnypD8ux3b5NvfrQu7UFZfTFELSDq77Rx2C4"
    UNCOMPRESSED_2 = "da11be60fbc6b2dbadc6678370ed153463dc9f499ff9ac2efb91b0831686ff6f6f63fe47b165211d039c8cd78c4f2fbe3277317bf1e94a5dbfd7e0e73f6ddd10"
    COMPRESSED_2 = "02da11be60fbc6b2dbadc6678370ed153463dc9f499ff9ac2efb91b0831686ff6f"
    PRIVATE_2_KEY = "6fb11ca588b36b13e600bbd06af491f1dc2495f51cc6acaec6f0916648370af5"
    PUBLIC_2_KEY = "02da11be60fbc6b2dbadc6678370ed153463dc9f499ff9ac2efb91b0831686ff6f"
    CHAIN_CODE_2 = "3cfe54f06b1ea806db43e6cd6a10399615b535be64a9400229b1cb419e82e1f8"
    HASH_2 = "5ec95f5a182ace27f593994c0cfc84af29c96212"
    FINGER_PRINT_2 = "5ec95f5a"

    DEFAULT_PASSPHRASE_ADDRESS = "dM64uZpczPDYSgEEi3sC1FmfeD3VEsUAVX"
    BECH32_PASSPHRASE_ADDRESS = "df1qd4ke9dcyzeg09udmcryxlftplsatkl5wv024sv"
    LEGACY_PASSPHRASE_ADDRESS = "8R4Te8wY8pKxYjxT8Y7MjdeaQEXPw3TVWr"
    WIF_PASSPHRASE_KEY = "L1BN9Nn2tMr6Zvy8tL1wxRe1CXrkF7BjCEucocUKmWPpw2UjoGuu"
    UNCOMPRESSED_PASSPHRASE = "2e2927c66300c407e0e7f148f54b9be305385a68d9dcd68b522749dbe68e14d80c838cc503ad6e2024ce4387bc0dffb0296228d3f5f8d8176535f6a160a22f37"
    COMPRESSED_PASSPHRASE = "032e2927c66300c407e0e7f148f54b9be305385a68d9dcd68b522749dbe68e14d8"
    PRIVATE_PASSPHRASE_KEY = "762499a31b7b53451d7ebd62c49a5201632293ebb2dff0aa0962d2c465f80bff"
    PUBLIC_PASSPHRASE_KEY = "032e2927c66300c407e0e7f148f54b9be305385a68d9dcd68b522749dbe68e14d8"
    CHAIN_CODE_PASSPHRASE = "2ecdfb1efd4bdc514ddfcff2d6225c7b1604f4ede53ca1f52a3a1dda3000e989"
    HASH_PASSPHRASE = "6d6d92b7041650f2f1bbc0c86fa561fc3abb7e8e"
    FINGER_PRINT_PASSPHRASE = "6d6d92b7"
    DUMPS_PASSPHRASE = "{'cryptocurrency': 'Defichain', 'symbol': 'DFI', 'network': 'mainnet', 'strength': 128, 'entropy': 'ee535b143b0d9d1f87546f9df0d06b1a', 'mnemonic': 'unusual onion shallow invite supply more bubble mistake over make bracket cry', 'language': 'english', 'passphrase': None, 'seed': '313a29e024ad78b0ce1d978c850c4e0284ec18caff25059449fd583e6f7aa265f1c2968cb2e5867fc6d51ad2a40c72ee451f3b81a36d5f3dc4ea4e94a25c8f79', 'root_xprivate_key': 'xprv9s21ZrQH143K3wyDj3RFDZ2NyueHmj42SkAhqN62guhz5hr5N2qzPKzLnzrRsYdi4DwoeBeqKyjizqdiSNr3yAn2yMMMwWoJQp2PsC4BPLp', 'root_xpublic_key': 'xpub661MyMwAqRbcGS3gq4xFagy7XwUnBBmsoy6JdkVeFFExxWBDuaAEw8JpeFVhYKJctV1ZXFdV6SPoN41MVkNMdTcZpxcqJoRWgJvede7ME9n', 'uncompressed': 'ff92aed3b7563d73da7c2c8810ec78182574e12a8210878b5d7b91ee0ae70f07baed4b3d4c6a1a7d720dfa1f7cf1d12bc97a5baee53dde8c2697a83cada6569c', 'compressed': '02ff92aed3b7563d73da7c2c8810ec78182574e12a8210878b5d7b91ee0ae70f07', 'chain_code': 'dc75ac21bc729ea83d363d289746ec59d61b2d9c8f56bd61d6ef062dd9e8222b', 'private_key': 'a77ba904f0a431f49be1c83bb8847b5d1002f551a5e0fda5f4954fd90d78807d', 'public_key': '02ff92aed3b7563d73da7c2c8810ec78182574e12a8210878b5d7b91ee0ae70f07', 'wif': 'L2qGxrTTFxoU5vygbRDHz7g8aa1951ZvDwiTK46t8jCvH37C3GUN', 'finger_print': '54e950c4', 'semantic': 'p2pkh', 'path': 'm/1129/0/0/0', 'hash': '54e950c4d365a2d973fb6b07987e21a1b6214eb1', 'addresses': {'legacy': '8Nppz7bUwsQHTrwJdKKeYVPaGS9mcZyf2J', 'bech32': 'df1q2n54p3xnvk3djulmdvresl3p5xmzzn43zm264a', 'default': 'db1UZE7tyvZ8R6V4HavCeCifKzLUiFDqxa'}}"

    ENTROPY = "ee535b143b0d9d1f87546f9df0d06b1a"
    MNEMONIC = "unusual onion shallow invite supply more bubble mistake over make bracket cry"
    SEED = "313a29e024ad78b0ce1d978c850c4e0284ec18caff25059449fd583e6f7aa265f1c2968cb2e5867fc6d51ad2a40c72ee451f3b81a36d5f3dc4ea4e94a25c8f79"
    SEED_PASSPHRASE = "df653d88cc549d56cc460a34167f429ee987d4b8651065abe88f05cb1d9be82e836bb749db36eddb306d6eb1bb6bd6bb77e55a0961673c804359eb13b80a61bf"
    PATH_1 = "m/1129/0/0/0"
    PATH_2 = "m/1129/0/0/1"
    INDEX_1 = "1129"
    INDEX_2 = "0"
    INDEX_3 = "0"
    INDEX_4 = "0"

    ROOT_xPRIVATE_KEY = "xprv9s21ZrQH143K3wyDj3RFDZ2NyueHmj42SkAhqN62guhz5hr5N2qzPKzLnzrRsYdi4DwoeBeqKyjizqdiSNr3yAn2yMMMwWoJQp2PsC4BPLp"
    ROOT_xPUBLIC_KEY = "xpub661MyMwAqRbcGS3gq4xFagy7XwUnBBmsoy6JdkVeFFExxWBDuaAEw8JpeFVhYKJctV1ZXFdV6SPoN41MVkNMdTcZpxcqJoRWgJvede7ME9n"
    ROOT_xPRIVATE_KEY_PASSPHRASE = "xprv9s21ZrQH143K4VewJbSSUZf9MCBYFLRkEG1vWgtCLqJ68nmSCsicHifVpfEGBxsWgJQooWXe8HRg6gsghddtJkKAPgf416F3o47XBov2N2U"
    ROOT_xPUBLIC_KEY_PASSPHRASE = "xpub661MyMwAqRbcGyjQQcySqhbsuE22eo9bbUwXK5HouAq51b6akR2rqWyyfxEmqVRnDf2S42JeF9YiQ6RmtNQv2VLHY6JtPcqXJfk5c1F3w4D"
    STRENGHT = 128
    PASSPHRASE = "passphrase"
    LANGUAGE = "english"
    CRYPTOCURRENCY = "Defichain"
    SYMBOL = "DFI"
    SEMANTIC = "p2pkh"
    NETWORK = "mainnet"


@pytest.mark.hdwallet
def test_wallet():  # 01
    assert Wallet(DefichainMainnet)
    assert Wallet(DefichainMainnet, "P2PKH")
    assert Wallet(network=DefichainMainnet, semantic="P2PKH", use_default_path=True)


@pytest.mark.hdwallet
def test_from_entropy():  # 02
    wallet = Wallet(network=DefichainMainnet)
    wallet.from_entropy(entropy=Vectors.ENTROPY, language="english", passphrase=None)

    assert Vectors.CRYPTOCURRENCY == wallet.cryptocurrency()
    assert Vectors.SYMBOL == wallet.symbol()
    assert Vectors.NETWORK == wallet.network()
    assert Vectors.STRENGHT == wallet.strength()
    assert Vectors.ENTROPY == wallet.entropy()
    assert Vectors.MNEMONIC == wallet.mnemonic()
    assert Vectors.LANGUAGE == wallet.language()
    assert None is wallet.passphrase()
    assert Vectors.SEED == wallet.seed()
    assert Vectors.ROOT_xPRIVATE_KEY == wallet.root_xprivate_key()
    assert Vectors.ROOT_xPUBLIC_KEY == wallet.root_xpublic_key()
    assert Vectors.UNCOMPRESSED_1 == wallet.uncompressed()
    assert Vectors.COMPRESSED_1 == wallet.compressed()
    assert Vectors.CHAIN_CODE_1 == wallet.chain_code()
    assert Vectors.PRIVATE_1_KEY == wallet.private_key()
    assert Vectors.PUBLIC_1_KEY == wallet.public_key()
    assert Vectors.WIF_1_KEY == wallet.wif()
    assert Vectors.FINGER_PRINT_1 == wallet.finger_print()
    assert Vectors.SEMANTIC == wallet.semantic()
    assert Vectors.PATH_1 == wallet.path()
    assert Vectors.HASH_1 == wallet.hash()
    assert Vectors.DEFAULT_1_ADDRESS == wallet.default_address()
    assert Vectors.BECH32_1_ADDRESS == wallet.bech32_address()
    assert Vectors.LEGACY_1_ADDRESS == wallet.legacy_address()


@pytest.mark.hdwallet
def test_from_mnemonic():  # 03
    wallet = Wallet(network=DefichainMainnet)
    wallet.from_mnemonic(mnemonic=Vectors.MNEMONIC, language="english", passphrase=None)

    assert Vectors.CRYPTOCURRENCY == wallet.cryptocurrency()
    assert Vectors.SYMBOL == wallet.symbol()
    assert Vectors.NETWORK == wallet.network()
    assert Vectors.STRENGHT == wallet.strength()
    assert Vectors.ENTROPY == wallet.entropy()
    assert Vectors.MNEMONIC == wallet.mnemonic()
    assert Vectors.LANGUAGE == wallet.language()
    assert None is wallet.passphrase()
    assert Vectors.SEED == wallet.seed()
    assert Vectors.ROOT_xPRIVATE_KEY == wallet.root_xprivate_key()
    assert Vectors.ROOT_xPUBLIC_KEY == wallet.root_xpublic_key()
    assert Vectors.UNCOMPRESSED_1 == wallet.uncompressed()
    assert Vectors.COMPRESSED_1 == wallet.compressed()
    assert Vectors.CHAIN_CODE_1 == wallet.chain_code()
    assert Vectors.PRIVATE_1_KEY == wallet.private_key()
    assert Vectors.PUBLIC_1_KEY == wallet.public_key()
    assert Vectors.WIF_1_KEY == wallet.wif()
    assert Vectors.FINGER_PRINT_1 == wallet.finger_print()
    assert Vectors.SEMANTIC == wallet.semantic()
    assert Vectors.PATH_1 == wallet.path()
    assert Vectors.HASH_1 == wallet.hash()
    assert Vectors.DEFAULT_1_ADDRESS == wallet.default_address()
    assert Vectors.BECH32_1_ADDRESS == wallet.bech32_address()
    assert Vectors.LEGACY_1_ADDRESS == wallet.legacy_address()


@pytest.mark.hdwallet
def test_from_seed():  # 04
    wallet = Wallet(network=DefichainMainnet)
    wallet.from_seed(seed=Vectors.SEED)

    assert Vectors.CRYPTOCURRENCY == wallet.cryptocurrency()
    assert Vectors.SYMBOL == wallet.symbol()
    assert Vectors.NETWORK == wallet.network()
    # assert Vectors.STRENGHT == wallet.strength()
    # assert Vectors.ENTROPY == wallet.entropy()
    # assert Vectors.MNEMONIC == wallet.mnemonic()
    # assert Vectors.LANGUAGE == wallet.language()
    assert None is wallet.passphrase()
    assert Vectors.SEED == wallet.seed()
    assert Vectors.ROOT_xPRIVATE_KEY == wallet.root_xprivate_key()
    assert Vectors.ROOT_xPUBLIC_KEY == wallet.root_xpublic_key()
    assert Vectors.UNCOMPRESSED_1 == wallet.uncompressed()
    assert Vectors.COMPRESSED_1 == wallet.compressed()
    assert Vectors.CHAIN_CODE_1 == wallet.chain_code()
    assert Vectors.PRIVATE_1_KEY == wallet.private_key()
    assert Vectors.PUBLIC_1_KEY == wallet.public_key()
    assert Vectors.WIF_1_KEY == wallet.wif()
    assert Vectors.FINGER_PRINT_1 == wallet.finger_print()
    assert Vectors.SEMANTIC == wallet.semantic()
    assert Vectors.PATH_1 == wallet.path()
    assert Vectors.HASH_1 == wallet.hash()
    assert Vectors.DEFAULT_1_ADDRESS == wallet.default_address()
    assert Vectors.BECH32_1_ADDRESS == wallet.bech32_address()
    assert Vectors.LEGACY_1_ADDRESS == wallet.legacy_address()


@pytest.mark.hdwallet
def test_from_xprivate_key():  # 05
    wallet = Wallet(network=DefichainMainnet)
    wallet.from_xprivate_key(xprivate_key=Vectors.ROOT_xPRIVATE_KEY)

    assert Vectors.CRYPTOCURRENCY == wallet.cryptocurrency()
    assert Vectors.SYMBOL == wallet.symbol()
    assert Vectors.NETWORK == wallet.network()
    # assert Vectors.STRENGHT == wallet.strength()
    # assert Vectors.ENTROPY == wallet.entropy()
    # assert Vectors.MNEMONIC == wallet.mnemonic()
    # assert Vectors.LANGUAGE == wallet.language()
    assert None is wallet.passphrase()
    # assert Vectors.SEED == wallet.seed()
    assert Vectors.ROOT_xPRIVATE_KEY == wallet.root_xprivate_key()
    assert Vectors.ROOT_xPUBLIC_KEY == wallet.root_xpublic_key()
    assert Vectors.UNCOMPRESSED_1 == wallet.uncompressed()
    assert Vectors.COMPRESSED_1 == wallet.compressed()
    assert Vectors.CHAIN_CODE_1 == wallet.chain_code()
    assert Vectors.PRIVATE_1_KEY == wallet.private_key()
    assert Vectors.PUBLIC_1_KEY == wallet.public_key()
    assert Vectors.WIF_1_KEY == wallet.wif()
    assert Vectors.FINGER_PRINT_1 == wallet.finger_print()
    assert Vectors.SEMANTIC == wallet.semantic()
    assert Vectors.PATH_1 == wallet.path()
    assert Vectors.HASH_1 == wallet.hash()
    assert Vectors.DEFAULT_1_ADDRESS == wallet.default_address()
    assert Vectors.BECH32_1_ADDRESS == wallet.bech32_address()
    assert Vectors.LEGACY_1_ADDRESS == wallet.legacy_address()


@pytest.mark.hdwallet
def test_from_xpublic_key():  # 06
    wallet = Wallet(network=DefichainMainnet)
    wallet.from_xpublic_key(xpublic_key=Vectors.ROOT_xPUBLIC_KEY)

    assert Vectors.CRYPTOCURRENCY == wallet.cryptocurrency()
    assert Vectors.SYMBOL == wallet.symbol()
    assert Vectors.NETWORK == wallet.network()
    # assert Vectors.STRENGHT == wallet.strength()
    # assert Vectors.ENTROPY == wallet.entropy()
    # assert Vectors.MNEMONIC == wallet.mnemonic()
    # assert Vectors.LANGUAGE == wallet.language()
    assert None is wallet.passphrase()
    # assert Vectors.SEED == wallet.seed()
    # assert Vectors.ROOT_xPRIVATE_KEY == wallet.root_xprivate_key()
    assert Vectors.ROOT_xPUBLIC_KEY == wallet.root_xpublic_key()
    assert Vectors.UNCOMPRESSED_1 == wallet.uncompressed()
    assert Vectors.COMPRESSED_1 == wallet.compressed()
    assert Vectors.CHAIN_CODE_1 == wallet.chain_code()
    # assert Vectors.PRIVATE_1_KEY == wallet.private_key()
    assert Vectors.PUBLIC_1_KEY == wallet.public_key()
    # assert Vectors.WIF_1_KEY == wallet.wif()
    assert Vectors.FINGER_PRINT_1 == wallet.finger_print()
    assert Vectors.SEMANTIC == wallet.semantic()
    assert Vectors.PATH_1 == wallet.path()
    assert Vectors.HASH_1 == wallet.hash()
    assert Vectors.DEFAULT_1_ADDRESS == wallet.default_address()
    assert Vectors.BECH32_1_ADDRESS == wallet.bech32_address()
    assert Vectors.LEGACY_1_ADDRESS == wallet.legacy_address()


@pytest.mark.hdwallet
def test_from_wif():  # 07
    wallet = Wallet(network=DefichainMainnet)
    wallet.from_wif(Vectors.WIF_1_KEY)

    assert Vectors.CRYPTOCURRENCY == wallet.cryptocurrency()
    assert Vectors.SYMBOL == wallet.symbol()
    assert Vectors.NETWORK == wallet.network()
    # assert Vectors.STRENGHT == wallet.strength()
    # assert Vectors.ENTROPY == wallet.entropy()
    # assert Vectors.MNEMONIC == wallet.mnemonic()
    # assert Vectors.LANGUAGE == wallet.language()
    assert None is wallet.passphrase()
    # assert Vectors.SEED == wallet.seed()
    # assert Vectors.ROOT_xPRIVATE_KEY == wallet.root_xprivate_key()
    # assert Vectors.ROOT_xPUBLIC_KEY == wallet.root_xpublic_key()
    assert Vectors.UNCOMPRESSED_1 == wallet.uncompressed()
    assert Vectors.COMPRESSED_1 == wallet.compressed()
    # assert Vectors.CHAIN_CODE_1 == wallet.chain_code()
    assert Vectors.PRIVATE_1_KEY == wallet.private_key()
    assert Vectors.PUBLIC_1_KEY == wallet.public_key()
    assert Vectors.WIF_1_KEY == wallet.wif()
    assert Vectors.FINGER_PRINT_1 == wallet.finger_print()
    # assert Vectors.SEMANTIC == wallet.semantic()
    # assert Vectors.PATH_1 == wallet.path()
    assert Vectors.HASH_1 == wallet.hash()
    assert Vectors.DEFAULT_1_ADDRESS == wallet.default_address()
    assert Vectors.BECH32_1_ADDRESS == wallet.bech32_address()
    assert Vectors.LEGACY_1_ADDRESS == wallet.legacy_address()


@pytest.mark.hdwallet
def test_from_private_key():  # 08
    wallet = Wallet(network=DefichainMainnet)
    wallet.from_private_key(private_key=Vectors.PRIVATE_1_KEY)

    assert Vectors.CRYPTOCURRENCY == wallet.cryptocurrency()
    assert Vectors.SYMBOL == wallet.symbol()
    assert Vectors.NETWORK == wallet.network()
    # assert Vectors.STRENGHT == wallet.strength()
    # assert Vectors.ENTROPY == wallet.entropy()
    # assert Vectors.MNEMONIC == wallet.mnemonic()
    # assert Vectors.LANGUAGE == wallet.language()
    assert None is wallet.passphrase()
    # assert Vectors.SEED == wallet.seed()
    # assert Vectors.ROOT_xPRIVATE_KEY == wallet.root_xprivate_key()
    # assert Vectors.ROOT_xPUBLIC_KEY == wallet.root_xpublic_key()
    assert Vectors.UNCOMPRESSED_1 == wallet.uncompressed()
    assert Vectors.COMPRESSED_1 == wallet.compressed()
    # assert Vectors.CHAIN_CODE_1 == wallet.chain_code()
    assert Vectors.PRIVATE_1_KEY == wallet.private_key()
    assert Vectors.PUBLIC_1_KEY == wallet.public_key()
    assert Vectors.WIF_1_KEY == wallet.wif()
    assert Vectors.FINGER_PRINT_1 == wallet.finger_print()
    # assert Vectors.SEMANTIC == wallet.semantic()
    # assert Vectors.PATH_1 == wallet.path()
    assert Vectors.HASH_1 == wallet.hash()
    assert Vectors.DEFAULT_1_ADDRESS == wallet.default_address()
    assert Vectors.BECH32_1_ADDRESS == wallet.bech32_address()
    assert Vectors.LEGACY_1_ADDRESS == wallet.legacy_address()


@pytest.mark.hdwallet
def test_from_public_key():  # 09
    wallet = Wallet(network=DefichainMainnet)
    wallet.from_public_key(public_key=Vectors.PUBLIC_1_KEY)

    assert Vectors.CRYPTOCURRENCY == wallet.cryptocurrency()
    assert Vectors.SYMBOL == wallet.symbol()
    assert Vectors.NETWORK == wallet.network()
    # assert Vectors.STRENGHT == wallet.strength()
    # assert Vectors.ENTROPY == wallet.entropy()
    # assert Vectors.MNEMONIC == wallet.mnemonic()
    # assert Vectors.LANGUAGE == wallet.language()
    assert None is wallet.passphrase()
    # assert Vectors.SEED == wallet.seed()
    # assert Vectors.ROOT_xPRIVATE_KEY == wallet.root_xprivate_key()
    # assert Vectors.ROOT_xPUBLIC_KEY == wallet.root_xpublic_key()
    assert Vectors.UNCOMPRESSED_1 == wallet.uncompressed()
    assert Vectors.COMPRESSED_1 == wallet.compressed()
    # assert Vectors.CHAIN_CODE_1 == wallet.chain_code()
    # assert Vectors.PRIVATE_1_KEY == wallet.private_key()
    assert Vectors.PUBLIC_1_KEY == wallet.public_key()
    # assert Vectors.WIF_1_KEY == wallet.wif()
    assert Vectors.FINGER_PRINT_1 == wallet.finger_print()
    # assert Vectors.SEMANTIC == wallet.semantic()
    # assert Vectors.PATH_1 == wallet.path()
    assert Vectors.HASH_1 == wallet.hash()
    assert Vectors.DEFAULT_1_ADDRESS == wallet.default_address()
    assert Vectors.BECH32_1_ADDRESS == wallet.bech32_address()
    assert Vectors.LEGACY_1_ADDRESS == wallet.legacy_address()


@pytest.mark.hdwallet
def test_from_path():  # 10
    wallet = Wallet(network=DefichainMainnet)
    wallet.from_entropy(entropy=Vectors.ENTROPY)

    assert Vectors.CRYPTOCURRENCY == wallet.cryptocurrency()
    assert Vectors.SYMBOL == wallet.symbol()
    assert Vectors.NETWORK == wallet.network()
    assert Vectors.STRENGHT == wallet.strength()
    assert Vectors.ENTROPY == wallet.entropy()
    assert Vectors.MNEMONIC == wallet.mnemonic()
    assert Vectors.LANGUAGE == wallet.language()
    assert None is wallet.passphrase()
    assert Vectors.SEED == wallet.seed()
    assert Vectors.ROOT_xPRIVATE_KEY == wallet.root_xprivate_key()
    assert Vectors.ROOT_xPUBLIC_KEY == wallet.root_xpublic_key()
    assert Vectors.UNCOMPRESSED_1 == wallet.uncompressed()
    assert Vectors.COMPRESSED_1 == wallet.compressed()
    assert Vectors.CHAIN_CODE_1 == wallet.chain_code()
    assert Vectors.PRIVATE_1_KEY == wallet.private_key()
    assert Vectors.PUBLIC_1_KEY == wallet.public_key()
    assert Vectors.WIF_1_KEY == wallet.wif()
    assert Vectors.FINGER_PRINT_1 == wallet.finger_print()
    assert Vectors.SEMANTIC == wallet.semantic()
    assert Vectors.PATH_1 == wallet.path()
    assert Vectors.HASH_1 == wallet.hash()
    assert Vectors.DEFAULT_1_ADDRESS == wallet.default_address()
    assert Vectors.BECH32_1_ADDRESS == wallet.bech32_address()
    assert Vectors.LEGACY_1_ADDRESS == wallet.legacy_address()

    wallet.from_path("m/1129/0/0/1")

    assert Vectors.CRYPTOCURRENCY == wallet.cryptocurrency()
    assert Vectors.SYMBOL == wallet.symbol()
    assert Vectors.NETWORK == wallet.network()
    assert Vectors.STRENGHT == wallet.strength()
    assert Vectors.ENTROPY == wallet.entropy()
    assert Vectors.MNEMONIC == wallet.mnemonic()
    assert Vectors.LANGUAGE == wallet.language()
    assert None is wallet.passphrase()
    assert Vectors.SEED == wallet.seed()
    assert Vectors.ROOT_xPRIVATE_KEY == wallet.root_xprivate_key()
    assert Vectors.ROOT_xPUBLIC_KEY == wallet.root_xpublic_key()
    assert Vectors.UNCOMPRESSED_2 == wallet.uncompressed()
    assert Vectors.COMPRESSED_2 == wallet.compressed()
    assert Vectors.CHAIN_CODE_2 == wallet.chain_code()
    assert Vectors.PRIVATE_2_KEY == wallet.private_key()
    assert Vectors.PUBLIC_2_KEY == wallet.public_key()
    assert Vectors.WIF_2_KEY == wallet.wif()
    assert Vectors.FINGER_PRINT_2 == wallet.finger_print()
    assert Vectors.SEMANTIC == wallet.semantic()
    assert Vectors.PATH_2 == wallet.path()
    assert Vectors.HASH_2 == wallet.hash()
    assert Vectors.DEFAULT_2_ADDRESS == wallet.default_address()
    assert Vectors.BECH32_2_ADDRESS == wallet.bech32_address()
    assert Vectors.LEGACY_2_ADDRESS == wallet.legacy_address()


@pytest.mark.hdwallet
def test_from_index():  # 11
    wallet = Wallet(network=DefichainMainnet)
    wallet.from_entropy(entropy=Vectors.ENTROPY)

    assert Vectors.CRYPTOCURRENCY == wallet.cryptocurrency()
    assert Vectors.SYMBOL == wallet.symbol()
    assert Vectors.NETWORK == wallet.network()
    assert Vectors.STRENGHT == wallet.strength()
    assert Vectors.ENTROPY == wallet.entropy()
    assert Vectors.MNEMONIC == wallet.mnemonic()
    assert Vectors.LANGUAGE == wallet.language()
    assert None is wallet.passphrase()
    assert Vectors.SEED == wallet.seed()
    assert Vectors.ROOT_xPRIVATE_KEY == wallet.root_xprivate_key()
    assert Vectors.ROOT_xPUBLIC_KEY == wallet.root_xpublic_key()
    assert Vectors.UNCOMPRESSED_1 == wallet.uncompressed()
    assert Vectors.COMPRESSED_1 == wallet.compressed()
    assert Vectors.CHAIN_CODE_1 == wallet.chain_code()
    assert Vectors.PRIVATE_1_KEY == wallet.private_key()
    assert Vectors.PUBLIC_1_KEY == wallet.public_key()
    assert Vectors.WIF_1_KEY == wallet.wif()
    assert Vectors.FINGER_PRINT_1 == wallet.finger_print()
    assert Vectors.SEMANTIC == wallet.semantic()
    assert Vectors.PATH_1 == wallet.path()
    assert Vectors.HASH_1 == wallet.hash()
    assert Vectors.DEFAULT_1_ADDRESS == wallet.default_address()
    assert Vectors.BECH32_1_ADDRESS == wallet.bech32_address()
    assert Vectors.LEGACY_1_ADDRESS == wallet.legacy_address()

    wallet.clean_derivation()
    wallet.from_index(index=1129)
    wallet.from_index(index=0)
    wallet.from_index(index=0)
    wallet.from_index(index=1)

    assert Vectors.CRYPTOCURRENCY == wallet.cryptocurrency()
    assert Vectors.SYMBOL == wallet.symbol()
    assert Vectors.NETWORK == wallet.network()
    assert Vectors.STRENGHT == wallet.strength()
    assert Vectors.ENTROPY == wallet.entropy()
    assert Vectors.MNEMONIC == wallet.mnemonic()
    assert Vectors.LANGUAGE == wallet.language()
    assert None is wallet.passphrase()
    assert Vectors.SEED == wallet.seed()
    assert Vectors.ROOT_xPRIVATE_KEY == wallet.root_xprivate_key()
    assert Vectors.ROOT_xPUBLIC_KEY == wallet.root_xpublic_key()
    assert Vectors.UNCOMPRESSED_2 == wallet.uncompressed()
    assert Vectors.COMPRESSED_2 == wallet.compressed()
    assert Vectors.CHAIN_CODE_2 == wallet.chain_code()
    assert Vectors.PRIVATE_2_KEY == wallet.private_key()
    assert Vectors.PUBLIC_2_KEY == wallet.public_key()
    assert Vectors.WIF_2_KEY == wallet.wif()
    assert Vectors.FINGER_PRINT_2 == wallet.finger_print()
    assert Vectors.SEMANTIC == wallet.semantic()
    assert Vectors.PATH_2 == wallet.path()
    assert Vectors.HASH_2 == wallet.hash()
    assert Vectors.DEFAULT_2_ADDRESS == wallet.default_address()
    assert Vectors.BECH32_2_ADDRESS == wallet.bech32_address()
    assert Vectors.LEGACY_2_ADDRESS == wallet.legacy_address()


@pytest.mark.hdwallet
def test_wallet_with_passphrase():  # 12
    wallet = Wallet(network=DefichainMainnet)
    wallet.from_entropy(entropy=Vectors.ENTROPY, passphrase=Vectors.PASSPHRASE)

    assert Vectors.CRYPTOCURRENCY == wallet.cryptocurrency()
    assert Vectors.SYMBOL == wallet.symbol()
    assert Vectors.NETWORK == wallet.network()
    assert Vectors.STRENGHT == wallet.strength()
    assert Vectors.ENTROPY == wallet.entropy()
    assert Vectors.MNEMONIC == wallet.mnemonic()
    assert Vectors.LANGUAGE == wallet.language()
    assert Vectors.PASSPHRASE is wallet.passphrase()
    assert Vectors.SEED_PASSPHRASE == wallet.seed()
    assert Vectors.ROOT_xPRIVATE_KEY_PASSPHRASE == wallet.root_xprivate_key()
    assert Vectors.ROOT_xPUBLIC_KEY_PASSPHRASE == wallet.root_xpublic_key()
    assert Vectors.UNCOMPRESSED_PASSPHRASE == wallet.uncompressed()
    assert Vectors.COMPRESSED_PASSPHRASE == wallet.compressed()
    assert Vectors.CHAIN_CODE_PASSPHRASE == wallet.chain_code()
    assert Vectors.PRIVATE_PASSPHRASE_KEY == wallet.private_key()
    assert Vectors.PUBLIC_PASSPHRASE_KEY == wallet.public_key()
    assert Vectors.WIF_PASSPHRASE_KEY == wallet.wif()
    assert Vectors.FINGER_PRINT_PASSPHRASE == wallet.finger_print()
    assert Vectors.SEMANTIC == wallet.semantic()
    assert Vectors.PATH_1 == wallet.path()
    assert Vectors.HASH_PASSPHRASE == wallet.hash()
    assert Vectors.DEFAULT_PASSPHRASE_ADDRESS == wallet.default_address()
    assert Vectors.BECH32_PASSPHRASE_ADDRESS == wallet.bech32_address()
    assert Vectors.LEGACY_PASSPHRASE_ADDRESS == wallet.legacy_address()


@pytest.mark.hdwallet
def test_query_all_correct_data():  # 13
    wallet = Wallet(network=DefichainMainnet)
    wallet.from_entropy(entropy=Vectors.ENTROPY)

    assert Vectors.CRYPTOCURRENCY == wallet.cryptocurrency()
    assert Vectors.SYMBOL == wallet.symbol()
    assert Vectors.NETWORK == wallet.network()
    assert Vectors.STRENGHT == wallet.strength()
    assert Vectors.ENTROPY == wallet.entropy()
    assert Vectors.MNEMONIC == wallet.mnemonic()
    assert Vectors.LANGUAGE == wallet.language()
    assert None is wallet.passphrase()
    assert Vectors.SEED == wallet.seed()
    assert Vectors.ROOT_xPRIVATE_KEY == wallet.root_xprivate_key(encoded=True)
    assert Vectors.ROOT_xPUBLIC_KEY == wallet.root_xpublic_key(encoded=True)
    assert Vectors.UNCOMPRESSED_1 == wallet.uncompressed(compressed=wallet.compressed())
    assert Vectors.COMPRESSED_1 == wallet.compressed(uncompressed=wallet.uncompressed())
    assert Vectors.CHAIN_CODE_1 == wallet.chain_code()
    assert Vectors.PRIVATE_1_KEY == wallet.private_key()
    assert Vectors.PUBLIC_1_KEY == wallet.public_key(compressed=True, private_key=wallet.private_key())
    assert Vectors.WIF_1_KEY == wallet.wif()
    assert Vectors.FINGER_PRINT_1 == wallet.finger_print()
    assert Vectors.SEMANTIC == wallet.semantic()
    assert Vectors.PATH_1 == wallet.path()
    assert Vectors.HASH_1 == wallet.hash()
    assert Vectors.DEFAULT_1_ADDRESS == wallet.default_address()
    assert Vectors.BECH32_1_ADDRESS == wallet.bech32_address()
    assert Vectors.LEGACY_1_ADDRESS == wallet.legacy_address()
