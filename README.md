[![PyPI Version](https://img.shields.io/pypi/v/defichain.svg?color=green)](https://pypi.org/project/defichain)
[![PyPI Python Version](https://img.shields.io/pypi/pyversions/defichain.svg)](https://pypi.org/project/defichain)
[![Downloads](https://static.pepy.tech/personalized-badge/defichain?period=total&units=international_system&left_color=grey&right_color=green&left_text=Downloads)](https://pepy.tech/project/defichain)

[![Build and Deploy Documentation to GitHub Pages](https://github.com/eric-volz/DefichainPython/actions/workflows/publish_docs.yml/badge.svg)](https://github.com/eric-volz/DefichainPython/actions/workflows/publish_docs.yml)
[![Tests](https://github.com/eric-volz/DefichainPython/actions/workflows/tests.yml/badge.svg)](https://github.com/eric-volz/DefichainPython/actions/workflows/tests.yml)

# [DefichainPython](https://github.com/eric-volz/DefichainPython)

This library is a community funded project. The objective is to interact with the defichain blockchain as effortlessly as possible, 
utilizing a variety of methods:

1. __[Node / RPC](#node--rpc)__
2. __[Ocean](#ocean)__
3. __[HDWallet](#hdwallet)__
4. __[Transactions](#transactions)__

## Installation

Download the PyPi package:
```bash
pip install defichain -U
```
Clone the GitHub Repository:
```bash
git clone https://github.com/eric-volz/DefichainPython.git
```

## Features

### 1. [Node / RPC](https://docs.defichain-python.de/build/html/api/node/index.html):
The node implementation empowers you to easily connect to your defichain node without having to deal with everything 
else. You can execute any function witch is supported by your defichain node.

Make a poolswap via your node:
```python
# Import node object
from defichain import Node

# Specify connection
node =  Node("user", "password", url="127.0.0.1", port=8554)

addressFrom = "df1qn6utdvuaq0yshc4sah6puzf0dnlfkc2c8ryme8"
tokenFrom = "BTC"
amount = 0.1
addressTo = "df1qn6utdvuaq0yshc4sah6puzf0dnlfkc2c8ryme8"
tokenTo = "DFI"
maxprice = 3000

# Execute poolswap
txid = node.poolpair.poolswap(addressFrom, tokenFrom, amount, addressTo, tokenTo, maxprice)

# Print txid
print(txid)
```

### 2. [Ocean](https://docs.defichain-python.de/build/html/api/ocean/index.html):
Ocean is an API infrastructure, which is operated by Birthday Research. You can use it to retrieve a lot of information 
about the blockchain and to interact with it.

Ask for the utxo balance of an address:
```python
# Import ocean object
from defichain import Ocean

# Specify connection
ocean =  Ocean(network="mainnet")

# Execute getBalace method
utxo_balance = ocean.address.getBalance("df1qn6utdvuaq0yshc4sah6puzf0dnlfkc2c8ryme8")

# Print the utxo balance of the requested address 
print(utxo_balance)
```

### 3. [HDWallet](https://docs.defichain-python.de/build/html/api/hdwallet/index.html):
HDWallet (Hierarchical Deterministic Wallet) is a special wallet implementation for defichain. You can use it to derive 
your private / public keys from your mnemonic seed. This implementation is used in combination with the following 
feature: [Transactions](#transactions)

Create a wallet for mainnet from mnemonic seed:
```python
# Import wallet and network
from defichain import Wallet
from defichain.networks import DefichainMainnet

#  Mnemonic seed
mnemonic = "avocado key fan step egg engage winter upper attitude carry regret mixed utility body party trip valid oppose gas ensure deputy suspect blur trade"

# Create wallet for specified network and insert mnemonic seed
wallet = Wallet(DefichainMainnet)
wallet.from_mnemonic(mnemonic)

# Derive first account from the wallet
account = wallet.get_account(0)

# Print every address type
print(account.get_p2pkh())  # 8KvWa4oCfAhdyUNK8pXJS8XnddsxY6ZY7J
print(account.get_p2sh())  # dUiMDov5Jxg3qKcy9yi6petuUtrvBRezUS
print(account.get_p2wpkh())  # df1qx52ql637w4t7uk2vjdatj3a24cnvuu4fkxryrr

# Print every private key type
print(account.get_privateKey())  # c72f08c17b475d641a711ef1e16bcdb0cc0c1210e6da846060b2e04d5c2299b3
print(account.get_wif())  # L3tu3Bx5n8aWgcDd14btMPgxQ8H5VYbbNoodrNESaonom64YPnr9
```

### 4. [Transactions](https://docs.defichain-python.de/build/html/api/transactions/index.html):
This transaction implementation enables you to create, sign and broadcast your own transaction just within python.
It supports native utxo (send, sendall, ...), as well as defi transactions (poolswap, takeloan, ...) for mainnet and 
testnet.

```python
# Import ocean, wallet, network and txbuilder
from defichain import Ocean
from defichain import Wallet
from defichain.networks import DefichainMainnet
from defichain import TxBuilder

# Specify ocean connection
ocean =  Ocean(network="mainnet") 

# Create wallet and account
mnemonic = "avocado key fan step egg engage winter upper attitude carry regret mixed utility body party trip valid oppose gas ensure deputy suspect blur trade"

wallet = Wallet(DefichainMainnet)
wallet.from_mnemonic(mnemonic)

account = wallet.get_account(0)

# Create TxBuilder
builder = TxBuilder(account.get_p2wpkh(), account, ocean)

addressFrom = account.get_p2wpkh()
tokenFrom = "BTC"
amount = 0.1
addressTo = account.get_p2wpkh()
tokenTo = "DFI"
maxprice = 3000

# Build poolswap transaction
tx = builder.pool.poolswap(addressFrom, tokenFrom, amount, addressTo, tokenTo, maxprice)

# Send transaction into the blockchain
txid = builder.send_tx(tx)

# Print txid
print(txid)
```

## [Community](https://docs.defichain-python.de/build/html/legal/community.html)

This [project](https://github.com/DeFiCh/dfips/issues/133) is funded by the Defichain Community:
Thank you for your trust! If you have suggestions for improvement
or other ideas open an [issue](https://github.com/eric-volz/DefichainPython/issues), 
write me on [Twitter](https://twitter.com/Intr0c) or via email (introc@volz.link)!

## [License & Disclaimer](https://docs.defichain-python.de/build/html/legal/licenseAndDisclaimer.html)

By using (this repo), you (the user) agree to be bound by the 
[terms of this license](https://github.com/eric-volz/defichainLibrary/blob/main/LICENSE) (MIT License).
