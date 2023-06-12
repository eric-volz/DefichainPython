.. _HDWallet index:

HDWallet
========

This is the main page to get information about the control of the Wallet.

The most important class is the :ref:`HDWallet wallet`: within this class all important parameters of your
wallet are calculated.

There are other methods around the wallet, which can be found under :ref:`HDWallet utils`.
These methods include for example the generation of the mnemonic seed.

When creating a wallet, a network must be passed to the wallet, which defines how the various parameters are calculated.
There are three different types of networks: **DefichainMainnet, DefichainTestnet, DefichainRegTest**

The simplest setup of the class can be seen on the :ref:`Quickstart <instruction quickstart wallet>` page.

You can find more explanations :ref:`below <HDWallet illustration>`.

.. admonition:: Path
    :class: caution

    **All defichain addresses and private keys use the path: m/1129/0/0/0.**
    The last index of the path can increased to calculate the next addresses and keys.


.. admonition:: Import private keys
    :class: caution

    **All calculated private keys in the WIF format can be imported into a Defichain Node with the method: importprivkey**

.. admonition:: Defichain Lightwallet addresses
    :class: caution

    **The bech32 addresses are the addresses used in the Defichain Lightwallet**

Wallet Components
-------------------

.. toctree::
    :maxdepth: 1

    wallet
    utils

.. _HDWallet illustration:

Illustration
------------

Get Networks
____________

The networks are located in a seperated folder of the package:

>>> from defichain.networks import DefichainMainnet
>>> DefichainMainnet.NETWORK
mainnet
>>> from defichain.networks import DefichainTestnet
>>> DefichainTestnet.NETWORK
testnet
>>> from defichain.networks import DefichainRegtest
>>> DefichainRegtest.NETWORK
regtest

Wallet from mnemonic seed
_________________________

On of the easiest ways to create a wallet is to use a mnemonic seed:

>>> from defichain import Wallet
>>> from defichain.networks import DefichainMainnet
>>> wallet = Wallet(DefichainMainnet)
>>> wallet.from_mnemonic("sceptre capter séquence girafe absolu relatif fleur zoologie muscle sirop saboter parure")


Wallet from private key
_______________________

But you can also create a wallet from just one Private Key:

.. note::
    Creates only keys for specified private key: no iteration is possible

>>> from defichain import Wallet
>>> from defichain.networks import DefichainMainnet
>>> wallet = Wallet(DefichainMainnet)
>>> wallet.wif("Kzn333NbqsAASpycmNTB8ssuZQJjiaj8wDrBzAaGPNoJCDTNJqfQ")
>>> wallet.bech32_address()
df1qwhruysa0t04vtcmyezrc6feddwg0f8fdc5dwy7

Generate mnemonic seed
______________________

This mnemonic seed can be generated with the method: generate_mnemonic() in the wallet utils

>>> from defichain.hdwallet.utils import generate_mnemonic
>>> generate_mnemonic()
damage salt diary special jealous biology uncle detect carbon shadow pelican unusual exit mansion direct paper vehicle panther obvious orchard skill ball scare jar

Iterate truth addresses and private keys
________________________________________

Calculates the first ten bech32 addresses and private keys from mnemonic

>>> from defichain import Wallet
>>> from defichain.networks import DefichainMainnet
>>> wallet = Wallet(DefichainMainnet)
>>> wallet.from_mnemonic("sceptre capter séquence girafe absolu relatif fleur zoologie muscle sirop saboter parure")
>>> for i in range(10):
>>>     wallet.from_path(f"m/1129/0/0/{i}")
>>>     print(f"{i+1}. Bech32 Address: {wallet.bech32_address()}")
>>>     print(f"{i+1}. Private Key {wallet.wif()}")
1. Bech32 Address: df1qwhruysa0t04vtcmyezrc6feddwg0f8fdc5dwy7
1. Private Key Kzn333NbqsAASpycmNTB8ssuZQJjiaj8wDrBzAaGPNoJCDTNJqfQ
2. Bech32 Address: df1q8ysut4vvchwzfz852w2tw8mc0ev6az5twhv7fh
2. Private Key L4CSqWy2iaeWQqz5mDSU8pyLS3PPp756aQdLrKmsfmg8h3GDkkWD
3. Bech32 Address: df1q93qkyxapl3crdgyum2xw8yc6w7fzyf7k8qx7rh
3. Private Key KxBPXweWK2M1W1NBjBpdhpR2NHGqNAdWQ4Fb2G7LUdW46xSA9653
4. Bech32 Address: df1q8tyn7e05hnzqzhg2rm2xntu8t74y79lqrk0vm6
4. Private Key L4Q5ThuGq6zL5hREqUaW8wbSnmUEc6yLApkWYm4PgocSkQ7NuM5W
5. Bech32 Address: df1q8h3geevwhqmk7njsrq80dqf7uzsshgrdr583zj
5. Private Key L5X97wjMsQdFJwbJwdTeZbU1pF7wosHhFh5ijBBx5PjfGgidwpYD
6. Bech32 Address: df1qmnqh6j9p55y56cws5vnuu3lrr9k8dwhvrwzqmj
6. Private Key Kza8sb5exVwu5FT5JBdjAJgky7iivVCt2t3h2MwBD8oqjKeUHBzL
7. Bech32 Address: df1qmzusk8ns4evrduu5phmr0vc2exectum38qc27h
7. Private Key L2hrsrMeMufMnYgHCvBofkc4Tcm8jS8Td4xtW1qg6hWmHyXRBeaK
8. Bech32 Address: df1qy4pq4m6aq8rcdr7mhd34urzrarpnulsd5udd0c
8. Private Key Kww1ciPxUkDFBhY5mcXTcUzkXZEYHafFi1eSJUfMveiCZ2b2a8NM
9. Bech32 Address: df1quk3sjkw7sy3jyu7j74uugxt3fcg9juh7myhzga
9. Private Key L4hfAjm13EjCik8krttsGAFzsZ7f4h65E2ch2Q36ZVSW1T9Sf9KR
10. Bech32 Address: df1qhzd5vka5lyvwvaqntpn8yzpr7af6nddr7m5llx
10. Private Key L23iH2udEUpaUZnJzNpsRHJAtsEhQf6T4x9EWEond72s5Z5bzbLq