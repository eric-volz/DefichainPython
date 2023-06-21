## Overview
1. **Requester**: Eric Volz
2. **Amount requested in DFI**: 5000
3. **Receiving address**: df1qdx0mllcvvrdfcrstyvp2pu4szp2pct5njcgwev
4. **Reddit discussion thread**: [Provide a link to Reddit discussion thread]
5. **Proposal fee txid**: b0f4d4644a2378fbae44b68cd7b02f6b57be799fd313cf0b573d557c1f01cd46

---

## Recap

**Dear Defichain Community**,

As promised in the [first CFP](https://github.com/DeFiCh/dfips/issues/133), I have implemented, tested and documented all the methods of the defichain full node and 
the ocean API.

I have recently reworked the tests again to make them even better.
Tests for Linux, Windows and macOS are now [performed via GitHub](https://github.com/eric-volz/DefichainPython/actions/workflows/tests.yml).

The documentation of the methods is available within IDEs and on the [new documentation website](https://docs.defichain-python.de/build/html/index.html).

Here is an example of the documentation for the method "[getblock](https://docs.defichain-python.de/build/html/api/node/blockchain.html#defichain.node.Blockchain.getblock)":

getblock documentation for IDE:

![GitHub Clones Statistics](https://docs.defichain-python.de/additionalInfos/pictures/CFP_02/docs_getblock_ide.png)

getblock documentation for Website:

![GitHub Views Statistics](https://docs.defichain-python.de/additionalInfos/pictures/CFP_02/docs_getblock_web.png)

### User statistics

So that you can evaluate how many people this project helps, here are some download / clone and views numbers:

GitHub Traffic Data: 24.10.2022 - 06.10.2022

GitHub Clones Statistics:

![GitHub Clones Statistics](https://docs.defichain-python.de/additionalInfos/pictures/CFP_02/github_traffic_clones.png)

GitHub Views Statistics:

![GitHub Views Statistics](https://docs.defichain-python.de/additionalInfos/pictures/CFP_02/github_traffic_views.png)

Live updated download numbers of the Python Library from [PyPi](https://pypi.org/project/defichain/): 

Overall downloads:

[![Downloads](https://pepy.tech/badge/defichain)](https://pepy.tech/project/defichain)

Downloads within the last month:

[![Downloads](https://pepy.tech/badge/defichain/month)](https://pepy.tech/project/defichain)

Downloads within the last week:

[![Downloads](https://pepy.tech/badge/defichain/week)](https://pepy.tech/project/defichain)

To give these numbers a little more context:

If there is an update, the download numbers go up.
But there has been no major release nor announcement from my side in the last two weeks.

---

## What is part of this CFP?

### 1. Adding new methods (Already Implemented)
Since the first CFP, many additional methods have been added to the Node software and the Ocean API. Of course, I have 
always implemented, tested and documented them as soon as possible so that they could be used by the community.

### 2. [Creation of a documentation website](https://docs.defichain-python.de/build/html/index.html) (Already created)
To make the library even clearer, I decided to build a documentation website. 
This website should help everyone to get a quick overview and has even more detailed 
documentation than the documentation in the IDE.

The documentation website offers:
1. [Quickstart Guide](https://docs.defichain-python.de/build/html/instructions/quickstart.html)
2. Explanation of the main modules: 
[Node](https://docs.defichain-python.de/build/html/api/node/index.html), 
[Ocean](https://docs.defichain-python.de/build/html/api/ocean/index.html),
[HDWallet](https://docs.defichain-python.de/build/html/api/hdwallet/index.html), 
[Mnemonic](https://docs.defichain-python.de/build/html/api/mnemonic.html)
3. More detailed documentation about the methods of each module
4. [Progress and updates](https://docs.defichain-python.de/build/html/instructions/progressAndUpdates.html) page about this project
5. In the future: additional tutorials

Feel free to get an overview yourself :)

### 3. [Hierarchical Deterministic Wallet](https://docs.defichain-python.de/build/html/api/hdwallet/index.html) (Already Implemented)
With HD Wallet you can calculate everything about your own wallet.

The HDWallet uses the same calculation method as the Defichain Lightwallet. So it is now very easy to generate the 
private keys of the different addresses from a mnemonic seed of the lightwallet.

To give an example of use:

You can use the HDWallet and a mnemonic seed of the lightwallet to read the private key of an address and import it 
into a defichain full node.
With the imported private key, the address of the lightwallet can now also be controlled and managed via a full node.

It can be used within the Mainnet, Testnet and Regtest network.

To clarify: for any calculation in HDWallet no connection to the internet is needed (offline)

--> [Reddit Post](https://www.reddit.com/r/defiblockchain/comments/y7icf1/the_defichain_python_library_implements_hdwallet/)

### 4. [Implementation of Defichain Lense](https://github.com/DeFiCh/dfips/issues/209) (still to be implemented)
Defichain Lense is another community project that wants to provide account and historical pool data via an API.

When this project releases its API endpoints I will implement, test and document all endpoints, so they are easily 
accessible through this library.

--> [Defichain Lense Main Page](https://defilense.com/)

---

## How will the fund be spent?

The funds are used to cover the research and development effort.

---

## How does this CFP benefit the DeFiChain community?
All these new features make the development of Python projects much easier and faster. 
The barrier to entry into the Defichain ecosystem is getting smaller and new developers are attracted.

By implementing HDWallet, anyone who wants to know his private key can easily find it out. This also applies to 
non-developer, since this process is very simple.

Even long-awaited historical pool data through Defichain Lense can then be retrieved via the API, without any further 
hassle and so save time while developing.

---

### Summarized Important Links
- [Github](https://github.com/eric-volz/DefichainPython)
- [Documentation](https://docs.defichain-python.de/)
- [PyPI](https://pypi.org/project/defichain/)

If you have suggestions for improvement or other ideas open an [issue](https://github.com/eric-volz/DefichainPython/issues),
write me on [Twitter](https://twitter.com/Intr0c) or via email (introc@volz.link)!

**Thank you for voting and feel free to ask if you have any questions :)**
