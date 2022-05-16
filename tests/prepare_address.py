import time

from defichain import Ocean
from tests.util import createNode
from tests.util import load_secrets_conf

"""
This is a script witch prepares your address for the tests of the library
It assumes that your vault is properly setup and all given addresses 
belongs to your wallet

Use a separate wallet to perform the test: this script shifts all UTXOs of the 
wallet to the given address
"""


# static variables
UTXO_MIN_AMOUNT = 0.5
UTXO_MAX_AMOUNT = 2
DUSD_AMOUNT = 0.1
DFI_AMOUNT = 0.01
VAULT_MIN_RATIO = 400

node = createNode()
ocean = Ocean()
ADDRESS = load_secrets_conf()["wallet_address"]
VAULT = load_secrets_conf()["vault_address"]

# All needed functions
def check_min_and_max_utxo():
    balance = float(node.wallet.getbalances()["mine"]["trusted"])
    if balance < UTXO_MIN_AMOUNT:
        raise Exception(f"You have less then the minimum required UTXO on your wallet: {balance}UTXO\n"
                        f"Please fill it up")
    elif balance >= UTXO_MAX_AMOUNT:
        print(f"You have more than the maximum allowed {UTXO_MAX_AMOUNT} UTXO on your Wallet: \n"
              f"{UTXO_MAX_AMOUNT - balance - 0.5} will be converted to DFI Tokens")
    print(f"You are good with UTXOs: {balance}")


def check_vault_ratio():
    vault = ocean.loan.getVault(VAULT)
    ratio = float(vault["data"]["collateralRatio"])
    if ratio < VAULT_MIN_RATIO:
        raise Exception(f"Please fill up your vault collateral it is below the specified minimum ratio of "
                        f"{VAULT_MIN_RATIO}%: it is at {ratio}")
    else:
        print(f"Your vault is good with a ratio of: {ratio}")


def all_utxo_to_address():
    addresses = node.wallet.listaddressgroupings()
    for address in addresses[0]:
        if address[0] != ADDRESS and address[1] > 0.00001:
            node.accounts.sendutxosfrom(address[0], ADDRESS, address[1] - 0.00001)
            print(f"Send {address[1]}UTXO from {address[0]} to {ADDRESS}")


def check_DUSD_amount():
    dusd_balance = float(node.accounts.getaccount(ADDRESS, indexed_amounts=True)["15"])
    if dusd_balance < DUSD_AMOUNT:
        loan = round(DUSD_AMOUNT - dusd_balance, 8)
        print(f"DUSD on address is below minimum amount\n"
              f"A loan will be taken: {loan}DUSD")
        node.loan.takeloan(VAULT, f"{loan}@DUSD")

    print("You are good to go with the DUSD part")


def check_DFI_amount():
    dfi_balance = float(node.accounts.getaccount(ADDRESS, indexed_amounts=True)["0"])
    if dfi_balance < DFI_AMOUNT:
        convert = round(DFI_AMOUNT - dfi_balance, 8)
        print(f"DFI on address is below minimum amount\n"
              f"UTXO will be converted to DFI: {convert}UTXO to DFI")

    print(f"You are good to go with the DFI part")


def wait_one_block():
    current_block = node.blockchain.getblockcount()
    print(f"Waiting for one block to be mined: {current_block + 1}")
    while node.blockchain.getblockcount() < current_block + 1:
        time.sleep(1)
    print("Block has been mined")


# actual program sequence
# handle tokens and vault
check_vault_ratio()
check_DUSD_amount()
check_DFI_amount()
wait_one_block()

# handle utxo
all_utxo_to_address()
wait_one_block()
check_min_and_max_utxo()

print(f"if you see this message you are good to go to proceed with the tests")
