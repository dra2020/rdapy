# Graph

There are two functions for evaluating the graph of features (like precincts) assigned to districts.
The graphs may contain a virtual "OUT_OF_STATE" node and virtual "OUT_OF_STATE" neighbors, so you can
detect when a feature is on the border of the state. 

## Contiguity

To check whether a graph is fully connected:

```python
def is_connected(geos: list[Any], graph: dict[str, list[str]]) -> bool:
```

where "geos" is a list of ids for geographies (features) and 
"graph" is a nodes/neighbors dictionary of their connectedness.

## Embeddedness

To check whether a district is fully embedded within another district:

```python
def is_embedded(
    district_id: int | str,
    plan: dict[str, int | str],
    inverted_plan: dict[int | str, set[str]],
    graph: dict[str, list[str]],
) -> bool:
```

where "plan" is a dictionary mapping of geographies (features) to districts, and
"inverted_plan" is a dictionary mapping of districts to sets of features in them.

A district is *not* a "donut hole" district:

* If any neighbor is "OUT_OF_STATE"; or
* If there are two or more neighboring districts.
