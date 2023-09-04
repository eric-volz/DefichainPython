.. _Transactions index:

Transactions
============

Documentation  is coming soon!


.. toctree::
    :maxdepth: 1

    builder/index
    advanced/index

.. toctree::
    :maxdepth: 1
    :hidden:

    exceptions

Helper Classes
--------------

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