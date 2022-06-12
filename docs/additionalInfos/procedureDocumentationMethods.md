# Procedure for documentation of methods

 1. Add **parameters** of method with **types**

 2. Add expected **Output** of method

 3. Create **doc string**

 4. Add **doc string** parameters with **types**

 5. Add the **description** of the method

 6. Specify whether the parameters are **required** or **optional**

 7. Add the **parameters descriptions**

 8. Add the **return** of the method

 9. Add **examples**

 10. **Build HTML**

## [Perfect Doc-string](https://docs.defichain-python.de/build/html/api/node/accounts.html#defichain.node.Accounts.getaccount)
 ```python
 def getaccount(self, owner: str, start: str = None, including_start: bool = None, limit: int = None,
                  indexed_amounts: bool = False) -> "[{...}]":  # 06
       """
       Returns information about account.

       :param owner: (required) Owner address in base58/bech32/hex encoding
       :type owner: str
       :param start: (optional) Optional first key to iterate from, in lexicographical order.Typically it's set to last tokenID from previous request.
       :type start: str
       :param including_start: (optional) If true, then iterate including starting position. False by default
       :type including_start: bool
       :param limit: (optional) Maximum number of orders to return, 100 by default
       :type limit: int
       :param indexed_amounts: (optional) Format of amounts output (default = false): (true: obj = {tokenid:amount,...}, false: array = ["amount@tokenid"...])
       :type indexed_amounts: bool
       :return: [{...}] (array) Json object with order information

       :example:

           >>> node.accounts.getaccount("mxxA2sQMETJFbXcNbNbUzEsBCTn1JSHXST")
       """
 ```
