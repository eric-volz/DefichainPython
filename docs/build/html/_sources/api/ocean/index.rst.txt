.. _Ocean index:

Ocean
=====

This is the main page to get information about the control of ocean.

The most important class is the :ref:`Ocean Ocean` class: it takes care of the actual
connection to ocean and performs the requests made by methods.

The simplest setup of the class can be seen on the :ref:`instruction quickstart` page.

All individual methods are assigned to specific modules.
For example to output data from blocks you have to use the method List in blocks.

You can find more explanations :ref:`below <Ocean requestStructure>`

Ocean Modules
-------------

.. admonition:: Documentation of modules
    :class: important

    I will keep documenting more methods. :ref:`Here<instruction progressAndUpdates>`
    you can follow the progress.

.. toctree::

    ocean
    address
    blocks
    fee
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

Will follow soon