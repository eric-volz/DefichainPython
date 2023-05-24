# DefichainPython Tests

## Intention:

### Node & Ocean

The task of the test is to guarantee the always same functionality of all classes and methods

I assume that all methods are implemented correctly.

The task of the tests is therefore not to test the correctness of the return of a method, 
this is the task of a correct node software.

### HDWallet

The tests of hdwallet are verifying the correctness of the implementation.

## Preconditions

### Node

1. a fix address for all tests for node
2. a vault on the same address
3. have funds on the listed places
   - 0.5 <= UTXO <= 2 on address
   - DFI Token >= 0.01 on address
   - DUSD >= 0.01 on address
   - vault with big collateralization ratio
4. create a **secrets_conf.py** and fill out all mandatory information
5. check if everything is set up properly with the check_setup.py script

### Ocean & HDWallet

There are no preconditions for the tests of ocean and hdwallet.

## Testing

### Install requirements

```bash
pip install -r requirements_tests.txt
```

### Run tests

#### Run all tests

```bash
cd tests
pytest
```

#### Run specific tests
```bash
cd tests
pytest node
pytest ocean
pytest hdwallet
```