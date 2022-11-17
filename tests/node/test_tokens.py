import pytest
from tests.util import load_secrets_conf

# Import Exceptions
from defichain.exceptions.http.InternalServerError import InternalServerError

from . import node
address = load_secrets_conf()["wallet_address"]


@pytest.mark.query
def test_createtoken():  # 01
    symbol = "FOO"
    collateralAddress = address
    name = "FOO"
    isDat = True
    decimal = 8
    limit = 100
    mintable = True
    tradeable = True
    string = ".* RPC_WALLET_ERROR: Insufficient funds"
    with pytest.raises(InternalServerError, match=string):
        assert node.tokens.createtoken(symbol, collateralAddress)
        assert node.tokens.createtoken(symbol, collateralAddress, name, isDat, decimal, limit, mintable, tradeable, [])
        assert node.tokens.createtoken(symbol=symbol, collateralAddress=collateralAddress, name=name, isDat=isDat,
                                       decimal=decimal, limit=limit, mintable=mintable, tradeable=tradeable, inputs=[])


@pytest.mark.query
def test_decodecustomtx():  # 02
    hexstring = "04000000000101721f42d2a041ad8911b15b1199dee954d0989d493fdfafbab3472edb79dee09f0100000000ffffffff0" \
                "20000000000000000526a4c4f4466547869160014e59d348df62e7710cc79e1f7096ace5b78c23abc024e07da01000000" \
                "00160014e59d348df62e7710cc79e1f7096ace5b78c23abc000000000000000000ae2b0000000000000105007d9398000" \
                "0000000160014e59d348df62e7710cc79e1f7096ace5b78c23abc000247304402203abd70aac9fe1050c57f901782dd8a" \
                "becdb94ef71068089b6492e55d084acb0d02207eebbbd5f14c398152d03765e280f19559a9c9a96729f4249556f381eb8" \
                "beaf9012102cc9ac20cf0b91cc0b2624f1d26f0b1182f0125bdb1a738948a598e7fdccbafaa00000000"

    assert node.tokens.decodecustomtx(hexstring)
    assert node.tokens.decodecustomtx(hexstring, True)
    assert node.tokens.decodecustomtx(hexstring=hexstring, iswitness=True)


@pytest.mark.query
def test_getcustomtx():  # 03
    txid = "fd905b4b1b3da0ad6757cd0d067a6a6a256e3bdcd9f03aa593df2774bdc2a16c"
    blockhash = "a877ee573caf316d64c37141ac3b79d92d00d5aaf0966e2d8a13c321f7a4d534"
    assert node.tokens.getcustomtx(txid, blockhash)
    assert node.tokens.getcustomtx(txid=txid, blockhash=blockhash)


@pytest.mark.query
def test_gettoken():  # 04
    key = 0
    assert node.tokens.gettoken(key)


@pytest.mark.query
def test_listtoken():  # 05
    start = 2
    including_start = True
    limit = 2
    assert node.tokens.listtokens()
    assert node.tokens.listtokens(start, including_start, limit)
    assert node.tokens.listtokens(start=start, including_start=including_start, limit=limit)


@pytest.mark.query
def test_minttokens():  # 06
    token = "SPY"
    amount = 1
    string = ".* RPC_INVALID_ADDRESS_OR_KEY: Incorrect authorization for 8bL7jZe2Nk5EhqFA6yuf8HPre3M6eewkqj"
    with pytest.raises(InternalServerError, match=string):
        assert node.tokens.minttokens(f"{amount}@{token}")
        assert node.tokens.minttokens(f"{amount}@{token}", [])
        assert node.tokens.minttokens(amounts=f"{amount}@{token}", inputs=[])


@pytest.mark.query
def test_updatetoken():  # 07
    token = "SPY"
    symbol = "SPY"
    name = "SPY"
    isDAT = False
    mintable = True
    tradeable = True
    finalize = True
    string = ".* RPC_INVALID_ADDRESS_OR_KEY: Need foundation member authorization"
    with pytest.raises(InternalServerError, match=string):
        assert node.tokens.updatetoken(token)
        assert node.tokens.updatetoken(token, symbol, name, isDAT, mintable, tradeable, finalize, [])
        assert node.tokens.updatetoken(token=token, symbol=symbol, isDAT=isDAT, mintable=mintable,
                                       tradeable=tradeable, finalize=finalize, inputs=[])
