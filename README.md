# rdapy

Redistricting Analytics in Python

This repository ([rdapy](https://github.com/dra2020/rdapy)) re-implements 
the main analytics used in [Dave's Redistricting](https://davesredistricting.org/) (DRA).
Unlike the analytics used in the app ([dra-analytics](https://github.com/dra2020/dra-analytics))
which are implememented in TypeScript, 
these are implemented as a Python package to make them easier to use outside of DRA.
There is also a command-line interface for high-volume scoring.

These are described in detail at [the website for this repository](https://dra2020.github.io/rdapy/).

To use it in your Python, install the package.
To use the high-volume scoring scripts, set up the command-line interface.

## Installing the Package

To install the package:

```bash
pip install rdapy
```

The latest version of the package is 2.3.4.

Then in your code, either `import rdapy` or `from rdapy import ...`.

## Installing Command-Line Interface

Before installing the command-line interface (CLI),
make sure you have the prerequisites installed.

### Install Prequisites

The high-volume scoring scripts require Python 3.12 or later.
If that is not the default on your computer, 
you can use `pyenv` to manage multiple Python versions.
These instructions assume you're using `pyenv`.

Install `pyenv` from [Homebrew](https://formulae.brew.sh/formula/pyenv):

```bash
brew install pyenv
```

Completing that setup will involve adding a few lines to your shell profile file (like `.bash_profile`).

You can install Python 3.12 from [Homebrew](https://formulae.brew.sh/formula/python@3.12):

```bash
brew install python@3.12
```

### Setting Up Your Environment

With the prequisites installed, clone the GitHub repository:

```bash
git clone https://github.com/dra2020/rdapy
cd rdapy
```

Then create a virtual environment that uses Python 3.12, and 
then reset Python outside the virtual environment to the normal setting:

```bash
pyenv shell 3.12
python3 -m venv /path/to/venvs/rdapy
source /path/to/venvs/rdapy/bin/activate
deactivate
pyenv shell --unset
```

Then activate the virtual environment again, and install the required dependencies:

```bash
source /path/to/venvs/rdapy/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

Finally, test that the automated tests run:

```bash
pytest
```

Then test that the command-line interface works:

```bash
scripts/score/SCORE.sh \
--state NC \
--plan-type congress \
--geojson testdata/data/NC_vtd_datasets.v4.geojson \
--graph testdata/examples/NC_graph.json \
--precomputed testdata/examples/NC_congress_precomputed.json \
--plans testdata/plans/NC_congress_plans.tagged.jsonl \
--scores /path/to/TEST_scores.csv \
--by-district /path/to/TEST_by-district.jsonl
```

Replace `/path/to` with where you want the output files to go.

## Development

There is a `launch.json` for VS Code debugging in the `docs` directory.

## Testing

Run automated tests with:

```bash
pytest
```

# Questions

Email questions to [feedback](mailto:feedback@davesredistricting.org?subject=Python-analytics).
