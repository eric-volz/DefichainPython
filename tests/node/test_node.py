import pytest
from defichain import Node
from tests.util import load_secrets_conf


secrets = load_secrets_conf()


@pytest.mark.mandatory
def test_createNode():
    """
    Checking if the Node Object builds as wanted
    """
    assert Node(secrets["user"], secrets["password"], secrets["url"], secrets["port"])
    assert Node(user=secrets["user"], password=secrets["password"], url=secrets["url"], port=secrets["port"])
    if "wallet_path" in secrets:
        assert Node(user=secrets["user"], password=secrets["password"], url=secrets["url"], port=secrets["port"],
                    wallet_path=secrets["wallet_path"])
