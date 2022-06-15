.. _instruction quickstart:

Quickstart
==========

Install the Defichain Python Package
------------------------------------

The library can be installed and used in two ways

1. The library was published on PyPi and can be installed with only one command.

.. code-block:: bash

    pip install defichain

2. if you need the latest release or just want to view the code, then clone the GitHub repository

.. code-block:: bash

    git clone https://github.com/eric-volz/DefichainPython.git


Make a request to the Node
--------------------------

Here is an example of how you can connect to the node and how individual requests are executed:

.. code-block:: python

    from defichain import Node

    node = Node("user", "password", "127.0.0.1", 8554)

    node.blockchain.getblockcount() #  returns block height of the latest block

    node.poolpair.compositeswap("fromAddress", "BTC", 0.01, "toAddress", "DFI")  # swaps 0.01 BTC to DFI

For more information check the :ref:`Node index` section.


Make a request to Ocean
-----------------------

Here is an example of how you can connect to Ocean and how to request blockchain data:

.. code-block:: python

    from defichain import Ocean

    ocean = Ocean() #  creates the connection to Ocean

    ocean.blocks.list() #  returns the latest 30 blocks

    ocean.poolpairs.get(4) #  returns data from ETH-DFI Pool

For more information check the :ref:`Ocean index` section.