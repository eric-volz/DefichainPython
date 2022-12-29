from setuptools import setup
from os import path

VERSION = '2.3.0'
DESCRIPTION = 'Defichain Python Library'

# Project URLs
project_urls = {
    "Tracker": "https://github.com/eric-volz/DefichainPython",
    "Documentation": "https://docs.defichain-python.de"
}

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

# requirements.txt
with open("requirements.txt", "r") as _requirements:
    requirements: list = list(map(str.strip, _requirements.read().split("\n")))

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
              'defichain.libs'
              'defichain.mnemonic',
              'defichain.mnemonic.wordlist',
              'defichain.networks',
              'defichain.node',
              'defichain.node.modules',
              'defichain.ocean',
              'defichain.ocean.modules',
              'defichain.hdwallet',
              'defichain.hdwallet'],
    package_data={'': ['*.txt']},
    install_requires=requirements,
    keywords=['python', 'defichain', 'node', 'ocean', 'mnemonic', 'wallet', 'privateKey'],
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
