# rdapy
Redistricting analytics in Python

The analytics here are the main ones used in [Dave's Redistricting](https://davesredistricting.org/maps#).
Unlike the analytics in [dra-analytics](https://github.com/dra2020/dra-analytics) which are implememented
in TypeScript, these are implemented in Python and do not depend on the DRA codebase or implement any
DRA-specific functionality.

These are all the categories:

- [Compactness](./docs/compactness.md): Various measures of compactness
- [Equal](./docs/equal.md): Population deviation
- [Graph](./docs/graph.md): Checks for contiguity & embeddedness
- [Partisan](./docs/partisan.md): Various measures of partisan bias & responsiveness, as well as support for rank-vote graphs and seats-votes curves
- [Splitting](./docs/splitting.md): County- & district-splitting and COI splitting
