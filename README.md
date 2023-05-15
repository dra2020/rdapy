# rdapy

Redistricting analytics in Python

These are the main analytics used in [Dave's Redistricting](https://davesredistricting.org/maps#),
ignoring a few DRA-specific aspects (in particular, the five [0-100] ratings).
Unlike the analytics in [dra-analytics](https://github.com/dra2020/dra-analytics)
which are implememented in TypeScript, these are implemented in Python. 

## Categories

The analytics are organized by area:

- [Compactness](./docs/compactness.md): Various measures of compactness
- [Equal](./docs/equal.md): Population deviation
- [Graph](./docs/graph.md): Checks for contiguity & embeddedness
- [Partisan](./docs/partisan.md): Various measures of partisan bias & responsiveness, as well as support for rank-vote graphs and seats-votes curves
- [Splitting](./docs/splitting.md): County- & district-splitting and COI splitting

## Installation

TODO

```bash
pip install rdapy
```
