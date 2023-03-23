from binascii import hexlify, unhexlify
import struct
from hashlib import sha256
from ecdsa import SigningKey, SECP256k1
from ecdsa.util import sigencode_der

from defichain.transactions.constants import ORDER


def sign_input(privateKey: str, data: bytes) -> str:
    """
    Signs the given data with a given private key in a deterministic way

    :param privateKey: (required) private key to sign the input
    :type privateKey: str
    :param data: (required) data that has to be signed
    :type data: bytes
    :return: "hex" - signature of data
    """

    sk = SigningKey.from_string(unhexlify(privateKey), curve=SECP256k1)
    sig = sk.sign_digest_deterministic(data, sigencode=sigencode_der, hashfunc=sha256)

    der_prefix = sig[0]
    length_total = sig[1]
    der_type_int = sig[2]
    length_r = sig[3]
    R = sig[4:4 + length_r]
    length_s = sig[5 + length_r]
    S = sig[5 + length_r + 1:]
    S_as_bigint = int(hexlify(S).decode('utf-8'), 16)

    half_order = ORDER // 2
    if S_as_bigint > half_order:
        new_S_as_bigint = ORDER - S_as_bigint
        new_S = unhexlify(format(new_S_as_bigint, 'x').zfill(64))
        length_s -= 1
        length_total -= 1
    else:
        new_S = S

    sig = struct.pack('BBBB', der_prefix, length_total, der_type_int, length_r) + R + \
          struct.pack('BB', der_type_int, length_s) + new_S

    sig += struct.pack('B', 1)

    return hexlify(sig).decode('utf-8')
