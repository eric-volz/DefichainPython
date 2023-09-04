.. _Transaction Builder Index:

Transaction Builder
===================

The :ref:`TxBuilder class <Transaction Builder TxBuilder>` tries to reduces the complexity of creating a transaction to a minimum.
The objective is to empower everyone to create their own transactions.

The :ref:`class <Transaction Builder TxBuilder>` arguments will be explained inside the class itself. But an example with explanation can be read
:ref:`below <Transaction Builder Example>`.

The TxBuilder, as well as the whole implementation, supports building transactions for
:ref:`all address types <Transaction Advanced Address Index>` (P2PKH, P2SH, P2WPKH) currently supported by defichain.
Both networks, mainnet and testnet, are supported.

.. admonition:: Assumptions
    :class: caution

    Because of the reduced the complexity when using the TxBuilder some assumptions had to be made:

    - All UTXO inputs of an address will be used and combined to one UTXO output (unless otherwise stated in the method)
    - When executing a DefiTx the UTXO outputs will always go back to the same address

----

TxBuilder Modules
-----------------

.. toctree::
    :maxdepth: 1

    txbuilder
    accounts
    data
    governance
    loans
    masternode
    pool
    utxo
    vault

.. _Transaction Builder Example:

Example with explanation
------------------------
The following example demonstrates how to create, sign, and send a transaction to the defichain network using the
TxBuilder object:

.. code-block:: python

    # 1. Import ocean, wallet, txbuilder and the network
    from defichain import Ocean, Wallet, TxBuilder
    from defichain.networks import DefichainMainnet

    # 2. Specify ocean connection
    ocean =  Ocean(network="mainnet")

    # 3. Create wallet and account
    mnemonic = "avocado key fan step egg engage winter upper attitude carry regret mixed utility body party trip valid oppose gas ensure deputy suspect blur trade"

    wallet = Wallet(DefichainMainnet)
    wallet.from_mnemonic(mnemonic)

    account = wallet.get_account(0)

    # 4. Create TxBuilder
    builder = TxBuilder(account.get_p2wpkh(), account, ocean)

    addressFrom = account.get_p2wpkh()
    tokenFrom = "BTC"
    amount = 0.1
    addressTo = account.get_p2wpkh()
    tokenTo = "DFI"
    maxprice = 3000

    # 5. Build poolswap transaction
    tx = builder.pool.poolswap(addressFrom, tokenFrom, amount, addressTo, tokenTo, maxprice)

    # 6. Send transaction into the blockchain
    txid = builder.send_tx(tx)

    # 7. Print txid
    print(txid)


Initialization of the TxBuilder object
______________________________________
The following four steps must always be fulfilled at the beginning of a new project / script to create a TxBuilder
object:

1. First, all the necessary elements required for creating transactions must be imported. This includes a connection to
   :ref:`Ocean <Ocean Index>`, the :ref:`Wallet <HDWallet Index>` Implementation, and the
   :ref:`TxBuilder <Transaction Builder Index>` object itself. Since this example pertains to building transactions for the
   mainnet, the correct network must be imported.

2. In the second step, the :ref:`ocean <Ocean Ocean>` object is initialized, establishing a connection to the Ocean
   mainnet. This connection is necessary because certain information from the blockchain are required to create a
   transaction. These details do not necessarily have to come from Ocean; you can also use a connection to your own
   :ref:`defichain node <Node Index>` or manually input the required information.

3. In the third step, the :ref:`account <HDWallet Account>` being used must be initialized. In the example, a
   :ref:`wallet <HDWallet wallet>` is initialized using a mnemonic seed, and from that seed, the first account is
   derived. This is similar to using the first address in the LightWallet. However, the account object can also be
   initialized directly using the private key.

4. As the fourth step, the :ref:`TxBuilder <Transaction Builder TxBuilder>` object is initialized with the dependencies
   created earlier. Since an account represents exactly one private key, which in turn corresponds to three different
   :ref:`address types <Transaction Advanced Address Index>` (P2PKH, P2SH, P2WPKH), the appropriate address must be
   provided as the first argument.

Creating, signing, and sending transactions
___________________________________________
The following three steps are based on the previously created TxBuilder object.

5. In this code line, the actual transaction is created and automatically signed using the TxBuilder object. In this
   example, a :ref:`poolswap <Transaction Builder Pool>` transaction is shown. Creating transactions closely
   follows the arguments known by the defichain node. All implemented transaction types and their arguments can be
   found in the :ref:`documentation <Transaction Builder Index>`.

6. Once the transaction is created and signed, it can be added to the defichain network using the TxBuilder object as
   well.

7. If the transaction is valid and accepted by the blockchain, a transaction hash is returned.


