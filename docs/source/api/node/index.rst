.. _Node index:

Node / RPC
==========

This is the main page to get information about the control of the node.

The most important class is the :ref:`Node Node` class: it takes care of the actual
connection to the node and performs the requests made by methods.

The simplest setup of the class can be seen on the :ref:`Quickstart <instruction quickstart node>` page.
It offers other possibilities, such as automatically importing and using a
wallet or decrypting a password-protected wallet.

All individual methods are assigned to specific modules.
These modules match the ones that are output by the :ref:`help method<Node RawMethodsOverview>`.
For example, the getblockcount method belongs to the blockchain
module and the compositeswap method belongs to the poolpair module.

You can find more explanations :ref:`below <Node requestStructure>`

.. admonition:: New Logger available
    :class: caution

    If you want to log all requests and results, you can use the new :ref:`Logger` Class.

Node Modules 
------------

.. toctree::
    :maxdepth: 1

    node
    accounts
    blockchain
    control
    generating
    loan
    masternodes
    mining
    network
    oracles
    poolpair
    proposals
    rawtransactions
    spv
    stats
    tokens
    util
    vault
    wallet
    zmq

.. toctree::
    :maxdepth: 1
    :hidden:

    rawMethodsOverview

.. _Node requestStructure:

Request Structure
-----------------

The request structure is very simple and basically consists of only three things:

1. The previously created node object by the node class.
2. The module in which the method you want to execute is found.
3. The method you want to execute.

Example:

.. code-block:: python

    from defichain import Node  # Import

    node = Node("user", "password", "127.0.0.1", 8554)  # creating the node object

    # 1      2            3
    node.blockchain.getblockcount()

If you are not sure in which module your method is located, use the search function
in the upper left corner or look in the :ref:`Node RawMethodsOverview`

Default Inputs
--------------
These are input formats which are very often used in the Node software.

.. _Node Amount:

Amounts
~~~~~~~
Amount in amount@token format.

.. code-block:: text

    "1@DFI"  # one amount

    ["1@DFI", "1@BTC", "1@ETH"]  # multiple amounts

There is also a class for the creation of amounts, to make it evan easier:

BuildAmounts
____________

.. automodule:: defichain.node

.. autoclass:: BuildAmounts
    :members:

.. _Node Address Amount:

Address Amount
~~~~~~~~~~~~~~
The defi address is the key, the value is amount in amount@token format. If multiple tokens are to be transferred, specify an array ["amount1@t1", "amount2@t2"]

.. code-block:: text

    {
        "address": "amounts"
    }

Example:

.. code-block:: text

    {
        "dcTKz5SQrqf4vGVsgra76ptXeNBcxPrenP": "1@DFI",
        "df1qzkf582h0sgfksj0yn0wxz0r9amyqfferm5wycs": ["2.0@BTC", "3.0@ETH"]
    }

There is also a class for the creation of address amounts, to make it evan easier:

BuildAddressAmounts
___________________

.. autoclass:: BuildAddressAmounts
    :members:


.. _Node TransferDomain:

TransferDomain
______________

.. autoclass:: BuildTransferDomainData
    :members:

.. _Node Inputs:

Inputs
~~~~~~
Optional argument (may be empty array) is an array of specific UTXOs to spend

.. code-block:: text

    [
        {
        "txid": "hex",     (string, required) The transaction id
        "vout": n,         (numeric, required) The output number
        },
        ...
    ]
