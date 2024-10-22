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

```bash
pip install rdapy
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
