from __future__ import annotations

from sphinx_api_relink.linkcode import (
    _get_commit_sha,  # pyright:ignore[reportPrivateUsage]
)

BRANCH = _get_commit_sha()
REPO_NAME = "bossdoc"

author = ""
autosectionlabel_prefix_document = True
bibtex_bibfiles = ["bibliography.bib"]
bibtex_default_style = "unsrt_et_al"
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
    "sphinx_api_relink",
    "sphinx_comments",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_pybtex_etal_style",
    "sphinx_togglebutton",
    "sphinxcontrib.bibtex",
]
exclude_patterns = [
    "**.ipynb_checkpoints",
    "*build",
    "adr/template.md",
    "tests",
]
html_favicon = "_static/favicon.ico"
html_logo = "https://github.com/redeboer/bossdoc/assets/29308176/71ae5632-3aa9-4756-b4bb-8af397c62951"
html_show_copyright = False
html_sourcelink_suffix = ""
html_theme = "sphinx_book_theme"
html_theme_options = {
    "path_to_docs": "docs",
    "repository_url": f"https://github.com/redeboer/{REPO_NAME}",
    "repository_branch": BRANCH,
    "show_navbar_depth": 2,
    "show_toc_level": 2,
    "use_download_button": False,
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
    "use_source_button": True,
}
html_title = "BOSS Documentation"
intersphinx_mapping = {
    "compwa": ("https://compwa.github.io", None),
}
linkcheck_anchors = False
linkcheck_ignore = [
    "http://code.ihep.ac.cn/redeboer/IniSelect",
    "http://polywww.in2p3.fr",
    "http://www.cmtsite.net",
    "https://dayabay.bnl.gov",
    "https://github.com/redeboer/BOSS_IniSelect_ORIGINAL",
    "https://scientificlinux.org",
    "https://www.putty.org",
    "https://www.sciencedirect.com/science/article/pii/S0168900209023870",
    "https://www.tldp.org",
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
nitpicky = True  # warn if cross-references are missing
panels_add_bootstrap_css = False  # remove panels css to get wider main content
primary_domain = "py"
project = "BESIII Offline Software System"
pygments_style = "sphinx"
todo_include_todos = True
suppress_warnings = [
    "myst.domains",
]
