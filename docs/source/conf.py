# -*- coding: utf-8 -*-
import os
import sys

html_theme = "furo"
sys.path.insert(0, os.path.abspath("../../src"))
sys.path.insert(0, os.path.abspath("../../src/util"))

project = "Courier"
copyright = "2023, Joshua Rose"
author = "Joshua Rose"

# version info
version = "0.1"
release = "0.1.1"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx.ext.doctest",
    "sphinx_design",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"
language = "en"
pygments_style = "sphinx"

htmlhelp_basename = "courier"

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

epub_exclude_files = ["search.html"]

intersphinx_mapping = {"https://docs.python.org/": None}
