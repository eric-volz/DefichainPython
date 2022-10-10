.. _instruction quickstart:

Quickstart
==========

Install the Defichain Python Package
------------------------------------

The library can be installed and used in two ways

1. The library was published on PyPi and can be installed with only one command.

.. code-block:: bash

    pip install defichain -U

2. if you need the latest release or just want to view the code, then clone the GitHub repository

.. code-block:: bash

    git clone https://github.com/eric-volz/DefichainPython.git


Make a request to the Node
--------------------------

Here is an example of how you can connect to the node and how individual requests are executed:

>>> from defichain import Node
>>> node = Node("user", "password", "127.0.0.1", 8554)
>>> node.blockchain.getblockcount() #  returns block height of the latest block
>>> node.poolpair.compositeswap("fromAddress", "BTC", 0.01, "toAddress", "DFI")  # swaps 0.01 BTC to DFI

For more information check the :ref:`Node index` section.


Make a request to Ocean
-----------------------

Here is an example of how you can connect to Ocean and how to request blockchain data:

>>> from defichain import Ocean
>>> ocean = Ocean() #  creates the connection to Ocean
>>> ocean.blocks.list() #  returns the latest 30 blocks
>>> ocean.poolpairs.get(4) #  returns data from ETH-DFI Pool

For more information check the :ref:`Ocean index` section.

Setup a wallet and get the first address
----------------------------------------

Here is an example how to create a new wallet with a newly generated mnemonic seed and how to
retrieve the first bech32 address from it:

>>> from defichain import Wallet
>>> from defichain.networks import DefichainMainnet
>>> from defichain.hdwallet.utils import generate_mnemonic
>>> wallet = Wallet(DefichainMainnet)
>>> mnemonic = generate_mnemonic()
wisdom path obscure scrub travel vessel boring solar truth original quiz letter exhibit spy point mail else entire involve announce vault outer mirror rug
>>> wallet.from_mnemonic(mnemonic)
>>> wallet.bech32_address()
df1q95vyvvu05sgpaem7w8lwufxwnzdchwk9xr7j0y


For more information check the :ref:`HDWallet index` section.
