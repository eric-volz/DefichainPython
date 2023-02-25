from defichain.networks import DefichainMainnet, DefichainTestnet
import copy


def define_fee(tx, network: DefichainMainnet or DefichainTestnet, keys: [], feePerByte):
    """
    Signes the transaction to find out the real size


    :param tx: (required) the transaction object
    :type tx: Transaction
    :param network: (required) Network
    :type network: DefichainMainnet or DefichainTestnet
    :param keys: (required) array with all needed keys to sign the transaction
    :type keys: [str]
    :param feePerByte: (required) the amount of fee to pay per byte
    :type feePerByte: float
    :return: "int" - the amount of fee to pay
    """
    copy_tx = copy.deepcopy(tx)
    copy_tx.sign(network, keys)
    return round(copy_tx.size() * feePerByte)
