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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = 'Modding Handbook - rFactor2'
copyright = '2021 - 2022, FuNK!'
author = 'FuNK!'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
    'sphinxprettysearchresults',
    'sphinx.ext.mathjax',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.autosectionlabel',
    'sphinx_search.extension',
]

# Make section labels unique to allow multiple use.
autosectionlabel_prefix_document = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The default language to highlight source code in.
highlight_language = 'c++'

# The style name to use for Pygments highlighting of source code.
pygments_style = 'default'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"

# A dictionary of options that influence the look and feel of
# the selected theme. These are theme-specific.
html_theme_options = {}

# A list of paths that contain custom themes, either as subdirectories
# or as zip files. Relative paths are taken as relative to
# the configuration directory.
html_theme_path = []

if html_theme == "sphinx_rtd_theme":
    html_theme_options = {
        #"analytics_id": "",
        # included in the title
        "logo_only": True,
        "display_version": False,
        "prev_next_buttons_location": 'bottom',
        "style_external_links": True,
        "collapse_navigation": True,
        "sticky_navigation": True,
        "navigation_depth": -1,
    }

    extensions.append('sphinx_rtd_theme')

# The �title� for HTML documentation generated with Sphinx�s own templates.
# This is appended to the <title> tag of individual pages, and
# used in the navigation bar as the �topmost� element.
html_title = "Modding Handbook - rFactor2"

# The base URL which points to the root of the HTML documentation.
# It is used to indicate the location of document using
# The Canonical Link Relation.

#html_baseurl = ""

# If given, this must be the name of an image file
# (path relative to the configuration directory) that is the logo of the docs,
# or URL that points an image file for the logo.
#
# Socket logo from: https://www.blender.org/about/logo

html_logo = "_static/mh-rf2_logo.svg"

# If given, this must be the name of an image file
# (path relative to the configuration directory) that is the favicon of
# the docs, or URL that points an image file for the favicon.

html_favicon = "_static/favicon.png"

# path relative to _static
if html_theme == "sphinx_rtd_theme":
    html_css_files = ["css/theme_overrides.css",]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If this is not None, a �Last updated on:� timestamp is inserted at
# every page bottom, using the given strftime() format.
# The empty string is equivalent to '%b %d, %Y'
# (or a locale-dependent equivalent).
html_last_updated_fmt = '%m/%d/%Y'

# Additional templates that should be rendered to HTML pages,
# must be a dictionary that maps document names to template names.

#html_additional_pages = {
#    '404': '404.html',
#}

# If true, the reST sources are included in the HTML build as _sources/name.
html_copy_source = True

# If true (and html_copy_source is true as well), links to the reST sources
# will be added to the sidebar.
html_show_sourcelink = False

# If nonempty, an OpenSearch description file will be output,
# and all pages will contain a <link> tag referring to it.
# Ed. Note: URL has to be adapted, when versioning is set up.
# html_use_opensearch = 'http://www.tirewall.net/mh-rf2'

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr', 'zh'
#
html_search_language = 'en'

# If true, "(C) Copyright " is shown in the HTML footer.
html_show_copyright = True

# If true, "Created using Sphinx" is shown in the HTML footer.
html_show_sphinx = False
