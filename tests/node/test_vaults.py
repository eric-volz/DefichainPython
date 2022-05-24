import pytest
from tests.util import createNode, load_secrets_conf, LENGTH_OF_TXID

# Import Exceptions
from defichain.exceptions.InternalServerError import InternalServerError
from defichain.exceptions.BadRequest import BadRequest

node = createNode()
address = load_secrets_conf()["wallet_address"]
vault = load_secrets_conf()["vault_address"]


@pytest.mark.query
def test_closevault():  # 01
    false_vault = "86bc836f30fdf840dd4eab7a314bf0ebc2f16be827475071fdb764ef04249505"
    string = ".* RPC_INVALID_ADDRESS_OR_KEY: Vault <86bc836f30fdf840dd4eab7a314bf0ebc2f16be827475071fdb764ef04249505> " \
             "does not found"
    with pytest.raises(InternalServerError, match=string):
        assert node.vault.closevault(false_vault, address)
    with pytest.raises(InternalServerError, match=string):
        assert node.vault.closevault(false_vault, address, [])
    with pytest.raises(InternalServerError, match=string):
        assert node.vault.closevault(vaultId=false_vault, to=address, inputs=[])


@pytest.mark.query
def test_createvault():  # 02
    string = ".* RPC_WALLET_ERROR: Insufficient funds"
    with pytest.raises(InternalServerError, match=string):
        assert node.vault.createvault(address)
    with pytest.raises(InternalServerError, match=string):
        assert node.vault.createvault(address, "MIN150", [])
    with pytest.raises(InternalServerError, match=string):
        assert node.vault.createvault(ownerAddress=address, loanSchemeId="MIN150", inputs=[])


@pytest.mark.query
def test_deposittovault():  # 03
    assert len(node.vault.deposittovault(vault, address, "0.00000001@DUSD")) == LENGTH_OF_TXID
    assert len(node.vault.deposittovault(vault, address, "0.00000001@DUSD", [])) == LENGTH_OF_TXID
    assert len(node.vault.deposittovault(vault, address, "0.00000001@DUSD", [])) == LENGTH_OF_TXID


@pytest.mark.query
def test_estimatecollateral():  # 04
    assert node.vault.estimatecollateral("1@DUSD", 200)
    assert node.vault.estimatecollateral("1@DUSD", 200, {"DFI": 1})
    assert node.vault.estimatecollateral(loanAmounts="1@DUSD", targetRatio=200, tokens={"DFI": 1})

