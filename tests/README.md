# DefichainPython Tests

## Intention:
The task of the test is to guarantee the always same functionality of all classes and methods

I assume that all methods are implemented correctly.

The task of the tests is therefore not to test the correctness of the return of a method, 
this is the task of a correct node software.

## Precondition to run the test:
### 1. You have to download the python package "pytest"
```bash
pip install pytest
```
### 2. Start your Defichain Node without any extra parameters (just --daemon allowed)
```bash
# Navigate to the folder where your node files are stored.

./bin/defid # runs the Node in the most basic way
```
### 3. Configure your connection:
    - copy secrets_conf.example.py and save it as secrets_conf.py
    - fill in all mandatory and optional information if needed

### 4. Set up a vault
   - create a vault on given address in secrets_conf
   - put the vault id into the secrets_conf file
   - fill your vault at least with a dollar worth of collateral

### 5. Check if everything is properly set up
   #### The automatic way:
   - use a separate wallet if you use this script 
     - it will send all UTXOs from the wallet to the given address
   ```bash
   cd tests # navigate into the tests folder
   
   python3 prepare_address.py # this script prepares your address for the tests
   ```
   #### The manual way:
   - make sure that your address has the tokens specified here
   1. UTXO: 0.5 <= UTXO <= 2
   2. DFI: DFI >= 0.01
   3. DUSD: DUSD >= 0.1
   4. vault with a big collateralization ratio

## Run the test:
### Test all modules:
```bash
cd tests # navigate into the tests folder

pytest node  # run all tests for node / rpc

pytest ocean  # run all tests for ocean
```
### More specified testing:
```bash
cd tests # navigate into the tests folder

pytest node/test_blockchain.py # tests just the module blockchain from the node / rpc
pytest ocean/test_poolpairs.py 

pytest node -k query # executes just the tests that are marked with query
pytest ocean -k query # executes just the tests that are marked with query
pytest node/test_accounts.py -k transaction # executes just the tests that are marked with transaction
```
--> no test should fail

## Progess of Tests

:heavy_check_mark: = Finished and UpToDate

:heavy_minus_sign: = In Production or not UpToDate

:heavy_multiplication_x: = Not yet implemented

### RPC 
| RPC Parts       | Progress                 |
|-----------------|--------------------------|
| Accounts        | :heavy_check_mark:       |
| Blockchain      | :heavy_check_mark:       | 
| Control         | :heavy_check_mark:       |
| Generating      | :heavy_check_mark:       |
| Loan            | :heavy_check_mark:       |
| Masternodes     | :heavy_check_mark:       |
| Mining          | :heavy_check_mark:       |
| Network         | :heavy_check_mark:       |
| Oracles         | :heavy_check_mark:       |
| Poolpair        | :heavy_check_mark:       |
| Rawtransactions | :heavy_multiplication_x: |
| Spv             | :heavy_multiplication_x: |
| Stats           | :heavy_check_mark:       |
| Tokens          | :heavy_check_mark:       |
| Util            | :heavy_check_mark:       |
| Vault           | :heavy_check_mark:       |
| Wallet          | :heavy_multiplication_x: |
| Zmq             | :heavy_check_mark:       |
|                 |                          |
| Node Connection | :heavy_check_mark:       |
| Exceptions      | :heavy_multiplication_x: |


### Ocean Requests
| Ocean Requests   | Progress                 |
|------------------|--------------------------|
| Address          | :heavy_check_mark:       |
| Blocks           | :heavy_check_mark:       | 
| Fee              | :heavy_check_mark:       |
| Loan             | :heavy_check_mark:       |
| Masternodes      | :heavy_check_mark:       |
| Oracles          | :heavy_check_mark:       |
| Poolpairs        | :heavy_check_mark:       |
| Prices           | :heavy_check_mark:       |
| RawTx            | :heavy_check_mark:       |
| RPC              | :heavy_check_mark:       |
| stats            | :heavy_check_mark:       |
| Tokens           | :heavy_check_mark:       |
| Transactions     | :heavy_check_mark:       |
|                  |                          |
| Ocean Connection | :heavy_check_mark:       |
| Exceptions       | :heavy_multiplication_x: |