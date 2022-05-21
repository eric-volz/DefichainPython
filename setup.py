from setuptools import setup
from os import path

VERSION = '0.0.8'
DESCRIPTION = 'Defichain Python Library'

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_for_pypi.md'), encoding='utf-8') as f:
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
              'defichain.node',
              'defichain.exceptions',
              'defichain.ocean',
              'defichain.node.modules',
              'defichain.ocean.modules'],
    install_requires=["requests"],
    keywords=['python', 'defichain', 'node', 'ocean'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
