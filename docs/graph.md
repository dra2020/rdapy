# Graph

TODO

OUT_OF_STATE

## Contiguity

```python
def is_connected(geos: list[Any], adjacency: dict[Any, list[Any]]) -> bool:
    """Is a graph is fully connected?
    i.e., w/o regard to the virtual state boundary "shapes".

    Kenshi's iterative implementation of the recursive algorithm

    geos - the list of geographies
    adjacency - the connectedness of the geos
    """
```

## Embeddedness

```python
def is_embedded(
    district_id: int | str,
    plan: dict[str, int | str],
    inverted_plan: dict[int | str, set[str]],
    graph: dict[str, list[str]],
) -> bool:
    """Is a district fully embedded w/in another district?

    A district is NOT a "donut hole" district:
    * If any neighbor is 'OUT_OF_STATE'; or
    * If there are 2 or more neighboring districts.
    """
```
