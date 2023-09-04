.. _Transactions index:

Transactions
============

This is the entry page to get information about building a raw transaction for defichain using python.

**There are two ways to use this implementation:**

1. :ref:`Transaction Builder Index`: Abstracts the complexity of creating a transaction to a minimum
   **(recommended for 99% of users)**
2. :ref:`Transaction Advanced Index`: You can create transaction on your own behave and stay very flexible while
   using the infrastructure of the library

.. toctree::
    :maxdepth: 1
    :hidden:

    builder/index
    advanced/index

.. toctree::
    :maxdepth: 1
    :hidden:

    exceptions

----

Default Input Structure
-----------------------

There will be some input structures throughout the implementation witch will be explained below:

.. automodule:: defichain.transactions.utils

.. _Transactions Amounts:

Amounts
_______

The amount describes a combination of an token amount (int / float) and the corresponding token symbol: amount@token

>>> "1@DFI"  # one amount

>>> ["1@DFI", "1@BTC", "1@ETH"]  # multiple amounts

There is an helper class to make the creation of amounts evan easier:

.. autoclass:: BuildAmounts
    :members:
    :noindex:

.. _Transactions AddressAmount:

Address Amounts
_______________

The address is the key, the value are the :ref:`amounts <Transactions Amounts>`.

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

There is an helper class to make the creation of address amounts evan easier:

.. autoclass:: BuildAddressAmounts
    :members:
    :noindex: