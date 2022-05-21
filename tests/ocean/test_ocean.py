import pytest
from defichain import Ocean


@pytest.mark.mandatory
def test_createOcean():
    """
    Checking if the Ocean Object builds as wanted
    """
    assert Ocean()
    assert Ocean("https://ocean.defichain.com", "v0", "mainnet")
    assert Ocean(url="https://ocean.defichain.com", version="v0", network="mainnet")
