from setuptools import setup, find_packages
from os import path

VERSION = '3.0.0'
DESCRIPTION = 'Defichain Python Library'

# Project URLs
project_urls = {
    "Tracker": "https://github.com/eric-volz/DefichainPython",
    "Documentation": "https://docs.defichain-python.de"
}

this_directory = path.abspath(path.dirname(__file__))


def long_description():
    with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
        LONG_DESCRIPTION = f.read()
    return LONG_DESCRIPTION


def requirements():
    with open("requirements.txt", "r") as _requirements:
        requirement: list = list(map(str.strip, _requirements.read().split("\n")))
    return requirement


# Setting up
if __name__ == "__main__":
    setup(
        name="defichain",
        version=VERSION,
        author="Intr0c",
        author_email="introc@volz.link",
        url="https://github.com/eric-volz/DefichainPython",
        description=DESCRIPTION,
        long_description=long_description(),
        packages=["defichain"] + ["defichain." + package for package in find_packages(where="defichain")],
        package_data={'': ['*.txt', '*.json']},
        install_requires=requirements(),
        keywords=['python', 'defichain', 'node', 'ocean', 'mnemonic', 'wallet', 'privateKey', 'transactions',
                  'raw transactions', 'P2PKH', 'P2SH', 'P2WPKH', 'DefiTx', 'custom transaction'],
        classifiers=[
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Operating System :: Unix",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
    )
