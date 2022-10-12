import pytest
from defichain.hdwallet.utils import *

ENTROPY = "ee535b143b0d9d1f87546f9df0d06b1a"
MNEMONIC = "unusual onion shallow invite supply more bubble mistake over make bracket cry"


@pytest.mark.hdwallet
def test_generate_passphrase():  # 01
    assert len(generate_passphrase(length=32)) == 32


@pytest.mark.hdwallet
def test_generate_entropy():  # 02
    assert get_entropy_strength(generate_entropy(strength=256)) == 256


@pytest.mark.hdwallet
def test_generate_mnemonic():  # 03
    assert len(generate_mnemonic(language="english", strength=256).split(" ")) == 24


@pytest.mark.hdwallet
def test_is_entropy():  # 04
    assert is_entropy(entropy=ENTROPY) is True


@pytest.mark.hdwallet
def test_is_mnemonic():  # 05
    assert is_mnemonic(mnemonic=MNEMONIC, language="english") is True


@pytest.mark.hdwallet
def test_get_entropy_strength():  # 06
    assert get_entropy_strength(entropy=ENTROPY) == 128


@pytest.mark.hdwallet
def test_get_mnemonic_language():  # 07
    assert get_mnemonic_language(mnemonic=MNEMONIC) == "english"


@pytest.mark.hdwallet
def test_entropy_to_mnemonic():  # 08
    assert entropy_to_mnemonic(ENTROPY, language="english") == MNEMONIC


@pytest.mark.hdwallet
def test_mnemonic_to_entropy():  # 09
    assert mnemonic_to_entropy(mnemonic=MNEMONIC, language="english") == ENTROPY


