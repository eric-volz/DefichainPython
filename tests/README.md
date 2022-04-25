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
```bash
cd tests # navigate into the tests folder

pytest run_tests.py # run tests
```
--> no test should fail