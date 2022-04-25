import os
from os import path
from defichain import Node


def load_secrets_conf():
    if not path.isfile("secrets_conf.py"):
        print(os.listdir())
        raise Exception("There is not secrets_conf.py File: \n"
                        "To create one: read secrets_conf.example.py!")

    from tests.secrets_conf import USER, PASSWORD, URL, PORT
    json = {"user": USER, "password": PASSWORD, "url": URL, "port": PORT}

    try:
        from tests.secrets_conf import WALLET_PATH
        json.update({"wallet_path": WALLET_PATH})
    except:
        pass
    return json


def createNode():
    secrets = load_secrets_conf()

    if "wallet_path" in secrets:
        return Node(user=secrets["user"], password=secrets["password"], url=secrets["url"], port=secrets["port"],
                    wallet_path=secrets["wallet_path"])
    return Node(user=secrets["user"], password=secrets["password"], url=secrets["url"], port=secrets["port"])
