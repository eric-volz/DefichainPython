import pytest
from tests.node.util import createNode, load_secrets_conf

# Import Exceptions
from defichain.src.node.exceptions.InternalServerError import InternalServerError

node = createNode()
address = load_secrets_conf()["wallet_address"]


@pytest.mark.query
def test_generatetoaddress():  # 01
    nblocks = 11
    maxtries = 1
    string = ".* RPC_INVALID_ADDRESS_OR_KEY: Error: I am not masternode operator"
    with pytest.raises(InternalServerError, match=string):
        assert node.generating.generatetoaddress(nblocks, address)
        assert node.generating.generatetoaddress(nblocks, address, maxtries)
        assert node.generating.generatetoaddress(nblocks=nblocks, address=address, maxtries=maxtries)
