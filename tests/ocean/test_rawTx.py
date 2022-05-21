import pytest
from defichain import Ocean
from defichain.exceptions.BadRequest import BadRequest

ocean = Ocean()


HEX = "0400000001616cd43cb0d396c52d6a5342f9411307a4dc4847f9237ff8bbb62e0c247be803010000006a4730440220119839df669bf6e" \
      "b24dd7b806cdb782ffc1ffa892fd663b5be6bf3d22cc9fdd9022028f4e981bcbcfbec0ff508a9b67fd353840ed3132c4528ecc894b90c" \
      "da49382f012102d9438499f4280c74afa1e9cf1d3df9cff599d05740d9355acc6be97f45575251fdffffff0262390f00000000001976a" \
      "9147d8c7b0c6e867e3034afc49eabc16ed33590400388ac007950d705000000001976a9147d8c7b0c6e867e3034afc49eabc16ed33590" \
      "400388ac0000000000"


@pytest.mark.query
def test_send():  # 01
    string = ".*'Missing inputs'"
    with pytest.raises(BadRequest, match=string):
        assert ocean.rawTx.send(HEX)
        assert ocean.rawTx.send(HEX, 0.001)
        assert ocean.rawTx.send(hex=HEX, maxFeeRate=0.001)


@pytest.mark.query
def test_test():  # 02
    string = ".*'Transaction is not allowed to be inserted'"
    with pytest.raises(BadRequest, match=string):
        assert ocean.rawTx.test(HEX)
        assert ocean.rawTx.test(HEX, 0.001)
        assert ocean.rawTx.test(hex=HEX, maxFeeRate=0.001)
