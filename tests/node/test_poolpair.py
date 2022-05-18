import pytest
from tests.util import createNode, load_secrets_conf, LENGTH_OF_TXID

# Import Exceptions
from defichain.exceptions.InternalServerError import InternalServerError

node = createNode()
address = load_secrets_conf()["wallet_address"]
vault = load_secrets_conf()["vault_address"]


@pytest.mark.transactions
def test_addpoolliquidity():  # 01
    dusd_pool = node.poolpair.getpoolpair(17)
    reserveA = dusd_pool["17"]["reserveA"]
    reserveB = dusd_pool["17"]["reserveB"]
    price = round(reserveA / reserveB, 8)

    dfi = 0.00000001
    duds = round(dfi * price, 8)
    _from = {address: [f"{dfi}@DFI", f"{duds}@DUSD"]}
    assert node.poolpair.addpoolliquidity(_from, address)
    assert node.poolpair.addpoolliquidity(_from, address, [])
    assert node.poolpair.addpoolliquidity(_from=_from, shareAddress=address, inputs=[])
