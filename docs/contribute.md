# Contribute

This website has been set up not only to provide a set of **accessible** tutorial pages
on the use of BOSS, but also a continuously updated **inventory of the available
packages**. For now, it serves as a central, informal location to collect information
about BESIII, but the aim is to migrate its content to a formal, interactive BESIII
platform as soon as that has been set up.

```{image} _static/edit-button.png
:alt: fishy
:class: bg-primary
:width: 250px
:align: right
```

**It is quite easy to contribute!** First of all, if you spot some typos, just click the
edit button in the top right of each page. That will lead you to the source code for the
page in [this repository on GitHub](https://github.com/redeboer/bossdoc). Bigger
problems can be reported by opening an issue. In both cases, you will need to
[create a GitHub account](https://github.com/join).

Alternatively, just directly highlight or make notes on these pages. With a
[Hypothesis.is](https://hypothes.is) you can then post those notes as feedback.

## Developing these pages

:::{tip}

When developing, you have to implement changes through Git.
[Pro Git](https://git-scm.com/book/en/v2) is the best resource to learn how to do this.
Also have a look [here](https://guides.github.com/introduction/flow) for a short
tutorial about the Git workflow.

:::

These pages are built with [Sphinx](https://www.sphinx-doc.org/en/master), for which you
need to have [Python](https://www.python.org) installed. The pages are written in
[Markedly Structured Text (MyST)](https://myst-parser.readthedocs.io), an extended form
of [Markdown](https://en.wikipedia.org/wiki/Markdown).

The easiest way to develop these pages is by using
[Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) and
[Visual Studio Code](https://code.visualstudio.com). Conda manages
[virtual environments](https://realpython.com/python-virtual-environments-a-primer), so
that the Python packages that are required to work on the documentation can be easily
removed or updated. Once you have those installed, it's simply a matter of running:

```bash
git clone https://github.com/redeboer/bossdoc.git
cd bossdoc
conda env create  # install required packages
conda activate bossdoc
pre-commit install
code .
```

The rest of the instructions will be shown once Visual Studio Code opens with the last
command ;)

Next, open a terminal (**Ctrl + `**) and run

<!-- cspell:ignore doclive -->

```bash
tox -e doclive
```

This will build the documentation and automatically update it while you edit the files
in VSCode!

:::{seealso}

{doc}`compwa:develop` on the {doc}`ComPWA website <compwa:index>`, which uses the same
set-up.

:::
