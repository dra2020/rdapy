# rdapy

Redistricting analytics in Python

This repository ([rdapy](https://github.com/dra2020/rdapy)) re-implements 
the main analytics used in [Dave's Redistricting](https://davesredistricting.org/maps#),
ignoring a few DRA-specific aspects (in particular, the five [0-100] ratings).
Unlike the analytics used in the app ([dra-analytics](https://github.com/dra2020/dra-analytics))
which are implememented in TypeScript, these are implemented in Python. 

## Categories

The analytics are organized by area:

- [Compactness](./docs/compactness.md): Various measures of compactness
- [Equal](./docs/equal.md): Population deviation
- [Graph](./docs/graph.md): Checks for contiguity & embeddedness
- [Minority](./docs/minority.md): Minority opportunity metrics
- [Partisan](./docs/partisan.md): Various measures of partisan bias & responsiveness, as well as support for rank-vote graphs and seats-votes curves
- [Splitting](./docs/splitting.md): County- & district-splitting and COI splitting

The `samples` directory contains some simple examples of how to exercies these functions
and how to preprocess raw block-level data into the formats required by the analytics.

## Installation

To install the package:

```bash
pip install rdapy
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

Then create a virtual environment that uses Python 3.12, e.g., using `pyenv`.
Then reset Python to the normal setting.
For example:

```bash
pyenv shell 3.12
python3 -m venv "./venv"
source "./venv/bin/activate"
deactivate
pyenv shell --unset
```

Then activate the virtual environment again, and install the required dependencies:

```bash
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

## Usage

```
import rdapy
```

# Automated Tests

```bash
pytest
```

# Questions

Email questions to [feedback](mailto:feedback@davesredistricting.org?subject=Python-analytics).
