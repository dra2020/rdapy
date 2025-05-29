# rdapy

Redistricting Analytics in Python

This repository ([rdapy](https://github.com/dra2020/rdapy)) re-implements 
the main analytics used in [Dave's Redistricting](https://davesredistricting.org/) (DRA),
ignoring a few DRA-specific aspects (in particular, the five [0-100] ratings).
Unlike the analytics used in the app ([dra-analytics](https://github.com/dra2020/dra-analytics))
which are implememented in TypeScript, these are implemented in Python to make them easier to use outside of DRA.

There are both a PyPi package and a command-line interface.
They are described in detail at [the website for this repository](https://dra2020.github.io/rdapy/).

## Installing the Package

To install the package:

```bash
pip install rdapy
```

The latest version of the package is 2.3.3.

Then in your code, either `import rdapy` or `from rdapy import ...`.

## Setting up the Command-Line Interface

To setup the repository for local command-line use:

Clone the repository:

```bash
git clone https://github.com/dra2020/rdapy
cd rdapy
```

Then create a virtual environment that uses Python 3.12.
Then reset Python outside the virtual environment to the normal setting.
For example, using `pyenv`:

```bash
pyenv shell 3.12
python3 -m venv "./rdapy"
source "./rdapy/bin/activate"
deactivate
pyenv shell --unset
```

Then activate the virtual environment again, and install the required dependencies:

```bash
source "./rdapy/bin/activate"
pip install -r requirements.txt
pip install --upgrade pip
```

Finally, test that the automated tests run:

```bash
pytest
```

and that the command-line interface works:

```bash
scripts/score/SCORE.sh \
--state NC \
--plan-type congress \
--geojson testdata/data/NC_vtd_datasets.v4.geojson \
--graph testdata/examples/NC_graph.json \
--precomputed testdata/precomputed/NC_congress_precomputed.json \
--plans testdata/plans/NC_congress_plans.tagged.jsonl \
--scores temp/TEST_congress_scores.csv \
--by-district temp/TEST_congress_by-district.jsonl
```

## Development

There is a `launch.json` for VS Code debugging in the `docs` directory.

## Testing

Run automated tests with:

```bash
pytest
```

# Questions

Email questions to [feedback](mailto:feedback@davesredistricting.org?subject=Python-analytics).
