"""
This is a small script with which you can extract the private keys of your addresses from the mnemonic seed of the
defichain lightwallet.

It uses the DefichainPython libraries by Eric Volz.
GitHub: https://github.com/eric-volz/DefichainPython
PyPi: https://pypi.org/project/defichain/

This script aims to give everyone the possibility to extract their private keys from lightwallet.

Requirement:
>>> pip install defichain

How to use it:
--> Run the script :)

What you can do with the keys:
Import the private key into your defichain full node and control your lightwallet address via the full node
>>> defi-cli importprivkey L5njaFbrQ4nu7ao7a3ocrcrT3n5PnyiftHEY8A31HLDY3CY7d6cb # private key is not valid

Disclaimer:
Be careful when using this script. If your computer is compromised, disclosing the private keys could lead to a total
loss of your coins.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND
"""
from defichain import Wallet
from defichain.hdwallet.utils import generate_mnemonic
from defichain.networks import DefichainMainnet, DefichainTestnet

welcomeText = """
Extract private keys from defichain mnemonic seed
------------------------------------------------------------------------------------
This is a small script with which you can extract the private keys of your addresses
from the mnemonic seed of the defichain lightwallet.
It uses the DefichainPython library by Eric Volz.

It does not store any data on your system nor does it send any data. 
The script should be used offline.

Be careful when using this script. 
If your computer is compromised, disclosing the private keys could lead to a
total loss of your coins.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND
------------------------------------------------------------------------------------
"""
print(welcomeText)

while (network := input('Type "m" for MainNet or "t" for TestNet: ')) not in ("m", "t"):
    print("Network is not valid. Try again.")
wallet = None
if network == "m":
    wallet = Wallet(DefichainMainnet)
elif network == "t":
    wallet = Wallet(DefichainTestnet)

mnemonicSeedText = """
1. Generate new mnemonic seed
2. Use own mnemonic seed
"""
print(mnemonicSeedText)

while (mnemonicSeedPrompt := input('Decision: ')) not in ("1", "2"):
    print("The decision is not valid. Try again.")

if mnemonicSeedPrompt == "1":
    mnemonicSeed = generate_mnemonic()
    wallet.from_mnemonic(mnemonicSeed)
    print("\nGenerated seed:")
    print(f"--> {mnemonicSeed} <--")
elif mnemonicSeedPrompt == "2":
    print("Type your mnemonic seed word by word separated by one space.")
    while mnemonicSeed := input("Type mnemonic seed: "):
        try:
            wallet.from_mnemonic(mnemonicSeed)
            break
        except:
            print("Mnemonic seed is not valid, try again")

addressTypeText = """
There are three different types of addresses. Choose one. If you want to know other addresses, restart the script and 
choose another address.
If you want to know your lightwallet address choose number 3.
1. P2PKH (Legacy Address)
2. P2SH (Default Address)
3. P2WPKH (Bech32 Address) (Lightwallet Address)
"""
print(addressTypeText)

while (addressType := input('Decision: ')) not in ("1", "2", "3"):
    print("The decision is not valid. Try again.")

numberOfAddressesText = """
How many addresses do you want to explore and get the private keys of?
Type 1 if you only want to get the first address and private key.
If you type 10 you get the private keys to the first 10 addresses.
"""
print(numberOfAddressesText)

while True:
    numberOfAddresses = input('Number of addresses and private keys: ')
    try:
        n = int(numberOfAddresses)
        if n <= 0:
            raise Exception()
        break
    except:
        print("The number is not valid. Try again.")

for i in range(int(numberOfAddresses)):
    wallet.from_path(f"m/1129/0/0/{i}")
    if addressType == "1":
        print(f"{i + 1}. Legacy Address: {wallet.legacy_address()}")
    elif addressType == "2":
        print(f"{i + 1}. Default Address: {wallet.default_address()}")
    elif addressType == "3":
        print(f"{i + 1}. Bech32 Address: {wallet.bech32_address()}")
    print(f"{i+1}. Private Key {wallet.wif()}")
    print("--------------------------------------------------------------------")
