"""
EXPERIMENTING WITH GEOGRAPHIC BASESLINES (NEIGHBORHOODS)

NOTE - What are ways to speed this up?
"""

from typing import Any, List, Dict, Tuple, Set, NamedTuple, Deque

import math
from collections import deque, defaultdict

import rdapy as rda

from .utils import OUT_OF_STATE
from ..utils import approx_equal


def distance(a: Tuple[float, float], b: Tuple[float, float]) -> float:
    """Calculate a proxy for the distance between two points expressed as (lon, lat) tuples."""

    lat_squared: float = (a[1] - b[1]) * (a[1] - b[1])
    lon_squared: float = (a[0] - b[0]) * (a[0] - b[0])

    return lat_squared + lon_squared


# def distance(a: Tuple[float, float], b: Tuple[float, float]) -> float:
#     """Calculate the distance between two points expressed as (lon, lat) tuples."""

#     return math.sqrt((a[1] - b[1]) * (a[1] - b[1]) + (a[0] - b[0]) * (a[0] - b[0]))


def make_pair(precinct1: str, precinct2: str) -> Tuple[str, str]:
    """Return a pair of precincts in canonical sorted order."""

    return (precinct1, precinct2) if precinct1 < precinct2 else (precinct2, precinct1)


class DistanceLedger:
    """Compute and cache distances between pairs of precincts as needed."""

    def __init__(self):
        self.distances: Dict[Tuple[str, str], float] = dict()

    def distance_between(
        self,
        geoid1: str,
        center1: Tuple[float, float],
        geoid2: str,
        center2: Tuple[float, float],
    ) -> float:
        pair: Tuple[str, str] = make_pair(geoid1, geoid2)
        if pair in self.distances:
            return self.distances[pair]
        else:
            d: float = distance(center1, center2)
            self.distances[pair] = d
            return d


class Neighbor(NamedTuple):
    geoid: str
    distance: float
    pop: int
    dem_votes: int
    tot_votes: int


def make_region(
    geoid: str,
    data: Dict[str, Dict[str, Any]],
    graph: Dict[str, List[str]],
    *,
    ledger: DistanceLedger,
    target: int,
    buffer: float = 1.1,
    debug: bool = False,
) -> Deque[Neighbor]:
    """Return the 'region' around a precinct. Fully explore each 'layer' away from the precinct."""

    total_pop: int = data[geoid]["pop"]
    neighbors: List[Neighbor] = [
        Neighbor(
            geoid,
            0.0,
            data[geoid]["pop"],
            data[geoid]["dem_votes"],
            data[geoid]["tot_votes"],
        )
    ]

    layers: Dict[int, Set] = defaultdict(set)
    current_layer: int = 0
    split_index: int = -1

    visited: set[str] = {geoid}
    queue: Deque = deque([(geoid, current_layer)])

    while queue:
        node, layer = queue[0]  # Peek at next node

        if layer > current_layer:
            if split_index == -1:
                split_index = len(neighbors)
            if total_pop >= target * buffer:
                break
            current_layer = layer

        node, layer = queue.popleft()
        layers[layer].add(node)

        for neighbor in graph[node]:
            if neighbor == OUT_OF_STATE:
                continue
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, layer + 1))

                total_pop += data[neighbor]["pop"]
                distance: float = ledger.distance_between(
                    node, data[node]["center"], neighbor, data[neighbor]["center"]
                )
                neighbors.append(
                    Neighbor(
                        neighbor,
                        distance,
                        data[neighbor]["pop"],
                        data[neighbor]["dem_votes"],
                        data[neighbor]["tot_votes"],
                    )
                )

    # Make sure all the immediate neighbors come before precincts in outer layers
    nearest_neighbors: List[Neighbor] = neighbors[:split_index]
    nearest_neighbors.sort(key=lambda x: x.distance)
    other_neighbors: List[Neighbor] = neighbors[split_index:]
    other_neighbors.sort(key=lambda x: x.distance)

    return deque(nearest_neighbors + other_neighbors)


def make_neighborhood(
    geoid: str,
    data: Dict[str, Dict[str, Any]],
    graph: Dict[str, List[str]],
    *,
    ledger: DistanceLedger,
    target: int,
    pop_tol: float = 0.01,
    debug: bool = False,
) -> Deque[Neighbor]:
    """
    Return the 'neighborhood' for precinct.

    * Start with neighboring precincts sorted in order of increasing distance.
    * Left-remove precincts from that list and right-add them to a do-list of precincts to try to add.
    * For each precinct in the do-list (continuing in order of increasing distance):
      - If the total population would still be less than the threshold, and
      - If the neighborhood would remain connected,
      - Add the precinct to the neighborhood.
    * Then remove precincts from the neighborhood that reduce the deviation from the target population,
      in the order they were added (to maintain connectivity).

    """

    # Make a sorted list of candidate neighbors

    rg_q: Deque[Neighbor] = make_region(
        geoid, data, graph, ledger=ledger, target=target, debug=debug
    )

    # Add the nearest neighbors to the neighborhood until the population threshold is reached

    start: Neighbor = rg_q.popleft()
    nh_pop: int = start.pop
    nh_ids: List[str] = [start.geoid]

    nh_q: Deque[Neighbor] = deque([start])
    do_q: Deque[Neighbor] = deque([])

    i: int = 0
    while rg_q:
        i += 1
        do_q.append(rg_q.popleft())

        for n in list(do_q):
            if (nh_pop + n.pop) < target * (1.0 + pop_tol):
                nh_ids.append(n.geoid)
                if rda.is_connected(nh_ids, graph):
                    nh_q.append(n)
                    nh_pop += n.pop
                    do_q.remove(n)
                else:
                    nh_ids.pop()

            pass

    # NOTE - How do you distinguish between exhausting the region queue and
    # not being able to add any more connected precincts to get w/in tolerance?
    pop_dev_pct: float = (nh_pop - target) / target
    assert (
        abs(pop_dev_pct) < pop_tol
    ), f"Population deviation {pop_dev_pct} exceeds tolerance {pop_tol}!"

    # Remove precincts while that reduces the deviation from the target population

    prev_dev: int = abs(nh_pop - target)
    while True:
        last: Neighbor = nh_q.pop()
        new_dev: int = abs(nh_pop - last.pop - target)
        if new_dev < prev_dev:
            nh_pop -= last.pop
            prev_dev = new_dev
        else:
            nh_q.append(last)
            break

    return nh_q


def neighborhood_results(nh_q: Deque[Neighbor]) -> Tuple[float, float, float]:
    """Calculate the partisan results for a precinct's neighborhood."""

    dem_votes: int = 0
    tot_votes: int = 0
    for n in nh_q:
        dem_votes += n.dem_votes
        tot_votes += n.tot_votes

    Vf: float = dem_votes / tot_votes
    fractional_seats: float = rda.est_seat_probability(Vf)
    whole_seats: float = 1.0 if Vf > 0.5 else 0.0
    if approx_equal(Vf, 0.5):
        whole_seats = 0.5

    return Vf, fractional_seats, whole_seats


### END ###
