---
layout: page
title: Adjacency Graph
permalink: graph/
---

You can check a plan to make sure districts are contiguous and not embedded within other districts.

### Contiguity

To check whether a list of features (e.g., assigned to a district) is fully connected:

```python
def is_connected(ids: list[Any], graph: dict[str, list[str]]) -> bool:
```

where "ids" is a list of ids for the geographies (features) and 
"graph" is a nodes/neighbors dictionary of their connectedness (adjacency).

Examples can be found in the JSON files in the testdata/graph directory.

Note: The graph may contain a virtual "OUT_OF_STATE" node and virtual "OUT_OF_STATE" neighbors, 
so you can detect when a feature is on the border of the state (see below). 

If you pass all the feature ids for a state, 
you can check whether the graph for the state is fully connected.

### Embeddedness

To check whether one district is fully embedded within another district:

```python
def is_embedded(
    district_id: int | str,
    plan: dict[str, int | str],
    inverted_plan: dict[int | str, set[str]],
    graph: dict[str, list[str]],
) -> bool:
```

where "plan" is a dictionary mapping of features ids to districts, and
"inverted_plan" is a dictionary mapping of district ids to sets of features in them.

A district is *not* a "donut hole" district:

* If any neighbor is "OUT_OF_STATE"; or
* If there are two or more neighboring districts.
