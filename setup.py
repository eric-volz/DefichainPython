from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Defichain Node and Ocean Library'

# Setting up
setup(
    name="defichain",
    version=VERSION,
    author="Intr0c (Eric Volzp)",
    author_email="introc@volz.link",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'defichain', 'node', 'ocean'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)