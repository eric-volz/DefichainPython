import pytest
from . import ocean


@pytest.mark.query
def test_get():  # 01
    assert ocean.stats.get()


@pytest.mark.query
def test_RewardDistributiong():  # 02
    assert ocean.stats.getRewardDistribution()


@pytest.mark.query
def test_getSupply():  # 03
    assert ocean.stats.getSupply()


@pytest.mark.query
def test_getBurn():  # 04
    assert ocean.stats.getBurn()
