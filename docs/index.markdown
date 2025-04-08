---
layout: default
---

<h2>Redistricting Analytics in Python (rdapy)</h2>

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

- [Compactness](./compactness/): Various measures of compactness
- [Equal](./equal/): Population deviation
- [Graph](./graph/): Checks for contiguity & embeddedness
- [Minority](./minority/): Minority opportunity metrics
- [Partisan](./partisan/): Various measures of partisan bias & responsiveness, as well as support for rank-vote graphs and seats-votes curves
- [Splitting](./splitting/): County- & district-splitting and COI splitting

The `samples` directory contains some simple examples of how to exercies these functions
and how to preprocess raw block-level data into the formats required by the analytics.

## Command-Line Interface

The command-line interface uses the package and enables [high-volume offline scoring](./scoring/).

## Installation

For installation instructions, see the [README](https://github.com/dra2020/rdapy).

## Questions

Email questions to [feedback](mailto:feedback@davesredistricting.org?subject=Python-analytics).