## The Defichain Python Library implements HDWallet!

Dear Defichain Community,

a few days ago I released version 2.0.0 of the [Defichain Python Library](https://github.com/eric-volz/DefichainPython).

### What is new?
#### Hierarchical Deterministic Wallet
The new feature of this version is the implementation of Hierarchical Deterministic Wallet. 
With this mnemonic seeds can be generated and addresses and private keys can be extracted.

The HDWallet implementation corresponds to the addresses of the lightwallet. 
So it is possible to find out private keys to addresses using the mnemonic Seeds of the lightwallet.
These private keys can then be imported into a defichain node wallet. 
With that is possible to control your lightwallet address.

More information about how to use the HDWallet can be found on the 
[documentation page](https://docs.defichain-python.de/build/html/api/hdwallet/index.html).

### What's next?
- implementation of new Ocean API methods
- implementation of the [Historic Defichain Data API](https://github.com/DeFiCh/dfips/issues/209) (when available)

### Here are some important links around the project:
- [Github](https://github.com/eric-volz/DefichainPython)
- [Documentation](https://docs.defichain-python.de/)
- [PyPI](https://pypi.org/project/defichain/)

If you have suggestions for improvement
or other ideas open an [issue](https://github.com/eric-volz/DefichainPython/issues), 
write me on [Twitter](https://twitter.com/Intr0c) or via email (introc@volz.link)!
