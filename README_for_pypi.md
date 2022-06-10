[![PyPI Version](https://img.shields.io/pypi/v/defichain.svg?color=green)](https://pypi.org/project/defichain)
[![PyPI Python Version](https://img.shields.io/pypi/pyversions/defichain.svg)](https://pypi.org/project/defichain)
[![Documentation Status](https://readthedocs.org/projects/pytest/badge/?version=latest)](https://docs.defichain-python.de/)
[![Downloads](https://static.pepy.tech/personalized-badge/defichain?period=total&units=international_system&left_color=grey&right_color=green&left_text=Downloads)](https://pepy.tech/project/defichain)

# [DefichainPython](https://github.com/eric-volz/DefichainPython)

## Welcome to Defichain's Python Library
___
Welcome to the Python Library for the Defichain! 

In this library all RPC commands of a [Defichain Node](https://defichain.com/downloads) are available and can be 
called in a few lines of code!

If you just want to query data from the blockchain you can also use the Ocean API: you don't need a Defichain Node for 
this, just an internet connection!

But first we need to install it:

### Installation
```bash
pip install defichain
```

### Example Code for RPC
```python
from defichain import Node

node = Node("user", "password", "127.0.0.1", 8554)

node.blockchain.getblockcount() #  returns block height of the latest block

node.poolpair.compositeswap("fromAddress", "BTC", 0.01, "toAddress", "DFI")  # swaps 0.01 BTC to DFI
```

### Example Code for Ocean API
```python
from defichain import Ocean

ocean = Ocean() #  creates the connection to Ocean

ocean.blocks.list() #  returns the latest 30 blocks 

ocean.poolpairs.get(4) #  returns data from ETH-DFI Pool
```

## Next Steps
- Document all methods and publish it on [docs.defichain-python.de](https://docs.defichain-python.de/)

## Community
This [project](https://github.com/DeFiCh/dfips/issues/133) is funded by the Defichain Community:
Thank you for your trust! If you have suggestions for improvement
or other ideas open an [issue](https://github.com/eric-volz/DefichainPython/issues), 
write me on [Twitter](https://twitter.com/Intr0c) or via email (introc@volz.link)!

## License & Disclaimer
By using (this repo), you (the user) agree to be bound by the 
[terms of this license](https://github.com/eric-volz/defichainLibrary/blob/main/LICENSE) (MIT License).