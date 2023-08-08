.. image:: https://github.com/eric-volz/DefichainPython/blob/main/docs/source/logo/readme/defichainpython-logo-big.png?raw=true
    :align: center
    :alt: DefichainPython Logo

\

|PyPI Version| |PyPI Python Version| |Downloads|

|Docs Build| |Tests|

|Telegram Group| |Twitter / X| |Status Page|

This library is a community funded project. The objective is to interact
with the defichain blockchain as effortlessly as possible. This can be archived by
utilizing a variety of methods:

1. `Node / RPC <#node--rpc>`__
2. `Ocean <#ocean>`__
3. `HDWallet <#hdwallet>`__
4. `Transactions <#transactions>`__

Installation
------------

Download the PyPi package:

.. code:: bash

   pip install defichain -U

Clone the GitHub Repository:

.. code:: bash

   git clone https://github.com/eric-volz/DefichainPython.git

Features
--------

1. `Node / RPC <https://docs.defichain-python.de/build/html/api/node/index.html>`__:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The node implementation empowers you to easily connect to your defichain
node without having to deal with everything else. You can execute any
function witch is supported by your defichain node.

Make a poolswap via your node:

.. code:: python

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

2. `Ocean <https://docs.defichain-python.de/build/html/api/ocean/index.html>`__:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ocean is an API infrastructure, which is operated by Birthday Research.
You can use it to retrieve a lot of information about the blockchain and
to interact with it.

Ask for the utxo balance of an address:

.. code:: python

   # Import ocean object
   from defichain import Ocean

   # Specify connection
   ocean =  Ocean(network="mainnet")

   # Execute getBalace method
   utxo_balance = ocean.address.getBalance("df1qn6utdvuaq0yshc4sah6puzf0dnlfkc2c8ryme8")

   # Print the utxo balance of the requested address
   print(utxo_balance)

3. `HDWallet <https://docs.defichain-python.de/build/html/sdk/hdwallet/index.html>`__:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

HDWallet (Hierarchical Deterministic Wallet) is a special wallet
implementation for defichain. You can use it to derive your private /
public keys from your mnemonic seed. This implementation is used in
combination with the following feature: `Transactions <#transactions>`__

Create a wallet for mainnet from mnemonic seed:

.. code:: python

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

4. `Transactions <https://docs.defichain-python.de/build/html/sdk/transactions/index.html>`__:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This transaction implementation enables you to create, sign and
broadcast your own transaction just within python. It supports native
utxo (send, sendall, …), as well as defi transactions (poolswap,
takeloan, …) for mainnet and testnet.

.. code:: python

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

`Community <https://docs.defichain-python.de/build/html/legal/community.html>`__
--------------------------------------------------------------------------------

This `project <https://github.com/eric-volz/DefichainPython>`_ is funded by the Defichain Community:

**Thank you for your trust!**

Because of that the community has the right to know about the progress and status of the project. You can view the
status of each module yourself on the
`status page <https://docs.defichain-python.de/build/html/main/statusAndTasks.html>`_!

All official updates and CFPs are listed on
`this page <https://docs.defichain-python.de/build/html/legal/community.html>`_!

If you have suggestions for improvement or other ideas, open an
`issue <https://github.com/eric-volz/DefichainPython/issues>`_, write me on
`Twitter / X <https://twitter.com/defichainpython>`_, leave a comment in the
`telegram group <https://t.me/DefichainPython>`_ or write me oldschool via email
(`defichainpython@volz.link <defichainpython@volz.link>`_)!


`License & Disclaimer <https://docs.defichain-python.de/build/html/legal/licenseAndDisclaimer.html>`__
------------------------------------------------------------------------------------------------------

By using (this repo), you (the user) agree to be bound by the `terms of this
license <https://github.com/eric-volz/defichainLibrary/blob/main/LICENSE>`__
(MIT License).

.. |PyPI Version| image:: https://img.shields.io/pypi/v/defichain.svg?color=green
   :target: https://pypi.org/project/defichain
.. |PyPI Python Version| image:: https://img.shields.io/pypi/pyversions/defichain.svg
   :target: https://pypi.org/project/defichain
.. |Downloads| image:: https://static.pepy.tech/personalized-badge/defichain?period=total&units=international_system&left_color=grey&right_color=green&left_text=Downloads
   :target: https://pepy.tech/project/defichain
.. |Docs Build| image:: https://github.com/eric-volz/DefichainPython/actions/workflows/publish_docs.yml/badge.svg
   :target: https://github.com/eric-volz/DefichainPython/actions/workflows/publish_docs.yml
.. |Tests| image:: https://github.com/eric-volz/DefichainPython/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/eric-volz/DefichainPython/actions/workflows/tests.yml
.. |Telegram Group| image:: https://img.shields.io/badge/Telegram-Group-blue.svg?style=flat-square
   :target: https://t.me/DefichainPython
.. |Twitter / X| image:: https://img.shields.io/badge/Twitter / X-@DefichainPython-lightblue.svg?style=flat-square
   :target: https://twitter.com/defichainpython
.. |Status Page| image:: https://img.shields.io/badge/Status-Page-black.svg?style=flat-square
   :target: https://docs.defichain-python.de/build/html/main/statusAndTasks.html
