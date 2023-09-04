# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import requests
from typing import Any, Dict
sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------

project = 'DefichainPython'
copyright = '2023, Intr0c'
author = 'Intr0c'

# The full version, including alpha/beta/rc tags
from setup import VERSION
release = 'v' + VERSION


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    'sphinx_mdinclude',
    'sphinx_inline_tabs',
    'sphinxemoji.sphinxemoji',
    'sphinx_copybutton',
    'sphinx_sitemap',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Autodoc member order
autodoc_member_order = "bysource"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = 'furo'
html_title = f"DefichainPython {release}"
language = "en"

sitemap_url_scheme = "{link}"
html_baseurl = 'https://docs.defichain-python.de/build/html/'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

html_static_path = ["_static"]
html_theme_options = {
    "announcement": "A new CFP has just been uploaded: "
                    "Feedback about the project would be really appreciated on reddit!❤️",
}
html_favicon = 'logo/logo.png'

# Code Blocks
code_blocks = [{"url": "https://gist.githubusercontent.com/eric-volz/964cbb9ab2906c132632689b99b1fcab/raw/6ef58341fba7a5f0f544de14d49dcccab49f4281/multiple_transactions_in_one_block.py", "filename": "guides/example/chainedTransactions.py"},
               {"url": "https://gist.githubusercontent.com/eric-volz/987579be543cbb72c2c5bffaedea105b/raw/1aa5f9bb891d1fdd3759ca34f79a6a0b2a2674a8/defichainExtractPrivateKeys.py", "filename": "guides/example/extractPrivateKeys.py"},
               ]


def load_code():
    for code_block in code_blocks:
        raw_code = requests.get(code_block.get("url")).text
        with open(code_block.get("filename"), "w") as f:
            f.write(raw_code)


load_code()
