import pytest

from defichain import Ocean
from defichain.transactions.remotedata import RemoteDataOcean
from defichain.exceptions.http import BadRequest
from . import *

remote = RemoteDataOcean(Ocean())


@pytest.mark.transactions
def test_get_unspent():  # 01
    assert remote.get_unspent(ADDRESS)


@pytest.mark.transactions
def test_check_masternode():  # 02
    assert remote.check_masternode(MASTERNODE)


@pytest.mark.transactions
def test_test_tx():  # 03
    assert remote.test_tx(RAWTX) is False


@pytest.mark.transactions
def test_send_tx():  # 04
    with pytest.raises(BadRequest):
        assert remote.send_tx(RAWTX)
