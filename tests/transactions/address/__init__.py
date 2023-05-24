from defichain.networks import DefichainMainnet, DefichainTestnet


class MainNet:
    NETWORK: str = DefichainMainnet
    PUBLIC_KEY: str = "024d40d6f9f2f7d2eb29d5e51821a6fe30d234f4149ea18d463dd8c8953424c26b"
    PRIVATE_KEY: str = "c91e3def568e2a4e02f3c85d80a670ee2dceb4ea705cec2ad47680559b53fe95"
    WIF: str = "L3xf8c8MurLA5Tk9cDyJah5osXyXYatW4QASHMjxY9PDWRTbSjA9"

    P2PKH: str = "8Zcnw7Nx5VUNAp7zuopA3hZwHzEYFe79pT"
    P2PKH_SCRIPTPUBLICKEY: str = "76a914cb4bfead9eadc9511d25a4fb3e8de5dbd0694ede88ac"
    P2PKH_DECODE: str = "12cb4bfead9eadc9511d25a4fb3e8de5dbd0694ede521c1e20"
    P2PKH_REDEEMSCRIPT: str = "76a914cb4bfead9eadc9511d25a4fb3e8de5dbd0694ede88ac"
    P2PKH_PUBLICKEYHASH: str = "cb4bfead9eadc9511d25a4fb3e8de5dbd0694ede"

    P2SH: str = "da1eYcsdX8BSDjjCHnVsVwiGshqzXmYXmy"
    P2SH_SCRIPTPUBLICKEY: str = "a914e1e220e587448ecc5b422accf7b741bccd140c1987"
    P2SH_DECODE: str = "5ae1e220e587448ecc5b422accf7b741bccd140c192a41c300"
    P2SH_REDEEMSCRIPT: str = "a914e1e220e587448ecc5b422accf7b741bccd140c1987"

    P2WPKH: str = "df1qed9latv74hy4z8f95nanar09m0gxjnk7uxjhrr"
    P2WPKH_SCRIPTPUBLICKEY: str = "0014cb4bfead9eadc9511d25a4fb3e8de5dbd0694ede"
    P2WPKH_DECODE: str = "cb4bfead9eadc9511d25a4fb3e8de5dbd0694ede"
    P2WPKH_REDEEMSCRIPT: str = "76a914cb4bfead9eadc9511d25a4fb3e8de5dbd0694ede88ac"
    P2WPKH_PUBLICKEYHASH: str = "cb4bfead9eadc9511d25a4fb3e8de5dbd0694ede"


class TestNet:
    NETWORK: str = DefichainTestnet
    PUBLIC_KEY: str = "024d40d6f9f2f7d2eb29d5e51821a6fe30d234f4149ea18d463dd8c8953424c26b"
    PRIVATE_KEY: str = "c91e3def568e2a4e02f3c85d80a670ee2dceb4ea705cec2ad47680559b53fe95"
    WIF: str = "cUKebX8DLv2REuDQzdnRx1asVmGwD2zC8SJuPnCU3G3DmATVf1zN"

    P2PKH: str = "7MbyynV5wx5jiWhjqYpCbKkaQUTiA5CWq8"
    P2PKH_SCRIPTPUBLICKEY: str = "76a914cb4bfead9eadc9511d25a4fb3e8de5dbd0694ede88ac"
    P2PKH_DECODE: str = "0fcb4bfead9eadc9511d25a4fb3e8de5dbd0694edea5a4bcd3"
    P2PKH_REDEEMSCRIPT: str = "76a914cb4bfead9eadc9511d25a4fb3e8de5dbd0694ede88ac"
    P2PKH_PUBLICKEYHASH: str = "cb4bfead9eadc9511d25a4fb3e8de5dbd0694ede"

    P2SH: str = "trrZxkCaVynjJD2VDj9yvi4AnsdqXcPkA4"
    P2SH_SCRIPTPUBLICKEY: str = "a914e1e220e587448ecc5b422accf7b741bccd140c1987"
    P2SH_DECODE: str = "80e1e220e587448ecc5b422accf7b741bccd140c1900e59e79"
    P2SH_REDEEMSCRIPT: str = "a914e1e220e587448ecc5b422accf7b741bccd140c1987"

    P2WPKH: str = "tf1qed9latv74hy4z8f95nanar09m0gxjnk70kgyr8"
    P2WPKH_SCRIPTPUBLICKEY: str = "0014cb4bfead9eadc9511d25a4fb3e8de5dbd0694ede"
    P2WPKH_DECODE: str = "cb4bfead9eadc9511d25a4fb3e8de5dbd0694ede"
    P2WPKH_REDEEMSCRIPT: str = "76a914cb4bfead9eadc9511d25a4fb3e8de5dbd0694ede88ac"
    P2WPKH_PUBLICKEYHASH: str = "cb4bfead9eadc9511d25a4fb3e8de5dbd0694ede"
