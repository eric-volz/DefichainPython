Node / RPC
==========

Default Inputs
--------------
These are formats that are used more often as input to a method

.. _Node Amount:

Amounts
~~~~~~~
Amount in amount@token format.

.. code-block:: text

    "1@DFI"  # one amount

    ["1@DFI", "1@BTC", "1@ETH"]  # multiple amounts

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

.. toctree::
    :hidden:

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
    rawtransactions
    spv
    tokens
    util
    vault
    wallet
    zmq
