.. _Ocean index:

Ocean
=====

This is the main page to get information about the control of ocean.

The most important class is the :ref:`Ocean Ocean` class: it takes care of the actual
connection to ocean and performs the requests made by methods.

The simplest setup of the class can be seen on the :ref:`Quickstart <instruction quickstart ocean>` page.

All individual methods are assigned to specific modules.
For example to output data from blocks you have to use the method List in blocks.

You can find more explanations :ref:`below <Ocean requestStructure>`

.. admonition:: New Logger available
    :class: caution

    If you want to log all requests and results, you can use the new :ref:`Logger` Class.

Ocean Modules
-------------

.. toctree::

    ocean
    address
    blocks
    consortium
    fee
    governance
    loan
    masternodes
    oracles
    poolpair
    prices
    rawTx
    rpc
    stats
    tokens
    transactions

.. _Ocean requestStructure:

Request Structure
-----------------

The request structure is very simple and basically consists of only three things:

1. The previously created ocean object by the ocean class.
2. The module in which the method you want to execute is found.
3. The method you want to execute.

Example:

.. code-block:: python

    from defichain import Ocean  # Import

    ocean = Ocean()  # creating the ocean object

    # 1     2     3
    ocean.blocks.list()

If you are not sure in which module your method is located, use the search function
in the upper left corner.

Default Inputs
--------------

These are input formats which are very often used.

.. _Ocean Pagination:

Pagination
~~~~~~~~~~

Most API with LIST operation can be paginated. All paginate-able resource endpoint in
Ocean REST API represent one sort indexes/projection. Pagination within Ocean REST API is
done via "slice window", if there are more items in your query, you are given a "next token" to
get the next slice.

Example:
Should show how to work with the size and next parameter

.. code-block:: python

    from defichain import Ocean

    ocean = Ocean() #  creates the connection to Ocean
    next = "" # initialize the next value

    while True: # infinite loop
        request = ocean.blocks.list(size=200, next=next) # request for 200 blocks with correct next value

        next = request["page"]["next"] # set new next value from previous request
        blocks = request["data"] # slize block data

        print(blocks) # print block data

.. _Ocean Size:

Size
____
How many elements a List output should have.

Default: 30

Maximum: 200

.. code-block:: python

    ocean = Ocean() #  creates the connection to Ocean

    ocean.blocks.list(size=200) #  returns the latest 200 blocks

.. _Ocean Next:

Next
____
Scrolls through a list.

Points to the data of the next request.

The next pointer can be found in the output of the previous request.

.. code-block:: python

    ocean = Ocean() #  creates the connection to Ocean

    ocean.blocks.list(next="2269079") #  returns 30 blocks from next pointer 2269079