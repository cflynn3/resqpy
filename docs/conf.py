# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# See also https://wwoods.github.io/2016/06/09/easy-sphinx-documentation-without-the-boilerplate/#setup

# Nb. useful stackexchange thread about the :recursive: option and custom templates:
# https://stackoverflow.com/questions/2701998/sphinx-autodoc-is-not-automatic-enough/62613202#62613202


# -- Path setup --------------------------------------------------------------

# Point to the current working copy of resqml
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..',)))

# Mock imports for things not available
# autodoc_mock_imports = ["h5py"]

# -- Project information -----------------------------------------------------

project = 'resqpy'
copyright = '2021, BP'
author = 'BP'

release = 'PreRelease'
version = 'PreRelease'


# -- General configuration ---------------------------------------------------

autoclass_content = "both"  # include both class docstring and __init__
# autodoc_default_options = {
#     'members': None,
#     'inherited-members': None,
#     'private-members': None,
#     'show-inheritance': None,
# }
autosummary_generate = True  # Make _autosummary files and include them
autosummary_generate_overwrite = True

napoleon_use_rtype = False  # More legible
autodoc_member_order = 'bysource'
# napoleon_numpy_docstring = False  # Force consistency, leave only Google

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',     # Add a link to the Python source code for classes, functions etc.
]

templates_path = ['_templates']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

# Override table width restrictions
# See https://rackerlabs.github.io/docs-rackspace/tools/rtd-tables.html
html_static_path = ['_static']
html_context = {
    'css_files': [
        '_static/theme_overrides.css',  # override wide tables in RTD theme
        ],
     }