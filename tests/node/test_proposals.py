import pytest

# Import Exceptions
from defichain.exceptions.http.BadRequest import BadRequest

from . import node


@pytest.mark.query
def test_creategovcfp():  # 01
    pass


@pytest.mark.query
def test_creategovvoc():  # 02
    pass


@pytest.mark.query
def test_getgovproposal():  # 03
    pass


@pytest.mark.query
def test_listgovproposals():  # 04
    pass


@pytest.mark.query
def test_listgovproposalvotes():  # 05
    pass


@pytest.mark.query
def test_votegov():  # 06
    pass
