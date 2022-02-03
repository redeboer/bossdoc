# type: ignore

"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

import os
from typing import Dict

import requests
from sphinx.application import Sphinx

# -- Project information -----------------------------------------------------
project = "BESIII Offline Software System"
package = "bossdoc"
REPO_NAME = "bossdoc"
copyright = "2020, BESIII"

if os.path.exists(f"../src/{package}/version.py"):
    __release = get_distribution(package).version
    version = ".".join(__release.split(".")[:3])


# -- Fetch logo --------------------------------------------------------------
def fetch_logo(url: str, output_path: str) -> None:
    if os.path.exists(output_path):
        return
    online_content = requests.get(url, allow_redirects=True)
    with open(output_path, "wb") as stream:
        stream.write(online_content.content)


LOGO_PATH = "_static/logo.jpg"
try:
    fetch_logo(
        url="https://paluma.ruhr-uni-bochum.de/images/besIII/BES3_logo.jpg",
        output_path=LOGO_PATH,
    )
except requests.exceptions.ConnectionError:
    pass
if os.path.exists(LOGO_PATH):
    html_logo = LOGO_PATH


# -- General configuration ---------------------------------------------------
master_doc = "index.md"
source_suffix = {
    ".ipynb": "myst-nb",
    ".md": "myst-nb",
    ".rst": "restructuredtext",
}

# The master toctree document.
master_doc = "index"
modindex_common_prefix = [
    f"{package}.",
]

extensions = [
    "myst_nb",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx_comments",
    "sphinx_copybutton",
    "sphinx_math_dollar",
    "sphinx_panels",
    "sphinx_thebe",
    "sphinx_togglebutton",
    "sphinxcontrib.bibtex",
]
exclude_patterns = [
    "**.ipynb_checkpoints",
    "*build",
    "adr/template.md",
    "tests",
]

# Todo-list
todo_include_todos = True

# General sphinx settings
add_module_names = False
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
    "special-members": ", ".join(
        [
            "__call__",
            "__eq__",
        ]
    ),
}
graphviz_output_format = "svg"
html_copy_source = True  # needed for download notebook button
html_favicon = "_static/favicon.ico"
html_show_copyright = False
html_show_sourcelink = False
html_show_sphinx = False
html_sourcelink_suffix = ""
html_theme = "sphinx_book_theme"
html_theme_options = {
    "repository_url": f"https://github.com/redeboer/{REPO_NAME}",
    "repository_branch": "main",
    "path_to_docs": "docs",
    "use_download_button": True,
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org",
        "colab_url": "https://colab.research.google.com",
        "notebook_interface": "jupyterlab",
        "thebe": True,
        "thebelab": True,
    },
    "show_navbar_depth": 2,
    "show_toc_level": 2,
    "theme_dev_mode": True,
}
html_title = "BOSS Documentation"
panels_add_bootstrap_css = False  # remove panels css to get wider main content
pygments_style = "sphinx"
todo_include_todos = False
viewcode_follow_imported_members = True

# Cross-referencing configuration
default_role = "py:obj"
primary_domain = "py"
nitpicky = True  # warn if cross-references are missing

# Intersphinx settings
intersphinx_mapping = {
    "compwa-org": ("https://compwa-org.readthedocs.io/en/stable", None),
}

# Settings for autosectionlabel
autosectionlabel_prefix_document = True

# Settings for bibtex
bibtex_bibfiles = ["bibliography.bib"]
suppress_warnings = [
    "myst.domains",
]

# Settings for copybutton
copybutton_prompt_is_regexp = True
copybutton_prompt_text = r">>> |\.\.\. "  # doctest

# Settings for linkcheck
linkcheck_anchors = False
linkcheck_ignore = [
    "http://code.ihep.ac.cn/redeboer/IniSelect",
    "https://github.com/redeboer/BOSS_IniSelect_ORIGINAL",
    r"http://[A-Za-z0-9]+\.ihep\.ac\.cn",
    r"http://[A-Za-z0-9]+\.ihep\.cas\.cn",
    r"http://[A-Za-z0-9]+\.ucas\.ac\.cn",
    r"https://[A-Za-z0-9]+\.ihep\.ac\.cn",
]

# Settings for myst_nb
execution_timeout = -1
jupyter_execute_notebooks = "force"
nb_output_stderr = "remove"
nb_render_priority = {
    "html": (
        "application/vnd.jupyter.widget-view+json",
        "application/javascript",
        "text/html",
        "image/svg+xml",
        "image/png",
        "image/jpeg",
        "text/markdown",
        "text/latex",
        "text/plain",
    )
}
nb_render_priority["doctest"] = nb_render_priority["html"]

# Settings for myst-parser
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "smartquotes",
]
myst_update_mathjax = False

# Settings for sphinx_comments
comments_config = {
    "hypothesis": True,
    "utterances": {
        "repo": f"ComPWA/{REPO_NAME}",
        "issue-term": "pathname",
        "label": "📝 Docs",
    },
}

# Settings for Thebe cell output
thebe_config = {
    "repository_url": html_theme_options["repository_url"],
    "repository_branch": html_theme_options["repository_branch"],
}

# Add roles to simplify external linnks
def setup(app: Sphinx):
    app.add_role(
        "wiki", autolink("https://en.wikipedia.org/wiki/%s", {"_": " "})
    )


def autolink(pattern: str, replace_mapping: Dict[str, str]):
    def role(
        name, rawtext, text: str, lineno, inliner, options={}, content=[]
    ):
        output_text = text
        for search, replace in replace_mapping.items():
            output_text = output_text.replace(search, replace)
        url = pattern % (text,)
        node = nodes.reference(rawtext, output_text, refuri=url, **options)
        return [node], []

    return role


# Specify bibliography style
from pybtex.plugin import register_plugin
from pybtex.richtext import Tag, Text
from pybtex.style.formatting.unsrt import Style as UnsrtStyle
from pybtex.style.template import (
    FieldIsMissing,
    _format_list,
    field,
    href,
    join,
    node,
    sentence,
    words,
)


@node
def et_al(children, data, sep="", sep2=None, last_sep=None):
    if sep2 is None:
        sep2 = sep
    if last_sep is None:
        last_sep = sep
    parts = [part for part in _format_list(children, data) if part]
    if len(parts) <= 1:
        return Text(*parts)
    elif len(parts) == 2:
        return Text(sep2).join(parts)
    elif len(parts) == 3:
        return Text(last_sep).join([Text(sep).join(parts[:-1]), parts[-1]])
    else:
        return Text(parts[0], Tag("em", " et al"))


@node
def names(children, context, role, **kwargs):
    """Return formatted names."""
    assert not children
    try:
        persons = context["entry"].persons[role]
    except KeyError:
        raise FieldIsMissing(role, context["entry"])

    style = context["style"]
    formatted_names = [
        style.format_name(person, style.abbreviate_names) for person in persons
    ]
    return et_al(**kwargs)[formatted_names].format_data(context)


class MyStyle(UnsrtStyle):
    def __init__(self):
        super().__init__(abbreviate_names=True)

    def format_names(self, role, as_sentence=True):
        formatted_names = names(
            role, sep=", ", sep2=" and ", last_sep=", and "
        )
        if as_sentence:
            return sentence[formatted_names]
        else:
            return formatted_names

    def format_url(self, e):
        return words[
            href[
                field("url", raw=True),
                field("url", raw=True, apply_func=remove_http),
            ]
        ]

    def format_isbn(self, e):
        return href[
            join[
                "https://isbnsearch.org/isbn/",
                field("isbn", raw=True, apply_func=remove_dashes_and_spaces),
            ],
            join[
                "ISBN:",
                field("isbn", raw=True),
            ],
        ]


def remove_dashes_and_spaces(isbn: str) -> str:
    to_remove = ["-", " "]
    for remove in to_remove:
        isbn = isbn.replace(remove, "")
    return isbn


def remove_http(input: str) -> str:
    to_remove = ["https://", "http://"]
    for remove in to_remove:
        input = input.replace(remove, "")
    return input


register_plugin("pybtex.style.formatting", "unsrt_et_al", MyStyle)
