from os import path
from defichain import Node
from defichain.logger import Logger

LENGTH_OF_TXID = 64


def load_secrets_conf():
    # Check if file exists
    if not path.isfile("secrets_conf.py"):
        raise Exception("There is not secrets_conf.py File: \n"
                        "To create one: read secrets_conf.example.py!")

    # load mandatory config
    from tests.secrets_conf import USER, PASSWORD, URL, PORT, WALLET_ADDRESS, VAULT_ADDRESS, WALLET_NAME, WALLET_PASSWORD
    json = {"user": USER, "password": PASSWORD, "url": URL, "port": PORT, "wallet_address": WALLET_ADDRESS,
            "vault_address": VAULT_ADDRESS, "wallet_name": WALLET_NAME, "wallet_password": WALLET_PASSWORD}

    return json
