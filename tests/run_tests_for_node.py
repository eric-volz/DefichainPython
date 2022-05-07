import sys
import os

from tests.node.util import createNode

MODULES = ["accounts", "blockchain", "control", "generating", "loan", "masternodes", "mining", "network", "oracles",
           "poolpair", "rawtransaction", "spv", "tokens", "util", "vault", "wallet", "zmq", "node", "exceptions"]
MARKER = ["mandatory", "query", "transaction"]

# Parameter Handling
args = sys.argv
if len(args) == 1:
    module = "all"
    marker = "all"
elif len(args) == 3:
    module = args[1]
    marker = args[2]
else:
    raise Exception("Use none or both parameters, not just one!\n"
                    "1. Parameter Modules: name of module to test or all for every module\n"
                    "2. Parameter Marker: name of marker to do the tests on or all for every marker\n")

if module != "all" and not module in MODULES:
    raise Exception(f"The passed parameter is not supported: {module}")
if marker != "all" and not marker in MARKER:
    raise Exception(f"The passed parameter is not supported: {marker}")

# Test Node before tests
createNode()


# Test Handling
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

