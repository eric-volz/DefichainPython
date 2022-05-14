from os import path
from defichain import Node

LENGTH_OF_TXID = 64


def load_secrets_conf():
    # Check if file exists
    if not path.isfile("secrets_conf.py"):
        raise Exception("There is not secrets_conf.py File: \n"
                        "To create one: read secrets_conf.example.py!")

    # load mandatory config
    from tests.secrets_conf import USER, PASSWORD, URL, PORT, WALLET_ADDRESS
    json = {"user": USER, "password": PASSWORD, "url": URL, "port": PORT, "wallet_address": WALLET_ADDRESS}

    # load optional config
    try:
        from tests.secrets_conf import WALLET_PATH
        json.update({"wallet_path": WALLET_PATH})
    except:
        pass

    try:
        from tests.secrets_conf import WALLET_PASSWORD
        json.update({"wallet_password": WALLET_PASSWORD})
    except:
        pass

    return json


def createNode():
    secrets = load_secrets_conf()
    if "wallet_path" and "wallet_password" in secrets:
        return Node(user=secrets["user"], password=secrets["password"], url=secrets["url"], port=secrets["port"],
                    wallet_path=secrets["wallet_path"], wallet_password=secrets["wallet_password"])
    elif "wallet_path" in secrets:
        return Node(user=secrets["user"], password=secrets["password"], url=secrets["url"], port=secrets["port"],
                    wallet_path=secrets["wallet_path"])
    elif "wallet_password" in secrets:
        return Node(user=secrets["user"], password=secrets["password"], url=secrets["url"], port=secrets["port"],
                    wallet_password=secrets["wallet_password"])
    return Node(user=secrets["user"], password=secrets["password"], url=secrets["url"], port=secrets["port"])
