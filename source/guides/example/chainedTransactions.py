import time
from defichain import TxBuilder, Ocean, Wallet
from defichain.networks import DefichainTestnet

"""
In this example, several transactions build on each other. This means that the second transaction uses the inputs of the 
first transaction and so on.
With defi transactions (poolswap, takeloan, utxotoaccount) only those transactions can build on each other where the 
result is absolutely clear. 

Example:
When executing takeloan you want to have exactly 5 DUSD. The system knows that you will get exactly 5 DUSD and you can 
use them in the next Tx.

When executing a pool swap you want to exchange 1 DFI into BTC. But the system only knows how much BTC you will get 
when the block has been minted. So transactions that come after a poolswap cannot continue with the output of the 
poolswap.
"""

"""Script Setup"""
PRIVATE_KEY = "cTBazS4LCqitNniS3zW34UmhtQgBWSiuUeTCKFHfPkXyaLGPoy6b"  # wif private key
wallet = Wallet(DefichainTestnet).from_wif(PRIVATE_KEY)  # create testnet wallet
account = wallet.get_account()  # get account

ADDRESS = account.get_p2wpkh()  # address to use
VAULT_ID = "9429280b52dff4784465b3b00174fc12722907d6459bb7c50f2fad0dc5c20083"  # vault to use

ocean = Ocean(url="https://testnet.ocean.jellyfishsdk.com", network="testnet")  # testnet ocean connection
builder = TxBuilder(ADDRESS, account, ocean, 1.0)  # transaction builder

"""Account Setup"""
# tx_utxos_to_account = builder.accounts.utxostoaccount(ADDRESS, 700) # Convert UTXOS to Token
# tx_create_vault = builder.vault.createvault(ADDRESS, "C150")  # Create Vault with 150% Loan Scheme (Mainnet: MIN150)
# tx_deposit_to_vault = builder.vault.deposittovault(VAULT_ID, ADDRESS, "500@DFI")  # Deposit to vault

"""Create multiple transactions for one block"""
tx_take_loan = builder.loans.takeloan(VAULT_ID, ADDRESS, "5@DUSD")  # Take Loan
tx_take_loan_unspent = tx_take_loan.get_unspent()  # Takes the unspent inputs from the created transaction

# poolswapt with the inputs of the previously created transaction
tx_poolswap = builder.pool.poolswap(ADDRESS, "DUSD", 5, ADDRESS, "GOOGL", 99999999, tx_take_loan_unspent)

"""Submit multiple transactions in one block"""
txid_take_loan = builder.send_tx(tx_take_loan)  # Submit first tx to the network

while True:  # Ocean needs a few seconds to index the first transaction. After the second transaction can be submitted.
    try:
        txid_poolswap = builder.send_tx(tx_poolswap)  # Submit second tx to the network
        break
    except Exception as e:
        print(e)  # print exception
        time.sleep(0.5)  # wait 0.5 seconds for next try

"""Print TXID's"""
print(f"Take Loan: {txid_take_loan}")
print(f"PoolSwap: {txid_poolswap}")

