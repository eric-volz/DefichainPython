import pytest
from defichain import Ocean

ocean = Ocean()


@pytest.mark.query
def test_estimate():  # 01
    assert ocean.fee.estimate(10)
    assert ocean.fee.estimate(confirmationTarget=10)