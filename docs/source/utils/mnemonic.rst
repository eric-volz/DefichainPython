.. _Mnemonic:

Mnemonic
========

This is a class with which you can generate and check mnemonic seed's

Example
-------

>>> from defichain import Mnemonic
>>> mnemonic = Mnemonic(language="english")
>>> seed = mnemonic.generate(256)
"shoulder unusual practice sight apart course eager true diesel rescue diagram denial oppose total fun rocket spend chapter spider paddle benefit empower type purse"
>>> Mnemonic.detect_language(seed)
"english"
>>> mnemonic.check(seed)
True

.. automodule:: defichain.mnemonic

.. autoclass:: Mnemonic
    :members: