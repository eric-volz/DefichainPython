# How to use mnemonic seed phrase for your wallet.dat file

## Introduction
Personally, I find it difficult to rely solely on a single file as security for all my crypto assets. So I tried how it 
is possible to create and restore a wallet.dat file just from a mnemonic seed phrase.
But you can also restore the wallet just from the wallet.dat file.

Here is my approach to make this possible:

## Requirements
- a fully synced defichain node
- Python3 installed on your device
- install the python package: [hdwallet]("https://github.com/meherett/python-hdwallet)
    ```bash
    pip install hdwallet
    ```
  
## Best practice
- write down the mnemonic seed phase on a piece of paper and put it in a secure place
- don't fully rely on the mnemonic seed phrase
  - also make backups of the wallet.dat as you would normally do
- encrypt your wallet.dat with a passphrase
- try to be offline while creating or restoring the wallet.dat
- try to restore the wallet one time before using it
  - to be sure that everything works as expected

## Create a wallet with mnemonic seed phrase
### 1. Generate a mnemonic seed phrase
This two lines of code give you a newly generated mnemonic seed phrase.

Be sure to keep it save!!!
```python
from hdwallet.utils import generate_mnemonic

mnemonic = generate_mnemonic(language="english", strength=256)
```

### 2. Converting the words into [Wallet import format (WIF)](https://river.com/learn/terms/w/wallet-import-format-wif/)
This format is needed to be able to import the seed into a newly created wallet
```python
from hdwallet import HDWallet

wallet = HDWallet()  # creating an empty wallet in the python code
wallet.from_mnemonic(mnemonic)  # importing the mnemonic seed phrase into the wallet

wif = wallet.wif()  # extract the calculated WIF seed from the wallet inside the code
```

### 3. Creating a blank wallet
With this line of code you will create a wallet with the name and passphrase you have set

Explanation of parameters:
1. wallet_name: you can choose the wallet name yourself
2. disable_private_keys: has to be false
3. blank: has to be true
4. passphrase: is recommended
5. avoid_reuse: default is false
```bash
createwallet name false true passphrase false
```

### 4. Importing the WIF into the newly created blank wallet
Explanation of parameters:
1. newkeypool: True
2. seed: has to be the wif step 2
```bash
sethdseed true wif
```

Now you are good to go and able to use the wallet like every other wallet

## Recover a wallet with mnemonic seed phrase
### 1. Follow steps from above
Follow steps 2 - 4 for creating a wallet with mnemonic seed phrase.

### 2. Rescanblockchain
Rescan the blockchain to see all transaction and balances in the wallet
```bash
rescanblockchain
```

## Disclaimer
- Don't try to use a mnemonic seed phrase for an existing wallet
- This possibility to create the wallet using the mnemonic seed phrase should always exist
  - but there could also be changes made to the code that could invalidate the mnemonic seed phrase
  - therefore you should always backup the wallet.dat additionally


THE INSTRUCTION IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND