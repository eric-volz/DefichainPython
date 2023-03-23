# Bringing Python for Defichain to the next level!🚀🐍

Hey to all #Defighters,

it’s now been 1 year since I started this project and I wanted to give you an update on the current development.

I first want wo talk about the really exiting stuff!💣

## 1. Integration of Raw Transactions

I am currently working on the ability to create, sign and broadcast transactions using just python. 

### What is a raw transaction?

A raw transaction is a hexadecimal data string and always looks something like this. 

```
040000000001018605b44cda16f8828a406f4e4377c75b9508930b7cd343729dab1f56fbe19d1d0100000000ffffffff020000000000000000506a
4c4d446654787316001404c7767d2009c6dabe47d27a77406141c289376a0000e1f5050000000016001404c7767d2009c6dabe47d27a77406141c2
89376a016300000000000000ffe0f5050000000000fced052a0100000016001404c7767d2009c6dabe47d27a77406141c289376a00024830450221
00b11e61ff38835e09e5f4b4e5417808b99e1ddd3ccf792a60f929db22d3a93a2802203a3a69be756a4451e9461b1d795a13f0c837e104cc708101
7c3dfd844529c21c012103a5c791ba2a9c2668fc10b095e742b971d7acd50ffa77d6b40b9974937cb6064e00000000
```

This hexadecimal data string represents a [poolswap transaction](https://defiscan.live/transactions/1fcbdcd1b18753fb24dcaeb259fffeb84123e29e04db688b37522fbe8ce49365?network=TestNet) 
on the blockchain.

Creating these transactions requires a high level of understanding and can be very complex.

### What does the new implementation do?

The new transaction implementation in the DefichainPython library try’s to enable the user to create these raw 
transaction in a very intuitive and easy way. The goal is that the user can create these transactions like they would 
interact with a full node.

As an example the creation of a poolswap transaction:

```
tx = txbuilder.pool.poolswap(addressFrom, tokenFrom, amountFrom, addressTo, tokenTo, maxPrice)
```

The **tx** variable now contains the fully signed poolswap transaction that can be submitted directly to the blockchain. 
Everything is handled automatically in the background. 

To create a transactions some information from the blockchain is required. The needed information can be retrieved from 
the Ocean API. There is also the possibility to retrieve this information directly from a defichain node or to 
insert this information manually if you want to stay fully offline while creating a transaction.

### What does it make so special?

In the past creation of raw transactions could only be achieved by using the Jellyfish SDK from BirthdayResearch, witch 
is based on Typescript. So anyone who wanted to use python to execute transactions always had to rely on a running node. 
That is now no longer the case!

Furthermore, I try to make this implementation as user-friendly as possible. So anyone who has worked with a defichain 
node in the past will have no problems getting to know this new way of creating and broadcasting transactions.

This gives you for example the possibility to automate your lightwallet very easily and without large server costs.

### Do you want to test it?

I have written a [“Basic usage of transactions”](https://docs.defichain-python.de/build/html/additional/basicUsageOfRawTransactions.html#) 
Guide. You can follow this Guide to successfully create and broadcast your first transaction with python.

But please be careful using it, it’s an MVP and has not been tested extensively. There could still be significant errors 
inside the code that could lead to a total loss of funds.

I would really appreciate if you could leave some feedback in the comments or per [Twitter](https://twitter.com/Intr0c) 
DM🙂
- Did everything work?
- Is there anything that needs to be improved?
- How was the User Experience?

### Current status of the project

The current development is an MVP and is still limited in its functionality. All methods will be added, properly 
documented and tested in the next months.

**What is already implemented?**

- All needed methods to create and sign native UTXO transactions (for advanced users)
    - This is the base for creating transaction
- Creating transactions for P2SH and P2WPKH addresses
- Deserialize almost every raw transaction
    - the corresponding defi transaction must also be implemented
- UTXO Transactions
    - sendAll (Send all UTXO on an address to specified address)
    - send (Send a specified amount of UTXO to a specified address)
- Defi Transactions
    - UtxosToAccount
    - AccountToAccount
    - Poolswap

The current development of transactions can be viewed 
[here](https://github.com/eric-volz/DefichainPython/tree/main/defichain/transactions)!

**What is planed?**

1. Implement all essential defi transactions
    - AccountToUtxos
    - PoolAddLiquidity
    - PoolRemoveLiquidity
    - CompositeSwap
    - DepositToVault
    - WithdrawFromVault
    - ...
2. Wallet and Account Encryption
3. Logging
4. Test and document every essential method
5. Adding support for transactions with P2PKH address
6. Implement, test and document all remaining defi
7. Some special custom transactions?!

## 2. Update on my second CFP

As of the time I submitted my second CFP almost everything I promised was already implemented and ready to use. 

There was just one thing I promised to implement on a later stage. I talked about implementing the API provided by 
the **Defichain Lense** project. This project promised to deliver desperately needed historical data for a tax report 
and also an API to access this historical data.

As of now this project seems to be not implemented. So accordingly nothing has been built into the library either.

**Thus, my second CFP has not yet been fulfilled!**

### What I will do:

I will wait until either Defichain Lense launches its service or a different API witch is worth implementing comes 
along.

If you already have some suggestions which API I should integrate, feel free to comment or write me a DM.

## Conclusion

I hope you got a good overview about the current development. If anything is not clear or if you have some questions, 
don’t hesitate to ask!😉 I am happy about any feedback!🙂

### Important Project Links

- [GitHub](https://github.com/eric-volz/DefichainPython)
- [PyPi](https://pypi.org/project/defichain/)
- [Twitter](https://twitter.com/Intr0c)