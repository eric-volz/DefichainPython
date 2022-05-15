# DefichainPython Tests

## Intention:
The task of the test is to guarantee the always same functionality of all classes and methods

I assume that all methods are implemented correctly.

The task of the tests is therefore not to test the correctness of the return of a method, 
this is the task of a correct node software.

## Precondition to run the test:
1. You have to download the python package "pytest"
```bash
pip install pytest
```
2. Start your Defichain Node without any extra parameters (just --daemon allowed)
```bash
# Navigate to the folder where your node files are stored.

./bin/defid # runs the Node in the most basic way
```
3. Configure your connection:
    - copy secrets_conf.example.py and save it as secrets_conf.py
    - fill in all mandatory and optional information if needed

## Run the test:
1. (required) Parameter library: name of the library to be tested
```bash
cd tests # navigate into the tests folder

python3 run_tests.py node  # run all tests for node / rpc

python3 run_tests.py ocean  # run all tests for ocean
```
You can also filter tests by giving the script parameters:
2. (optional) Parameter Modules: name of module to test or all for every module
3. (optional) Parameter Marker: name of marker to do the tests on or all for every marker
```bash
cd tests # navigate into the tests folder

python3 run_tests.py node blockchain query # run all tests in the blockchain module with the marker query
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
| Loan            | :heavy_multiplication_x: |
| Masternodes     | :heavy_check_mark:       |
| Mining          | :heavy_check_mark:       |
| Network         | :heavy_check_mark:       |
| Oracles         | :heavy_check_mark:       |
| Poolpair        | :heavy_multiplication_x: |
| Rawtransactions | :heavy_multiplication_x: |
| Spv             | :heavy_multiplication_x: |
| Tokens          | :heavy_check_mark:       |
| Util            | :heavy_check_mark:       |
| Vault           | :heavy_multiplication_x: |
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