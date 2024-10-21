# BOSS Documentation

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Documentation build status](https://readthedocs.org/projects/bes3/badge/?version=latest)](https://bes3.readthedocs.io)
[![GPLv3+ license](https://img.shields.io/badge/License-GPLv3+-blue.svg)](https://www.gnu.org/licenses/gpl-3.0-standalone.html)
[![Open in Visual Studio Code](https://img.shields.io/badge/vscode-open-blue?logo=visualstudiocode)](https://open.vscode.dev/redeboer/bossdoc)
[![CI status](https://github.com/redeboer/bossdoc/workflows/CI/badge.svg)](https://github.com/redeboer/bossdoc/actions?query=branch%3Amaster+workflow%3ACI)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/redeboer/bossdoc/main.svg)](https://results.pre-commit.ci/latest/github/redeboer/bossdoc/main)
[![Spelling checked](https://img.shields.io/badge/cspell-checked-brightgreen.svg)](https://github.com/streetsidesoftware/cspell/tree/master/packages/cspell)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

This repository contains the source code for the
[bes3.rtfd.io](https://bes3.readthedocs.io) pages.

# How to contribute?

To contribute to the project, you need to install the package in a virtual environment. This can be done best with [`uv`](https://docs.astral.sh/uv) (see installation instructions [here](https://docs.astral.sh/uv/getting-started/installation)). For this, you first need to get the source code with [Git](https://git-scm.com):

```shell
git clone https://github.com/redeboer/bossdoc
cd bossdoc
```

Now it's simply a matter of creating and activating the [virtual environment](https://docs.astral.sh/uv/pip/environments) with [`uv sync`](https://docs.astral.sh/uv/reference/cli/#uv-sync). The dependencies for the project are 'pinned' in each commit through the [`uv.lock` file](https://docs.astral.sh/uv/concepts/projects/#project-lockfile).

```shell
uv sync
source .venv/bin/activate
```

Formatting and linting checks are automatically performed when committing changes. This is done with [pre-commit](https://pre-commit.com). To install the hooks in your local repository, run [`pre-commit install`](https://pre-commit.com/#3-install-the-git-hook-scripts) **once**:

```shell
pre-commit install --install-hooks
```
