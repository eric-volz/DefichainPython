import pytest
import time
from tests.util import createNode, load_secrets_conf

# Import Exceptions
from defichain.exceptions.http.InternalServerError import InternalServerError

node = createNode()
address = load_secrets_conf()["wallet_address"]
vault = load_secrets_conf()["vault_address"]


@pytest.mark.transactions
def test_addpoolliquidity():  # 01
    while len(node.wallet.listunspent()) < 1:
        time.sleep(1)

    dusd_pool = node.poolpair.getpoolpair(17)
    reserveA = dusd_pool["17"]["reserveA"]
    reserveB = dusd_pool["17"]["reserveB"]
    price = round(reserveA / reserveB, 8)

    dfi = 0.000001
    duds = round(dfi * price, 8)
    _from = {address: [f"{dfi}@DFI", f"{duds}@DUSD"]}
    assert node.poolpair.addpoolliquidity(_from, address)
    assert node.poolpair.addpoolliquidity(_from, address, [])
    assert node.poolpair.addpoolliquidity(_from=_from, shareAddress=address, inputs=[])


@pytest.mark.transactions
def test_compositeswap():  # 02
    while len(node.wallet.listunspent()) < 1:
        time.sleep(1)

    assert node.poolpair.compositeswap(address, "DFI", 0.00000001, address, "DUSD")
    assert node.poolpair.compositeswap(address, "DFI", 0.00000001, address, "DUSD", 2, [])
    assert node.poolpair.compositeswap(_from=address, tokenFrom="DFI", amountFrom=0.00000001, to=address,
                                       tokenTo="DUSD", maxPrice=2, inputs=[])


@pytest.mark.query
def test_createpoolpair():  # 03
    string = ".* RPC_INVALID_ADDRESS_OR_KEY: Need foundation member authorization"
    with pytest.raises(InternalServerError, match=string):
        assert node.poolpair.createpoolpair("USDT", "USDC", 0.1, True, address)
    with pytest.raises(InternalServerError, match=string):
        assert node.poolpair.createpoolpair("USDT", "USDC", 0.1, True, address, 10, "USDT-USDC")
    with pytest.raises(InternalServerError, match=string):
        assert node.poolpair.createpoolpair(tokenA="USDT", tokenB="USDC", commission=0.1, status=True,
                                            ownerAddress=address, customRewards=10, pairSymbol="USDT-USDC")


@pytest.mark.query
def test_getpoolpair():  # 04
    key = 17  # DUSD
    assert node.poolpair.getpoolpair(key)
    assert node.poolpair.getpoolpair(key, True)
    assert node.poolpair.getpoolpair(key=key, verbose=False)


@pytest.mark.query
def test_listpoolpairs():  # 05
    assert node.poolpair.listpoolpairs()
    assert node.poolpair.listpoolpairs(0, True, 100, True)
    assert node.poolpair.listpoolpairs(start=0, including_start=True, limit=100, verbose=True)


@pytest.mark.query
def test_listpoolshares():  # 06
    assert node.poolpair.listpoolshares()
    assert node.poolpair.listpoolshares(0, True, 100, True, False)
    assert node.poolpair.listpoolshares(start=0, including_start=True, limit=100, verbose=True, is_mine_only=False)


@pytest.mark.transactions
def test_poolswap():  # 07
    while len(node.wallet.listunspent()) < 1:
        time.sleep(1)

    assert node.poolpair.poolswap(address, "DFI", 0.00000001, address, "DUSD")
    assert node.poolpair.poolswap(address, "DFI", 0.00000001, address, "DUSD", 2, [])
    assert node.poolpair.poolswap(_from=address, tokenFrom="DFI", amountFrom=0.00000001, to=address,
                                  tokenTo="DUSD", maxPrice=2, inputs=[])


@pytest.mark.transactions
def test_removepoolliquidityy():  # 08
    while len(node.wallet.listunspent()) < 1:
        time.sleep(1)

    assert node.poolpair.removepoolliquidity(address, "0.00000001@DUSD-DFI")
    assert node.poolpair.removepoolliquidity(address, "0.00000001@DUSD-DFI", [])
    assert node.poolpair.removepoolliquidity(_from=address, amount="0.00000001@DUSD-DFI", inputs=[])


@pytest.mark.query
def test_testpoolswap():  # 09
    assert node.poolpair.testpoolswap(address, "DFI", 0.00000001, address, "DUSD")
    assert node.poolpair.testpoolswap(address, "DFI", 0.00000001, address, "DUSD", 2, "direct", True)
    assert node.poolpair.testpoolswap(_from=address, tokenFrom="DFI", amountFrom=0.00000001, to=address, tokenTo="DUSD",
                                      maxPrice=2, path="direct", verbose=True)


@pytest.mark.query
def test_updatepoolpair():  # 10
    string = ".* RPC_INVALID_ADDRESS_OR_KEY: Need foundation member authorization"
    with pytest.raises(InternalServerError, match=string):
        assert node.poolpair.updatepoolpair('DUSD-DFI')
    with pytest.raises(InternalServerError, match=string):
        assert node.poolpair.updatepoolpair('DUSD-DFI', True, 0.5, address, 100, [])
    with pytest.raises(InternalServerError, match=string):
        assert node.poolpair.updatepoolpair(pool='DUSD-DFI', status=True, commission=0.5, ownerAddress=address,
                                            customRewards=100, inputs=[])

