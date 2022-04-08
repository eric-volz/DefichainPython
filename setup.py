from setuptools import setup, find_packages
from os import path

VERSION = '0.0.2'
DESCRIPTION = 'Defichain Python Library'

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
    packages=find_packages(),
    install_requires=["requests"],
    keywords=['python', 'defichain', 'node', 'ocean'],
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
