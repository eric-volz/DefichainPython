import pytest
# Import Exceptions
from defichain.exceptions.http.InternalServerError import InternalServerError

from . import node


@pytest.mark.query
def test_evmtx():  # 01
    evm_address = "0xB553De274BFc1293DC703B013464202fC65E3FDF"

    string = ".* RPC_TYPE_ERROR: Invalid amount"
    with pytest.raises(InternalServerError, match=string):
        assert node.evm.evmtx(evm_address, 0x0, 0x09184e72a000, 0x2710, evm_address, 0x1e4876e800)
    with pytest.raises(InternalServerError, match=string):
        assert node.evm.evmtx(_from=evm_address, nonce=0x0, gasPrice=0x09184e72a000, gasLimit=0x2710,
                              to=evm_address, value=0x1e4876e800)
    with pytest.raises(InternalServerError, match=string):
        assert node.evm.evmtx(_from=evm_address, nonce=0x0, gasPrice=0x09184e72a000, gasLimit=0x2710,
                              to=evm_address, value=0x1e4876e800, data=0x0)


@pytest.mark.query
def test_logvmmaps():  # 02
    assert node.evm.logvmmaps(0)
    assert node.evm.logvmmaps(type=0)


@pytest.mark.query
def test_vmmap():  # 03
    string = ".* RPC_INVALID_PARAMETER: Key not found: *."
    with pytest.raises(InternalServerError, match=string):
        assert node.evm.vmmap("1600000", 0)
    with pytest.raises(InternalServerError, match=string):
        assert node.evm.vmmap(input="1600000", type=0)
