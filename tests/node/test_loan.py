import pytest
import time
from tests.util import load_secrets_conf

# Import Exceptions
from defichain.exceptions.http.InternalServerError import InternalServerError
from defichain.exceptions.http.BadRequest import BadRequest

from . import node
address = load_secrets_conf()["wallet_address"]
vault = load_secrets_conf()["vault_address"]


@pytest.mark.tx
def test_createloanscheme():  # 01
    while len(node.wallet.listunspent()) < 3:
        time.sleep(1)

    string = ".* RPC_INVALID_REQUEST: Test LoanSchemeTx execution failed:\ntx not from foundation member!"
    with pytest.raises(BadRequest, match=string):
        assert node.loan.createloanscheme(100, 10, "MIN100")
    with pytest.raises(BadRequest, match=string):
        assert node.loan.createloanscheme(100, 10, "MIN100", [])
    with pytest.raises(BadRequest, match=string):
        assert node.loan.createloanscheme(mincolratio=100, interestrate=10, id="MIN100", inputs=[])


@pytest.mark.tx
def test_destroyloanscheme():  # 02
    while len(node.wallet.listunspent()) < 3:
        time.sleep(1)

    string = ".* RPC_INVALID_REQUEST: Test DestroyLoanSchemeTx execution failed:\ntx not from foundation member!"
    with pytest.raises(BadRequest, match=string):
        assert node.loan.destroyloanscheme("MIN100")
    with pytest.raises(BadRequest, match=string):
        assert node.loan.destroyloanscheme("MIN100", node.blockchain.getblockcount() + 10, [])
    with pytest.raises(BadRequest, match=string):
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


@pytest.mark.query
def test_listloanschemes():  # 09
    assert node.loan.listloanschemes()


@pytest.mark.query
def test_listloantokens():  # 10
    assert node.loan.listloantokens()


@pytest.mark.tx
def test_paybackloan():  # 11
    while len(node.wallet.listunspent()) < 3:
        time.sleep(1)

    amounts = ["0.00000001@SPY", "0.00000001@SPY"]
    loans = [{"dToken": "SPY", "amounts": "0.00000001@SPY"}]
    assert node.loan.paybackloan(vault, address, amounts)
    assert node.loan.paybackloan(vaultId=vault, _from=address, amounts=amounts)
    assert node.loan.paybackloan(vault, address, None, loans)
    assert node.loan.paybackloan(vaultId=vault, _from=address, loans=loans)


@pytest.mark.query
def test_setcollateraltoken():  # 12
    string = ".* RPC_INVALID_PARAMETER: Token TEST does not exist!"
    with pytest.raises(InternalServerError, match=string):
        assert node.loan.setcollateraltoken("TEST", 150, "TEST/USD")
    with pytest.raises(InternalServerError, match=string):
        assert node.loan.setcollateraltoken("TEST", 150, "TEST/USD", node.blockchain.getblockcount()+1, [])
    with pytest.raises(InternalServerError, match=string):
        assert node.loan.setcollateraltoken(token="TEST", factor=150, fixedIntervalPriceId="TEST/USD",
                                        activateAfterBlock=node.blockchain.getblockcount()+1, inputs=[])


@pytest.mark.query
def test_setdefaultloanscheme():  # 13
    string = ".* Test DefaultLoanSchemeTx execution failed:"
    with pytest.raises(BadRequest, match=string):
        assert node.loan.setdefaultloanscheme("MIN150")
    with pytest.raises(BadRequest, match=string):
        assert node.loan.setdefaultloanscheme("MIN150", [])
    with pytest.raises(BadRequest, match=string):
        assert node.loan.setdefaultloanscheme(id="MIN150", inputs=[])


@pytest.mark.query
def test_setloantoken():  # 14
    string = ".* RPC_INVALID_REQUEST: Test SetLoanTokenTx execution failed:\ntx not from foundation member!"
    with pytest.raises(BadRequest, match=string):
        assert node.loan.setloantoken("TEST", "TEST/USD")
    with pytest.raises(BadRequest, match=string):
        assert node.loan.setloantoken("TEST", "TEST/USD", "TEST Coin", True, 0, [])
    with pytest.raises(BadRequest, match=string):
        assert node.loan.setloantoken(symbol="TEST", fixedIntervalPriceId="TEST/USD", name="TEST Coin", mintable=True,
                                      interest=0, inputs=[])


@pytest.mark.tx
def test_takeloan():  # 15
    while len(node.wallet.listunspent()) < 3:
        time.sleep(1)

    amounts = ["0.00000002@SPY", "0.00000002@SPY"]
    assert node.loan.takeloan(vault, amounts)
    assert node.loan.takeloan(vault, amounts, address, [])
    assert node.loan.takeloan(vaultId=vault, amounts=amounts, to=address, inputs=[])


@pytest.mark.query
def test_updateloanscheme():  # 16
    string = ".* RPC_INVALID_REQUEST: Test LoanSchemeTx execution failed:\ntx not from foundation member!"
    with pytest.raises(BadRequest, match=string):
        assert node.loan.updateloanscheme(100, 10, "MIN1000")
    with pytest.raises(BadRequest, match=string):
        assert node.loan.updateloanscheme(100, 10, "MIN1000", node.blockchain.getblockcount()+1, [])
    with pytest.raises(BadRequest, match=string):
        assert node.loan.updateloanscheme(mincolratio=100, interestrate=10, id="MIN1000",
                                          ACTIVATE_AFTER_BLOCK=node.blockchain.getblockcount()+1, inputs=[])


@pytest.mark.query
def test_updateloantoken():  # 17
    string = ".* RPC_INVALID_REQUEST: Test UpdateLoanTokenTx execution failed:\ntx not from foundation member!"
    with pytest.raises(BadRequest, match=string):
        assert node.loan.updateloantoken("SPY")
    with pytest.raises(BadRequest, match=string):
        assert node.loan.updateloantoken("SPY", "SPYY", "S&P 500 Index", "SPY/USD", True, 0, [])
    with pytest.raises(BadRequest, match=string):
        assert node.loan.updateloantoken(token="SPY", symbol="SPYY", name="S&P 500 Index",
                                         fixedIntervalPriceId="SPY/USD", mintable=True, interest=0, inputs=[])
