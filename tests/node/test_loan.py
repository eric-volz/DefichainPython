import pytest
from tests.util import createNode, load_secrets_conf, LENGTH_OF_TXID

# Import Exceptions
from defichain.exceptions.InternalServerError import InternalServerError
from defichain.exceptions.BadRequest import BadRequest

node = createNode()
address = load_secrets_conf()["wallet_address"]
vault = load_secrets_conf()["vault_address"]


@pytest.mark.transactions
def test_createloanscheme():  # 01
    string = ".* RPC_INVALID_ADDRESS_OR_KEY: Need foundation member authorization"
    with pytest.raises(InternalServerError, match=string):
        assert node.loan.createloanscheme(100, 10, "MIN100")
    with pytest.raises(InternalServerError, match=string):
        assert node.loan.createloanscheme(100, 10, "MIN100", [])
    with pytest.raises(InternalServerError, match=string):
        assert node.loan.createloanscheme(mincolratio=100, interestrate=10, id="MIN100", inputs=[])


@pytest.mark.transactions
def test_destroyloanscheme():  # 02
    string = ".* RPC_INVALID_ADDRESS_OR_KEY: Need foundation member authorization"
    with pytest.raises(InternalServerError, match=string):
        assert node.loan.destroyloanscheme("MIN100")
    with pytest.raises(InternalServerError, match=string):
        assert node.loan.destroyloanscheme("MIN100", node.blockchain.getblockcount() + 10, [])
    with pytest.raises(InternalServerError, match=string):
        assert node.loan.destroyloanscheme(id="MIN100", ACTIVATE_AFTER_BLOCK=node.blockchain.getblockcount() + 10,
                                           inputs=[])


@pytest.mark.query
def test_getcollateraltoken():  # 03
    assert node.loan.getcollateraltoken("DFI")
    assert node.loan.getcollateraltoken(token="DFI")


@pytest.mark.query
def test_getinterest():  # 04
    assert node.loan.getinterest("MIN150")
    assert node.loan.getinterest("MIN150", "DUSD")
    assert node.loan.getinterest(id="MIN150", token="DUSD")


@pytest.mark.query
def test_getloaninfo():  # 05
    assert node.loan.getloaninfo()


@pytest.mark.query
def test_getloanscheme():  # 06
    assert node.loan.getloanscheme("MIN150")
    assert node.loan.getloanscheme(id="MIN150")


@pytest.mark.query
def test_getloantoken():  # 07
    assert node.loan.getloantoken("DUSD")
    assert node.loan.getloantoken(token="DUSD")


@pytest.mark.query
def test_listcollateraltokens():  # 08
    assert node.loan.listcollateraltokens()
    assert node.loan.listcollateraltokens(0, True)
    assert node.loan.listcollateraltokens(height=0, all=True)
