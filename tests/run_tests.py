import sys
import os

from tests.util import createNode

LIBRARY = ["node", "ocean"]
NODE_MODULES = ["accounts", "blockchain", "control", "generating", "loan", "masternodes", "mining", "network",
                "oracles", "poolpair", "rawtransaction", "spv", "tokens", "util", "vault", "wallet", "zmq", "node",
                "exceptions"]
OCEAN_MODULES = ["address", "blocks", "fee", "loan", "masternodes", "oracles", "poolpairs", "prices", "rawTx", "rpc",
                 "stats", "tokens", "transactions", "ocean", "exceptions"]
MARKER = ["mandatory", "query", "transaction"]

# Parameter Handling
args = sys.argv
if len(args) == 2:
    library = args[1]
    module = "all"
    marker = "all"
elif len(args) == 4:
    library = args[1]
    module = args[2]
    marker = args[3]
else:
    raise Exception("You have not set the parameters correctly!\n"
                    "1. (required) Parameter library: name of the library to be tested\n"
                    "2. (optional) Parameter Modules: name of module to test or all for every module\n"
                    "3. (optional) Parameter Marker: name of marker to do the tests on or all for every marker\n")

if not library in LIBRARY:
    raise Exception(f"The passed parameter is not supported: {library}")
if library == "node":
    if module != "all" and not module in NODE_MODULES:
        raise Exception(f"The passed parameter is not supported: {module}")
else:
    if module != "all" and not module in OCEAN_MODULES:
        raise Exception(f"The passed parameter is not supported: {module}")
if marker != "all" and not marker in MARKER:
    raise Exception(f"The passed parameter is not supported: {marker}")

# Test Node before tests
createNode()


# Test Handling
if library == "node":
    if module == "all" and marker == "all":
        stream = os.popen("pytest node")
        output = stream.read()
        print(output)
    elif module == "all":
        stream = os.popen(f"pytest node -k {marker}")
        output = stream.read()
        print(output)
    elif marker == "all":
        stream = os.popen(f"pytest node/test_{module}.py")
        output = stream.read()
        print(output)
    else:
        stream = os.popen(f"pytest node/test_{module}.py -k {marker}")
        output = stream.read()
        print(output)
else:
    if module == "all" and marker == "all":
        stream = os.popen("pytest ocean")
        output = stream.read()
        print(output)
    elif module == "all":
        stream = os.popen(f"pytest ocean -k {marker}")
        output = stream.read()
        print(output)
    elif marker == "all":
        stream = os.popen(f"pytest ocean/test_{module}.py")
        output = stream.read()
        print(output)
    else:
        stream = os.popen(f"pytest ocean/test_{module}.py -k {marker}")
        output = stream.read()
        print(output)

