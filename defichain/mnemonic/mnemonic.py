#
# Copyright (c) 2013 Pavol Rusnak
# Copyright (c) 2017 mruddy
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import hashlib
import itertools
import os
import secrets
import unicodedata
from typing import AnyStr, List, TypeVar, Union

_T = TypeVar("_T")
PBKDF2_ROUNDS = 2048


class ConfigurationError(Exception):
    pass


# Refactored code segments from <https://github.com/keis/base58>
def b58encode(v: bytes) -> str:
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

    p, acc = 1, 0
    for c in reversed(v):
        acc += p * c
        p = p << 8

    string = ""
    while acc:
        acc, idx = divmod(acc, 58)
        string = alphabet[idx : idx + 1] + string
    return string


class Mnemonic(object):
    """
    Creates a mnemonic instance

    :param language: (optional) language of the mnemonic seed: english, chinese_simplified, chinese_traditional, french,
        italian, japanese, korean, spanish
    :type language: str
    :returns: Mnemonic -- Mnemonic instance.

    :example:

    >>> from defichain import Mnemonic
    >>> Mnemonic(language="english")
    """
    def __init__(self, language: str = "english"):
        self.language = language
        self.radix = 2048
        d = os.path.join(os.path.dirname(__file__), f"wordlist/{language}.txt")
        if os.path.exists(d) and os.path.isfile(d):
            with open(d, "r", encoding="utf-8") as f:
                self.wordlist = [w.strip() for w in f.readlines()]
            if len(self.wordlist) != self.radix:
                raise ConfigurationError(
                    f"Wordlist should contain {self.radix} words, but it's {len(self.wordlist)} words long instead."
                )
        else:
            raise ConfigurationError("Language not detected")
        # Japanese must be joined by ideographic space
        self.delimiter = "\u3000" if language == "japanese" else " "

    @classmethod
    def list_languages(cls) -> List[str]:
        """
        List all languages for mnemonic seed

        :return: (array) languages

        :example:

        >>> from defichain import Mnemonic
        >>> Mnemonic.list_languages()
        ['korean', 'japanese', 'chinese_simplified', 'english', 'french', 'italian', 'chinese_traditional', 'spanish']
        """
        return [
            f.split(".")[0]
            for f in os.listdir(os.path.join(os.path.dirname(__file__), "wordlist"))
            if f.endswith(".txt")
        ]

    @staticmethod
    def normalize_string(txt: AnyStr) -> str:
        if isinstance(txt, bytes):
            utxt = txt.decode("utf8")
        elif isinstance(txt, str):
            utxt = txt
        else:
            raise TypeError("String value expected")

        return unicodedata.normalize("NFKD", utxt)

    @classmethod
    def detect_language(cls, mnemonic: str) -> str:
        """
        Scan the Mnemonic until the language becomes unambiguous

        :param mnemonic: (required) the mnemonic seed
        :type mnemonic: str
        :return: (string) language of the mnemonic seed

        :example:

        >>> from defichain import Mnemonic
        >>> mnemonic = Mnemonic(language="english").generate()
        >>> Mnemonic.detect_language(mnemonic)
        "english"
        """
        code = cls.normalize_string(mnemonic)
        possible = set(cls(lang) for lang in cls.list_languages())
        for word in code.split():
            possible = set(p for p in possible if word in p.wordlist)
            if not possible:
                raise ConfigurationError(f"Language unrecognized for {word!r}")
        if len(possible) == 1:
            return possible.pop().language
        raise ConfigurationError(
            f"Language ambiguous between {', '.join( p.language for p in possible)}"
        )

    def generate(self, strength: int = 256) -> str:
        """
        Create a new mnemonic using a random generated number as entropy.

        As defined in BIP39, the entropy must be a multiple of 32 bits, and its size must be between 128 and 256 bits.
        Therefore the possible values for `strength` are 128, 160, 192, 224 and 256.

        If not provided, the default entropy length will be set to 128 bits.

        The return is a list of words that encodes the generated entropy.

        :param strength: (optional) Number of bytes used as entropy
        :type strength: int
        :return: (string) A randomly generated mnemonic

        :example:

        >>> from defichain import Mnemonic
        >>> mnemonic = Mnemonic(language="english")
        >>> mnemonic.generate()
        "shoulder unusual practice sight apart course eager true diesel rescue diagram denial oppose total fun rocket spend chapter spider paddle benefit empower type purse"
        """
        if strength not in [128, 160, 192, 224, 256]:
            raise ValueError(
                "Invalid strength value. Allowed values are [128, 160, 192, 224, 256]."
            )
        return self.to_mnemonic(secrets.token_bytes(strength // 8))

    # Adapted from <http://tinyurl.com/oxmn476>
    def to_entropy(self, words: Union[List[str], str]) -> bytearray:
        if not isinstance(words, list):
            words = words.split(" ")
        if len(words) not in [12, 15, 18, 21, 24]:
            raise ValueError(
                "Number of words must be one of the following: [12, 15, 18, 21, 24], but it is not (%d)."
                % len(words)
            )
        # Look up all the words in the list and construct the
        # concatenation of the original entropy and the checksum.
        concatLenBits = len(words) * 11
        concatBits = [False] * concatLenBits
        wordindex = 0
        for word in words:
            # Find the words index in the wordlist
            ndx = self.wordlist.index(word)
            if ndx < 0:
                raise LookupError('Unable to find "%s" in word list.' % word)
            # Set the next 11 bits to the value of the index.
            for ii in range(11):
                concatBits[(wordindex * 11) + ii] = (ndx & (1 << (10 - ii))) != 0
            wordindex += 1
        checksumLengthBits = concatLenBits // 33
        entropyLengthBits = concatLenBits - checksumLengthBits
        # Extract original entropy as bytes.
        entropy = bytearray(entropyLengthBits // 8)
        for ii in range(len(entropy)):
            for jj in range(8):
                if concatBits[(ii * 8) + jj]:
                    entropy[ii] |= 1 << (7 - jj)
        # Take the digest of the entropy.
        hashBytes = hashlib.sha256(entropy).digest()
        hashBits = list(
            itertools.chain.from_iterable(
                [c & (1 << (7 - i)) != 0 for i in range(8)] for c in hashBytes
            )
        )
        # Check all the checksum bits.
        for i in range(checksumLengthBits):
            if concatBits[entropyLengthBits + i] != hashBits[i]:
                raise ValueError("Failed checksum.")
        return entropy

    def to_mnemonic(self, data: bytes) -> str:
        if len(data) not in [16, 20, 24, 28, 32]:
            raise ValueError(
                f"Data length should be one of the following: [16, 20, 24, 28, 32], but it is not {len(data)}."
            )
        h = hashlib.sha256(data).hexdigest()
        b = (
            bin(int.from_bytes(data, byteorder="big"))[2:].zfill(len(data) * 8)
            + bin(int(h, 16))[2:].zfill(256)[: len(data) * 8 // 32]
        )
        result = []
        for i in range(len(b) // 11):
            idx = int(b[i * 11 : (i + 1) * 11], 2)
            result.append(self.wordlist[idx])
        return self.delimiter.join(result)

    def check(self, mnemonic: str) -> bool:
        """
        Checks if the mnemonic seed is valid

        :param mnemonic: (required) mnemonic seed
        :type mnemonic: str
        :return: bool

        :example:

        >>> from defichain import Mnemonic
        >>> mn = Mnemonic(language="english")
        >>> seed = mn.generate()
        >>> mn.check(seed)
        True
        """
        mnemonic_list = self.normalize_string(mnemonic).split(" ")
        # list of valid mnemonic lengths
        if len(mnemonic_list) not in [12, 15, 18, 21, 24]:
            return False
        try:
            idx = map(
                lambda x: bin(self.wordlist.index(x))[2:].zfill(11), mnemonic_list
            )
            b = "".join(idx)
        except ValueError:
            return False
        l = len(b)  # noqa: E741
        d = b[: l // 33 * 32]
        h = b[-l // 33 :]
        nd = int(d, 2).to_bytes(l // 33 * 4, byteorder="big")
        nh = bin(int(hashlib.sha256(nd).hexdigest(), 16))[2:].zfill(256)[: l // 33]
        return h == nh

    def expand_word(self, prefix: str) -> str:
        if prefix in self.wordlist:
            return prefix
        else:
            matches = [word for word in self.wordlist if word.startswith(prefix)]
            if len(matches) == 1:  # matched exactly one word in the wordlist
                return matches[0]
            else:
                # exact match not found.
                # this is not a validation routine, just return the input
                return prefix

    def expand(self, mnemonic: str) -> str:
        return " ".join(map(self.expand_word, mnemonic.split(" ")))\


    @classmethod
    def to_seed(cls, mnemonic: str, passphrase: str = "") -> bytes:
        mnemonic = cls.normalize_string(mnemonic)
        passphrase = cls.normalize_string(passphrase)
        passphrase = "mnemonic" + passphrase
        mnemonic_bytes = mnemonic.encode("utf-8")
        passphrase_bytes = passphrase.encode("utf-8")
        stretched = hashlib.pbkdf2_hmac(
            "sha512", mnemonic_bytes, passphrase_bytes, PBKDF2_ROUNDS
        )
        return stretched[:64]
