# BOSS Documentation

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![Documentation build status](https://readthedocs.org/projects/bes3/badge)](https://bes3.readthedocs.io)
[![Open in Visual Studio Code](https://img.shields.io/badge/vscode-open-blue?logo=visualstudiocode)](https://open.vscode.dev/redeboer/bossdoc)
[![CI](https://github.com/redeboer/bossdoc/actions/workflows/ci.yml/badge.svg)](https://github.com/redeboer/bossdoc/actions/workflows/ci.yml)
[![pre-commit](https://results.pre-commit.ci/badge/github/redeboer/bossdoc/main.svg)](https://results.pre-commit.ci/latest/github/redeboer/bossdoc/main)
[![Spelling checked](https://img.shields.io/badge/cspell-checked-brightgreen.svg)](https://github.com/streetsidesoftware/cspell/tree/master/packages/cspell)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

This repository contains the source code for the [bes3.rtfd.io](https://bes3.readthedocs.io) pages.

## How to contribute?

To contribute to the project, you need to install the package in a virtual environment. This can be done best with [`uv`](https://docs.astral.sh/uv) (see installation instructions [here](https://docs.astral.sh/uv/getting-started/installation)). For this, you first need to get the source code with [Git](https://git-scm.com):

```bash
git clone https://github.com/redeboer/bossdoc
cd bossdoc
```

Now it's simply a matter of creating and activating the [virtual environment](https://docs.astral.sh/uv/pip/environments) with [`uv sync`](https://docs.astral.sh/uv/reference/cli/#uv-sync). The dependencies for the project are 'pinned' in each commit through the [`uv.lock` file](https://docs.astral.sh/uv/concepts/projects/#project-lockfile).

```bash
uv sync
source .venv/bin/activate
```

Formatting and linting checks are automatically performed when committing changes. This is done with [pre-commit](https://pre-commit.com). To install the hooks in your local repository, run [`pre-commit install`](https://pre-commit.com/#3-install-the-git-hook-scripts) **once**:

```bash
pre-commit install --install-hooks
```
