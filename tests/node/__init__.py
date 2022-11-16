from defichain import Node
from defichain.logger import Logger
from ..util import load_secrets_conf

secrets = load_secrets_conf()
logger = Logger(log_level="all")

node = Node(user=secrets["user"], password=secrets["password"], url=secrets["url"], port=secrets["port"],
            wallet_name=secrets["wallet_name"], wallet_password=secrets["wallet_password"], wallet_timeout=3600,
            logger=logger)
