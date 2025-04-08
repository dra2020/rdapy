---
layout: default
---

<h2>Redistricting analytics in Python</h2>

This repository ([rdapy](https://github.com/dra2020/rdapy)) re-implements 
the main analytics used in [Dave's Redistricting](https://davesredistricting.org/) (DRA),
ignoring a few DRA-specific aspects (in particular, the five [0-100] ratings).
Unlike the analytics used in the app ([dra-analytics](https://github.com/dra2020/dra-analytics))
which are implememented in TypeScript, these are implemented in Python to make them easier to use outside of DRA.

There are both a PyPi package and a command-line interface.

Note: The repository is in the process of being upgraded to include a GitHub Pages site
which will, among other things, explain high-volume offline scoring.

## Package

The analytics in the PyPi package are organized by area (in alphabetical order):

- [Compactness](./compactness.html): Various measures of compactness
- [Equal](./equal.html): Population deviation
- [Graph](./graph.html): Checks for contiguity & embeddedness
- [Minority](./minority.html): Minority opportunity metrics
- [Partisan](./partisan.html): Various measures of partisan bias & responsiveness, as well as support for rank-vote graphs and seats-votes curves
- [Splitting](./splitting.html): County- & district-splitting and COI splitting

The `samples` directory contains some simple examples of how to exercies these functions
and how to preprocess raw block-level data into the formats required by the analytics.

## Command-Line Interface

The command-line interface enables [high-volume offline scoring](./scoring.html).

## Installation

To install the package:

```bash
pip install rdapy
```

Then

```
import rdapy
```

To setup the repository for local command-line use:

Clone the repository:

```bash
git clone https://github.com/dra2020/rdapy
cd rdapy
```

Until these high-volume scoring changes are merged into `main`, checkout the `bulkscoring` branch:

```bash
git checkout bulkscoring
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
scripts/SCORE.sh \
--state NC \
--plan-type congress \
--geojson testdata/data/NC_vtd_datasets.geojson \
--data-map testdata/data/NC_data_map.json \
--graph testdata/intermediate/NC_graph.json \
--plans testdata/ensemble/NC_congress_plans.100.jsonl \
--scores temp/TEST_congress_scores.csv \
--by-district temp/TEST_congress_by-district.jsonl
```

## Development

There is a `launch.json` for VS Code debugging in the `docs` directory.

Run automated tests with:

```bash
pytest
```

# Questions

Email questions to [feedback](mailto:feedback@davesredistricting.org?subject=Python-analytics).