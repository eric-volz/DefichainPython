from setuptools import setup
from os import path

VERSION = '1.2.0'
DESCRIPTION = 'Defichain Python Library'

# Project URLs
project_urls = {
    "Tracker": "https://github.com/eric-volz/DefichainPython",
    "Documentation": "https://docs.defichain-python.de"
}

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

# Setting up
setup(
    name="defichain",
    version=VERSION,
    author="Intr0c",
    author_email="introc@volz.link",
    url="https://github.com/eric-volz/DefichainPython",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=['defichain',
              'defichain.exceptions',
              'defichain.exceptions.http',
              'defichain.exceptions.hdwallet',
              'defichain.mnemonic',
              'defichain.mnemonic.wordlist',
              'defichain.networks',
              'defichain.node',
              'defichain.node.modules',
              'defichain.ocean',
              'defichain.ocean.modules',
              'defichain.hdwallet',
              'defichain.hdwallet.libs'],
    install_requires=["requests", "ecdsa", "sha3", "base58", "six"],
    keywords=['python', 'defichain', 'node', 'ocean', 'mnemonic', 'wallet', 'privateKey'],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)