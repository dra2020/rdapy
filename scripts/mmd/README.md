# Multi-Member District (MMD) Scoring

The scripts in this directory and the support code they use in the `rdapy` package are part of toolchain
for exploring the implications for multi-member districts (MMDs) with respect to minority representation.
This is a work in progress.

The code here leverages the production district aggregation code with only slight modifications allowing you
to experiment with different numbers of districts and different, homogeneous district magnitudes.

By default, official CVAP data is used to characterize the opportunities for different minority groups to elect
candidates of their choices in multi-member districts.
That official data can be transformed into alternative datasets that have the same format--the same nominal demographic
labels--but the values of which reflect assumptions based on modeling of group cohesion/fragmentation, crossover voting, 
and turnout.
In other words, the demographic labels in the transformed data--e.g., "Black", "Hispanic", etc.--represent repurposable 
groups of voters who will vote as a bloc and potentially elect candidates of their choice.

Note: "MMD" here refers to multi-member districts, not to be confused with majority-minority districts.

This experiment really highlights that, when it comes to analytics, there are two distinct systems:

* Two-party, single-member districts (SMDs) with first-past-the-post (FPTP) voting.
* More parties with multi-member districts (MMDs) and (some form of) proportional representation (PR) voting.

## TODO

[x] Add 'white' demographic to EI scoring.
[x] Move summarization to scoring. Delete separate script.
[x] Add statewide demographic percentages.
[x] Add Gallagher index to scores.

[x] Prune by-districts coming in.
[x] Add by-district E-I scores to aggs
[x] Summaries to scores.

[x] Backport compactness and splitting metrics into MMD scoring.

[ ] Leverage write.py to write scores.csv and by_districts.jsonl.

[ ] Add a district magnitude array to foreshadow heterogeneous magnitudes.


[ ] Rename args?
[ ] Draw diagram. 