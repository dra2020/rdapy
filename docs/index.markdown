---
layout: default
---

<h2>Redistricting Analytics in Python</h2>

This repository ([rdapy](https://github.com/dra2020/rdapy)) re-implements 
the main analytics used in [Dave's Redistricting](https://davesredistricting.org/) (DRA),
ignoring a few DRA-specific aspects (in particular, the five [0-100] ratings).
Unlike the analytics used in the app ([dra-analytics](https://github.com/dra2020/dra-analytics))
which are implememented in TypeScript, these are implemented in Python to make them easier to use outside of DRA.

There are both a PyPi package and a command-line interface.

### Package

The analytics in the PyPi package are organized by area (in alphabetical order):

- [Compactness](./compactness/): Various measures of compactness
- [Equal](./equal/): Population deviation
- [Graph](./graph/): Checks for contiguity & embeddedness
- [Minority](./minority/): Minority opportunity metrics
- [Partisan](./partisan/): Various measures of partisan bias & responsiveness, as well as support for rank-vote graphs and seats-votes curves
- [Splitting](./splitting/): County- & district-splitting and COI splitting

The `samples` directory contains some simple examples of how to exercies these functions
and how to preprocess raw block-level data into the formats required by the analytics.

### Command-Line Interface

The command-line interface uses the package and enables [high-volume offline scoring](./scoring/).
This toolchain uses DRA GeoJSON and graph files in the [dra2020/vtd_data](https://github.com/dra2020/vtd_data) GitHub repository.
as input data and scores each plan in an ensemble or collection
on several dozen metrics described in [Scores (Metrics)]({{ '/scores' | prepend: site.baseurl }})
generating a CSV file with one row of scores per plan.

There are some housekeeping scripts to support this scoring:

- [Extracting Contiguity Graphs]({{ '/extracting-graphs' | prepend: site.baseurl }}): Extracts fully connected adjacency graphs from DRA GeoJSON files.
- [Extracting Data]({{ '/extracting-data' | prepend: site.baseurl }}): Extracts precinct data from DRA GeoJSON files for scoring.
- [One-time Preprocessing]({{ '/once' | prepend: site.baseurl }}): Pre-computes geographic baselines for the geographic advantage metric.

### Installation

For installation instructions, see the [README](https://github.com/dra2020/rdapy).

### Questions

Email questions to [feedback](mailto:feedback@davesredistricting.org?subject=Python-analytics).