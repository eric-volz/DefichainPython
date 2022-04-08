[![Downloads](https://static.pepy.tech/personalized-badge/defichain?period=total&units=international_system&left_color=blue&right_color=green&left_text=Downloads)](https://pepy.tech/project/defichain)

# [DefichainPython](https://github.com/eric-volz/DefichainPython)

## This library is not finished yet and therefore should not be used in production!

## Welcome to Defichain's Python Library
___
Welcome to the Python Library for the Defichain! 

In this library all RPC commands of a [Defichain Node](https://defichain.com/downloads) are available and can be 
called in a few lines of code!

But first we need to install it:

### Installation
```bash
pip install defichain
```

### Example Code
```python
from defichain import Node

node = Node("127.0.0.1", 8554, "user", "password")

node.blockchain.getblockcount() #  returns block height of the latest block

node.poolpair.compositeswap("fromAddress", "BTC", 0.01, "toAddress", "DFI")  # swaps 0.01 BTC to DFI
```

## Progress and Updates
___

### Up to date to the node version: [v2.7.0 - Fort Canning Road](https://github.com/DeFiCh/ain/releases/tag/v2.7.0)

:heavy_check_mark: = Finished and UpToDate

:heavy_minus_sign: = In Production or not UpToDate

:heavy_multiplication_x: = Not yet implemented

### RPC 
| RPC Parts       | Progress           |
|-----------------|--------------------|
| Accounts        | :heavy_check_mark: |
| Blockchain      | :heavy_check_mark: | 
| Control         | :heavy_check_mark: |
| Generating      | :heavy_check_mark: |
| Loan            | :heavy_check_mark: |
| Masternodes     | :heavy_check_mark: |
| Mining          | :heavy_check_mark: |
| Network         | :heavy_check_mark: |
| Oracles         | :heavy_check_mark: |
| Poolpair        | :heavy_check_mark: |
| Rawtransactions | :heavy_check_mark: |
| Spv             | :heavy_minus_sign: |
| Tokens          | :heavy_check_mark: |
| Util            | :heavy_check_mark: |
| Vault           | :heavy_check_mark: |
| Wallet          | :heavy_check_mark: |
| Zmq             | :heavy_check_mark: |

### Ocean Requests
| Ocean Requests | Progress                 |
|----------------|--------------------------|
| Address        | :heavy_multiplication_x: |
| Blocks         | :heavy_multiplication_x: | 
| Fee            | :heavy_multiplication_x: |
| Loan           | :heavy_multiplication_x: |
| Masternodes    | :heavy_multiplication_x: |
| Oracles        | :heavy_multiplication_x: |
| Poolpairs      | :heavy_multiplication_x: |
| Prices         | :heavy_multiplication_x: |
| RawTx          | :heavy_multiplication_x: |
| stats          | :heavy_multiplication_x: |
| Tokens         | :heavy_multiplication_x: |
| Transactions   | :heavy_multiplication_x: |

## Next Steps
- Finish the RPC Code
- Write unit tests for RPC commands
- Document all functions and publish it on [ReadTheDocs](https://readthedocs.org/)
- Implement Ocean requests to query Data without a Node

## Community
This [project](https://github.com/DeFiCh/dfips/issues/133) is funded by the Defichain Community:
Thank you for your trust! If you have suggestions for improvement
or other ideas open an [issue](https://github.com/eric-volz/DefichainPython/issues), 
write me on [Twitter](https://twitter.com/Intr0c) or via email (introc@volz.link)!

## License & Disclaimer
By using (this repo), you (the user) agree to be bound by the 
[terms of this license](https://github.com/eric-volz/defichainLibrary/blob/main/LICENSE) (MIT License).
