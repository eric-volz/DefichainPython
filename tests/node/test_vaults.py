import pytest
from tests.util import createNode, load_secrets_conf, LENGTH_OF_TXID

# Import Exceptions
from defichain.exceptions.http.InternalServerError import InternalServerError
from defichain.exceptions.http.BadRequest import BadRequest

node = createNode()
address = load_secrets_conf()["wallet_address"]
vault = load_secrets_conf()["vault_address"]


@pytest.mark.query
def test_closevault():  # 01
    false_vault = "86bc836f30fdf840dd4eab7a314bf0ebc2f16be827475071fdb764ef04249505"
    string = ".* RPC_INVALID_ADDRESS_OR_KEY: Vault <86bc836f30fdf840dd4eab7a314bf0ebc2f16be827475071fdb764ef04249505> " \
             "not found"
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


@pytest.mark.transactions
def test_deposittovault():  # 03
    assert len(node.vault.deposittovault(vault, address, "0.00000001@DUSD")) == LENGTH_OF_TXID
    assert len(node.vault.deposittovault(vault, address, "0.00000001@DUSD", [])) == LENGTH_OF_TXID
    assert len(node.vault.deposittovault(vault, address, "0.00000001@DUSD", [])) == LENGTH_OF_TXID


@pytest.mark.query
def test_estimatecollateral():  # 04
    assert node.vault.estimatecollateral("1@DUSD", 200)
    assert node.vault.estimatecollateral("1@DUSD", 200, {"DFI": 1})
    assert node.vault.estimatecollateral(loanAmounts="1@DUSD", targetRatio=200, tokens={"DFI": 1})


@pytest.mark.query
def test_estimateloan():  # 05
    assert node.vault.estimateloan(vault, {"DUSD": 0.5, "TSLA": 0.5})
    assert node.vault.estimateloan(vault, {"DUSD": 0.5, "TSLA": 0.5}, 150)
    assert node.vault.estimateloan(vaultId=vault, tokens={"DUSD": 0.5, "TSLA": 0.5}, targetRatio=150)


@pytest.mark.query
def test_estimatevault():  # 06
    assert node.vault.estimatevault(["100@DFI", "0.00001@BTC"], ["0.05@TSLA"])
    assert node.vault.estimatevault(collateralAmounts=["100@DFI", "0.00001@BTC"], loanAmounts=["0.05@TSLA"])


@pytest.mark.query
def test_getvault():  # 07
    assert node.vault.getvault(vault)
    assert node.vault.getvault(vault, False)
    assert node.vault.getvault(vaultId=vault, verbose=False)


@pytest.mark.query
def test_listauctionhistory():  # 08
    assert node.vault.listauctionhistory() == []
    assert node.vault.listauctionhistory("mine", node.blockchain.getblockcount(),
                                         "63a41dbc6497a58f024b730ca27189cdd2da45a5f9adda78c02581de36345e18",
                                         0, 100) == []
    assert node.vault.listauctionhistory(identifier="all", maxBlockHeight=node.blockchain.getblockcount(),
                                         vaultId="63a41dbc6497a58f024b730ca27189cdd2da45a5f9adda78c02581de36345e18",
                                         index=0, limit=100)


@pytest.mark.query
def test_listauctions():  # 09
    result1 = node.vault.listauctions()
    assert result1 == [] or result1
    result2 = node.vault.listauctions("63a41dbc6497a58f024b730ca27189cdd2da45a5f9adda78c02581de36345e18", 0, False, 100)
    assert result2 == [] or result2
    result3 = node.vault.listauctions(vaultId="63a41dbc6497a58f024b730ca27189cdd2da45a5f9adda78c02581de36345e18",
                                      height=0, including_start=False, limit=100)
    assert result3 == [] or result3


@pytest.mark.query
def test_listvaulthistory():  # 10
    string = ".* RPC_INVALID_REQUEST: -vaultindex required for vault history"
    with pytest.raises(BadRequest, match=string):
        assert node.vault.listvaulthistory(vault)
    with pytest.raises(BadRequest, match=string):
        assert node.vault.listvaulthistory(vault, node.blockchain.getblockcount(), 1000, {}, 100)
    with pytest.raises(BadRequest, match=string):
        assert node.vault.listvaulthistory(vaultId=vault, maxBlockHeight=node.blockchain.getblockcount(), token=1000,
                                           txtype={}, limit=100)


@pytest.mark.query
def test_listvaults():  # 11
    assert node.vault.listvaults(address)
    assert node.vault.listvaults(address, "MIN150", "active", False, vault, True, 100)
    assert node.vault.listvaults(ownerAddress=address, loanSchemeId="MIN150", state="active", verbose=False,
                                 start=vault, including_start=True, limit=100)

@pytest.mark.query
def test_paybackwithcollateral():  # 12
    pass  # has to be implemented (tested manually)

@pytest.mark.query
def test_placeauctionbid():  # 13
    string = ".* RPC_TYPE_ERROR: amount: Invalid amount"
    with pytest.raises(InternalServerError, match=string):
        assert node.vault.placeauctionbid(vault, 0, address, "0.01DUSD")
    with pytest.raises(InternalServerError, match=string):
        assert node.vault.placeauctionbid(vault, 0, address, "0.01DUSD", [])
    with pytest.raises(InternalServerError, match=string):
        assert node.vault.placeauctionbid(vaultId=vault, index=0, _from=address, amount="0.01DUSD", inputs=[])


@pytest.mark.transactions
def test_updatevault():  # 14
    assert len(node.vault.updatevault(vault, address)) == LENGTH_OF_TXID
    assert len(node.vault.updatevault(vault, None, "MIN150")) == LENGTH_OF_TXID
    assert len(node.vault.updatevault(vault, address, None, [])) == LENGTH_OF_TXID
    assert len(node.vault.updatevault(vault, None, "MIN150", [])) == LENGTH_OF_TXID
    assert len(node.vault.updatevault(vaultId=vault, ownerAddress=address, inputs=[])) == LENGTH_OF_TXID
    assert len(node.vault.updatevault(vaultId=vault, loanSchemeId="MIN150", inputs=[])) == LENGTH_OF_TXID


@pytest.mark.transactions
def test_withdrawfromvault():  # 15
    assert len(node.vault.withdrawfromvault(vault, address, "0.00000001@DUSD")) == LENGTH_OF_TXID
    assert len(node.vault.withdrawfromvault(vault, address, "0.00000001@DUSD", [])) == LENGTH_OF_TXID
    assert len(node.vault.withdrawfromvault(vaultId=vault, to=address, amount="0.00000001@DUSD", inputs=[])) == \
           LENGTH_OF_TXID
