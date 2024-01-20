from __future__ import annotations

import os
from typing import TYPE_CHECKING

from docutils import nodes
from pybtex.plugin import register_plugin
from pybtex.richtext import Tag, Text
from pybtex.style.formatting.unsrt import Style as UnsrtStyle
from pybtex.style.template import (
    FieldIsMissing,
    _format_list,  # pyright: ignore[reportPrivateUsage]
    field,
    href,
    join,
    node,
    sentence,
    words,
)

if TYPE_CHECKING:
    from sphinx.application import Sphinx


def get_execution_mode() -> str:
    if "EXECUTE_NB" in os.environ:
        print("\033[93;1mWill run Jupyter notebooks!\033[0m")
        return "cache"
    return "off"


PACKAGE_NAME = "bossdoc"
REPO_NAME = "bossdoc"


autosectionlabel_prefix_document = True
bibtex_bibfiles = ["bibliography.bib"]
comments_config = {
    "hypothesis": True,
    "utterances": {
        "repo": f"redeboer/{REPO_NAME}",
        "issue-term": "pathname",
        "label": "📝 Docs",
    },
}
copybutton_prompt_is_regexp = True
copybutton_prompt_text = r">>> |\.\.\. "
copyright = "2020, BESIII"
default_role = "py:obj"
extensions = [
    "myst_nb",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx_comments",
    "sphinx_copybutton",
    "sphinx_design",
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
html_copy_source = True  # needed for download notebook button
html_favicon = "_static/favicon.ico"
html_logo = "https://github.com/redeboer/bossdoc/assets/29308176/71ae5632-3aa9-4756-b4bb-8af397c62951"
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
}
html_title = "BOSS Documentation"
intersphinx_mapping = {
    "compwa": ("https://compwa.github.io", None),
}
linkcheck_anchors = False
linkcheck_ignore = [
    "http://code.ihep.ac.cn/redeboer/IniSelect",
    "http://www.cmtsite.net",
    "https://github.com/redeboer/BOSS_IniSelect_ORIGINAL",
    "https://scientificlinux.org",
    r"http://[A-Za-z0-9]+\.ihep\.ac\.cn",
    r"http://[A-Za-z0-9]+\.ihep\.cas\.cn",
    r"http://[A-Za-z0-9]+\.ucas\.ac\.cn",
    r"https://[A-Za-z0-9]+\.ihep\.ac\.cn",
]
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "smartquotes",
]
myst_update_mathjax = False
nb_execution_mode = get_execution_mode()
nb_execution_timeout = -1
nb_output_stderr = "remove"
nitpicky = True  # warn if cross-references are missing
panels_add_bootstrap_css = False  # remove panels css to get wider main content
primary_domain = "py"
project = "BESIII Offline Software System"
pygments_style = "sphinx"
source_suffix = {
    ".ipynb": "myst-nb",
    ".md": "myst-nb",
    ".rst": "restructuredtext",
}
thebe_config = {
    "repository_url": html_theme_options["repository_url"],
    "repository_branch": html_theme_options["repository_branch"],
}
todo_include_todos = True
viewcode_follow_imported_members = True
suppress_warnings = [
    "myst.domains",
]


# Add roles to simplify external linnks
def setup(app: Sphinx):
    app.add_role("wiki", autolink("https://en.wikipedia.org/wiki/%s", {"_": " "}))


def autolink(pattern: str, replace_mapping: dict[str, str]):
    def role(name, rawtext, text: str, lineno, inliner, options={}, content=[]):
        output_text = text
        for search, replace in replace_mapping.items():
            output_text = output_text.replace(search, replace)
        url = pattern % (text,)
        node = nodes.reference(rawtext, output_text, refuri=url, **options)
        return [node], []

    return role


# Specify bibliography style
@node
def et_al(children, data, sep="", sep2=None, last_sep=None):
    if sep2 is None:
        sep2 = sep
    if last_sep is None:
        last_sep = sep
    parts = [part for part in _format_list(children, data) if part]
    if len(parts) <= 1:
        return Text(*parts)
    if len(parts) == 2:  # noqa: PLR2004
        return Text(sep2).join(parts)
    if len(parts) == 3:  # noqa: PLR2004
        return Text(last_sep).join([Text(sep).join(parts[:-1]), parts[-1]])
    return Text(parts[0], Tag("em", " et al"))


@node
def names(children, context, role, **kwargs):
    """Return formatted names."""
    assert not children
    try:
        persons = context["entry"].persons[role]
    except KeyError:
        raise FieldIsMissing(role, context["entry"]) from None
    style = context["style"]
    formatted_names = [
        style.format_name(person, style.abbreviate_names) for person in persons
    ]
    return et_al(**kwargs)[formatted_names].format_data(context)


class MyStyle(UnsrtStyle):
    def __init__(self):
        super().__init__(abbreviate_names=True)

    def format_names(self, role, as_sentence=True):
        formatted_names = names(role, sep=", ", sep2=" and ", last_sep=", and ")
        if as_sentence:
            return sentence[formatted_names]
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
