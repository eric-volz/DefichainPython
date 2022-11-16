import pytest
from . import ocean


@pytest.mark.query
def test_estimate():  # 01
    assert ocean.fee.estimate(10)
    assert ocean.fee.estimate(confirmationTarget=10)