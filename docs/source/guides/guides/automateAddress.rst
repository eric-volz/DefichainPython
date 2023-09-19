How To Automate Your Defichain Address?
=======================================
This guide will walk you through all the steps to automate your address.
It will show you how to extract your private keys, initialize all the necessary tools, and provide an example of what
automation can look like.

This guide can be used for both Lightwallet addresses and Defichain Node addresses.

.. admonition:: Disclaimer
    :class: attention

    **Please be careful!**

    It requires your private key, which gives access to all your assets.
    So if your computer is compromised, all your assets could be stolen.

    **If you do not know what you are doing, please stop here.**

    Also check the code before you use it, it can not be excluded that there is an error that leads to a total loss
    of funds.

    **Don’t Trust, Verify!**

----

Content
-------

1. `Extracting The Private Key <#extracting-the-private-key>`__
2. `Initialization Of The Script <#initialization-of-the-script>`__
3. `Example Automation <#example-automation>`__
4. `Full Script <#full-script>`__

----

1. Extracting The Private Key
-----------------------------
In order to automate your address, you first need to obtain the private key associated with the address so that you can
move assets.

It's important to note that there are two different types of private keys: the standard hexadecimal private key and a
WIF (Wallet Import Format) private key. These differ in their representation but grant the same access to the address.

**In this guide, we will exclusively work with the WIF Private Key!**

These private keys need to be extracted differently depending on whether you're using a Lightwallet or a Node:

Defichain Lightwallet (Mnemonic Seed)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To automate a Defichain Lightwallet address, you need to extract the private key corresponding to the address using the
mnemonic seed (24 words).

In this case, the first address in the Lightwallet has an index of 0, the second address has an index of 1, and so on...

Depending on which address you want to automate, you must extract the appropriate private key with the correct index:

.. code-block:: python

    from defichain import Wallet
    from defichain.networks import DefichainMainnet

    mnemonic = "blue spend awkward smooth celery earth oak raw unaware bronze tree dry month dust outdoor visa anchor target neglect coast case window depart timber"

    wallet = Wallet(DefichainMainnet)  # initialise wallet on mainnet
    wallet.from_mnemonic(mnemonic)  # import mnemonic into wallet implementation

    account = wallet.get_account(index=0)  # get the first account / address of the mnemonic seed
    print(account.get_wif())  # print the wif of the first account


Defichain Node
~~~~~~~~~~~~~~
For a Defichain Node, you can extract the private key using the CLI command:
`dumpprivkey <https://docs.defichain-python.de/build/html/api/node/wallet.html#defichain.node.Wallet.dumpprivkey>`_

When using the CLI, you should execute the following command:

.. code-block:: bash

    ./defi-cli dumpprivkey "address"

----

2. Initialization Of The Script
-------------------------------
To easily automate the address, you need to set up all the dependencies first.

This includes establishing a connection to Ocean, which serves as the interface to the blockchain.
You'll also need an Account object to manage your private keys and addresses.

The TxBuilder object will then consolidate all the created dependencies, allowing you to easily create transactions.

.. admonition:: Address Types
    :class: caution

    A private key can represent multiple address types. It's essential to choose the correct address carefully:

    P2PKH (legacy): 8L1gvvZFfXAoKy5M79dskWRPa5gof7sme8

    P2SH (default): dNV1LDwyFAuCCvYFQ9QoZYkxAGWgGbF4W2

    P2WPKH (bech32, lightwallet): df1qxc8v5tftrhedg955gj2desxygvn5vqxtqlaekc

.. code-block:: python

    # Import ocean, wallet, network and txbuilder
    from defichain import Ocean
    from defichain import Account
    from defichain.networks import DefichainMainnet
    from defichain import TxBuilder

    # Specify ocean connection
    ocean = Ocean(network="mainnet")

    # Create account
    wif = "Kya4bk1kVzWrbwPy1hanNGxa1maMQH9pgmWKwhHms23cRHi6XBnu"
    account = Account(network=DefichainMainnet, key=wif)

    # Derive correct address
    address = account.get_p2wpkh()

    # Create TxBuilder
    builder = TxBuilder(address, account, ocean)

.. admonition:: Environment file for secrets
    :class: hint

    If you plan to use this script in a production environment, I would recommend storing the private keys in an
    environment file (.env) for security and ease of management.
    However, for the sake of simplicity, I haven't done that in this example.

----

3. Example Automation
---------------------
In this example, I'm presenting a script that converts all tokens on an address to DFI.
This can be used to convert dust on an address and can be scheduled to run daily, for instance.

**All transactions are executed within a single block!**

Querying all tokens associated with the address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To query all tokens associated with an address, you can use the
`listToken <https://docs.defichain-python.de/build/html/api/ocean/address.html#defichain.ocean.Address.listToken>`_
method from Ocean.

In this script, all tokens are queried, and LP tokens as well as the DFI token itself are filtered out:

.. code-block:: python

    # Request all tokens of your address from ocean
    tokens = ocean.address.listToken(address, size=200).get("data")
    convert_tokens = []

    for token in tokens:
        if not token.get("isLPS") and not token.get("symbol") == "DFI":  # Filter LP-token and DFI token
            convert_tokens.append({"symbol": token.get("symbol"), "amount": token.get("amount")})

Preparing the inputs for the composite swap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A for loop is executed in the script, iterating through each token that can be swapped. Before the tokens can be
swapped into DFI, some variables need to be set.

Of particular interest here is the path used for the swap, which is queried from Ocean.

.. code-block:: python

    for convert_token in convert_tokens:
        # Variables for composite swap
        address_from = address
        token_from = convert_token.get("symbol")
        amount = float(convert_token.get("amount"))
        address_to = address
        token_to = "DFI"
        max_price = 999999999

        # Get best swap path for different tokens from ocean
        token_from_id = Token.get_id_from_symbol(DefichainMainnet, token_from)
        token_to_id = Token.get_id_from_symbol(DefichainMainnet, token_to)

        pools = ocean.poolpairs.getBestPath(token_from_id, token_to_id)

        paths = pools.get("data").get("bestPath")
        bestPath = []
        for path in paths:
            bestPath.append(path.get("symbol"))

Building and executing transactions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The transactions are built sequentially, meaning the second transaction uses the unspent inputs from the first
transaction, the third transaction uses the unspent inputs from the second transaction, and so on.

The unspent inputs are stored in a variable called "unspent":

**Outside the For-Loop:**

.. code-block:: python

    unspent = None  # Store unspent inputs of the last tx


The transactions are built at 10-second intervals and submitted to the blockchain via Ocean.

**Inside the For-Loop:**

.. code-block:: python

    if not unspent:
        # First transaction uses the inputs from ocean (automatic)
        tx = builder.pool.compositeswap(
            addressFrom=address_from,
            tokenFrom=token_from,
            amountFrom=amount,
            addressTo=address_to,
            tokenTo=token_to,
            maxPrice=max_price,
            pools=bestPath
        )
    else:
        # Following transactions are using the unspent inputs from the transaction before them
        tx = builder.pool.compositeswap(
            addressFrom=address_from,
            tokenFrom=token_from,
            amountFrom=amount,
            addressTo=address_to,
            tokenTo=token_to,
            maxPrice=max_price,
            pools=bestPath,
            inputs=unspent
        )
    unspent = tx.get_unspent()  # set unspent inputs from the last transaction

    time.sleep(10)  # wait 10 seconds for the transaction to be inserted
    txid = builder.send_tx(tx)  # insert transaction
    print(txid)


Full Script
-----------

.. admonition::  **Be careful!**
    :class: attention

    This script swaps all tokens on your address to DFI!

.. code-block:: python

    # Import ocean, wallet, network and txbuilder
    from defichain import Ocean
    from defichain import Account
    from defichain.networks import DefichainMainnet
    from defichain import TxBuilder

    # Specify ocean connection
    ocean = Ocean(network="mainnet")

    # Create account
    wif = "Kya4bk1kVzWrbwPy1hanNGxa1maMQH9pgmWKwhHms23cRHi6XBnu"
    account = Account(network=DefichainMainnet, key=wif)

    # Derive correct address
    address = account.get_p2wpkh()

    # Create TxBuilder
    builder = TxBuilder(address, account, ocean)

    # Request all tokens of your address from ocean
    tokens = ocean.address.listToken(address, size=200).get("data")
    convert_tokens = []

    for token in tokens:
        if not token.get("isLPS") and not token.get("symbol") == "DFI":  # Filter LP-token and DFI token
            convert_tokens.append({"symbol": token.get("symbol"), "amount": token.get("amount")})

    unspent = None  # Store unspent inputs of the last tx

    # For loop to swap all tokens on an address to DFI
    for convert_token in convert_tokens:
        # Variables for composite swap
        address_from = address
        token_from = convert_token.get("symbol")
        amount = float(convert_token.get("amount"))
        address_to = address
        token_to = "DFI"
        max_price = 999999999

        # Get best swap path for different tokens from ocean
        token_from_id = Token.get_id_from_symbol(DefichainMainnet, token_from)
        token_to_id = Token.get_id_from_symbol(DefichainMainnet, token_to)

        pools = ocean.poolpairs.getBestPath(token_from_id, token_to_id)

        paths = pools.get("data").get("bestPath")
        bestPath = []
        for path in paths:
            bestPath.append(path.get("symbol"))

        if not unspent:
            # First transaction uses the inputs from ocean (automatic)
            tx = builder.pool.compositeswap(
                addressFrom=address_from,
                tokenFrom=token_from,
                amountFrom=amount,
                addressTo=address_to,
                tokenTo=token_to,
                maxPrice=max_price,
                pools=bestPath
            )
        else:
            # Following transactions are using the unspent inputs from the transaction before them
            tx = builder.pool.compositeswap(
                addressFrom=address_from,
                tokenFrom=token_from,
                amountFrom=amount,
                addressTo=address_to,
                tokenTo=token_to,
                maxPrice=max_price,
                pools=bestPath,
                inputs=unspent
            )
        unspent = tx.get_unspent()  # set unspent inputs from the last transaction

        time.sleep(10)  # wait 10 seconds for the transaction to be inserted
        txid = builder.send_tx(tx)  # insert transaction
        print(txid)


