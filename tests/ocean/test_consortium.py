import pytest
from . import ocean
from defichain.exceptions.http.NotFound import NotFound


@pytest.mark.query
def test_getAssetBreakdown():  # 01
    assert ocean.consortium.getAssetBreakdown()


@pytest.mark.query
def test_getMemberStats():  # 02
    string = "Consortium member not found"
    memberId = "member"
    with pytest.raises(NotFound, match=string):
        assert ocean.consortium.getMemberStats(memberId)
        assert ocean.consortium.getMemberStats(memberId=memberId)
