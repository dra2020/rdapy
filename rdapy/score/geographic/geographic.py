"""
GEOGRAPHIC "NEIGHBORHOODS" A LA JON EGUIA & JEFF BARTON
"""

from typing import Any, List, Dict, Tuple, Set, NamedTuple, Generator, TextIO

import math

from rdapy.partisan import est_seat_probability
from rdapy.graph import is_connected, OUT_OF_STATE
from rdapy.utils import approx_equal

from .packunpack import deserialize_bits, get_bit


def distance_proxy(a: Tuple[float, float], b: Tuple[float, float]) -> float:
    """
    Calculate a proxy for the distance between two points expressed as (lon, lat) tuples.

    No need for sqrt() since we are only *comparing* distances.
    """

    lat_squared: float = (a[1] - b[1]) * (a[1] - b[1])
    lon_squared: float = (a[0] - b[0]) * (a[0] - b[0])

    return lat_squared + lon_squared


def distance(a: Tuple[float, float], b: Tuple[float, float]) -> float:
    """Calculate the distance between two points expressed as (lon, lat) tuples."""

    return math.sqrt((a[1] - b[1]) * (a[1] - b[1]) + (a[0] - b[0]) * (a[0] - b[0]))


def make_precinct_pair(precinct1: str, precinct2: str) -> Tuple[str, str]:
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
        pair: Tuple[str, str] = make_precinct_pair(geoid1, geoid2)
        if pair in self.distances:
            return self.distances[pair]
        else:
            d: float = distance_proxy(center1, center2)
            self.distances[pair] = d
            return d


class Neighbor(NamedTuple):
    geoid: str
    distance: float
    pop: int


def nearest_connected_neighbor(
    node: str,
    data_by_geoid: Dict[str, Dict[str, Any]],
    total_pop_field: str,
    graph: Dict[str, List[str]],
    *,
    ledger: DistanceLedger,
    debug: bool = False,
) -> Generator[Neighbor, None, None]:
    """Return the nearest connected neighbors to a precinct in increasing order of distance."""

    yielded: Set[str] = set()
    queue: List[Neighbor] = [Neighbor(node, 0.0, data_by_geoid[node][total_pop_field])]

    while True:
        if len(queue) == 0:
            return

        next: Neighbor = queue.pop()

        yielded.add(next.geoid)
        assert is_connected(
            list(yielded), graph
        ), f"Yields must maintain connectivity: {next.geoid}"

        in_queue: Set[str] = set([n.geoid for n in queue])
        new_candidates: List[str] = [
            neighbor
            for neighbor in graph[next.geoid]
            if neighbor not in yielded
            and neighbor not in in_queue
            and neighbor != OUT_OF_STATE
        ]
        for neighbor in new_candidates:
            queue.append(
                Neighbor(
                    neighbor,
                    ledger.distance_between(
                        node,
                        data_by_geoid[node]["center"],
                        neighbor,
                        data_by_geoid[neighbor]["center"],
                    ),
                    data_by_geoid[neighbor][total_pop_field],
                )
            )
        queue.sort(key=lambda x: x.distance, reverse=True)

        yield next


def make_neighborhood(
    geoid: str,
    data_by_geoid: Dict[str, Dict[str, Any]],
    total_pop_field: str,
    graph: Dict[str, List[str]],
    *,
    ledger: DistanceLedger,
    size: int,
    slack: float = 0.05,
    debug: bool = False,
) -> List[Neighbor]:
    """Find the 'neighborhood' around a precinct."""

    neighborhood: List[Neighbor] = list()

    # NOTE - This could theoretically terminate earlier than ideally,
    # if the last attempted neighbor is too large. One could skip that one
    # and continue, provided the neighborhood were still connected.
    # The generator doesn't support skipping yielded precincts though.

    # TODO - Alternatively, one could choose to add the last neighbor,
    # if it puts the neighborhood over the target size, but the delta
    # would be smaller than not adding it. This would make neighborhoods
    # "the closest to target size."
    for neighbor in nearest_connected_neighbor(
        geoid, data_by_geoid, total_pop_field, graph, ledger=ledger, debug=debug
    ):
        if neighbor.pop + sum([n.pop for n in neighborhood]) < size * (1.0 - slack):
            neighborhood.append(neighbor)
        else:
            break

    return neighborhood


def unpack_neighborhood(
    geoid: str,
    packed_data: Dict[str, Any],
    index_to_geoid: Dict[int, str],
    debug: bool = False,
) -> List[str]:
    """Deserialize a neighborhood from a JSON string & verify it."""

    bits = deserialize_bits(packed_data["neighborhood"])
    size = len(bits) * 8

    neighbors: List[int] = [idx for idx in range(size) if get_bit(bits, idx)]

    assert min(neighbors) >= 0, f"Negative index in neighborhood for {geoid}"
    assert max(neighbors) < len(
        index_to_geoid.keys()
    ), f"Index out of range in neighborhood for {geoid}"

    neighborhood: List[str] = [index_to_geoid[idx] for idx in neighbors]

    if debug:
        nneighbors: int = len(neighbors)
        checksum: int = sum(neighbors)

        assert geoid in neighborhood, f"{geoid} in not in own neighborhood"
        assert (
            nneighbors == packed_data["size"]
        ), f"Wrong size neighborhood for {geoid} ({nneighbors} vs. {packed_data['size']})"
        assert checksum == packed_data["checksum"], f"Checksum mismatch for {geoid}"

        print(f"Neighborhood for {geoid} roundtripped successfully ...")

    return neighborhood


def eval_partisan_lean(
    neighborhood: List[str],
    data: Dict[str, Dict[str, Any]],
    dem_votes_field: str,
    tot_votes_field: str,
) -> Tuple[float, float, float]:
    """Calculate the partisan results for a precinct's neighborhood."""

    dem_votes: int = 0
    tot_votes: int = 0
    for geoid in neighborhood:
        dem_votes += data[geoid][dem_votes_field]
        tot_votes += data[geoid][tot_votes_field]

    Vf: float = dem_votes / tot_votes if tot_votes > 0 else 0.0
    fractional_seats: float = est_seat_probability(Vf)
    whole_seats: float = 1.0 if Vf > 0.5 else 0.0
    if approx_equal(Vf, 0.5):
        whole_seats = 0.5

    return Vf, fractional_seats, whole_seats


def calc_geographic_baseline(
    neighborhoods: List[Dict[str, Any]],
    ndistricts: int,
    state_pop: int,
    data: Dict[str, Dict[str, Any]],
    geoids: List[str],
    total_pop_field: str,
    dem_votes_field: str,
    tot_votes_field: str,
    *,
    debug: bool = False,
) -> Tuple[float, float]:
    """Calculate Jon Eguia & Jeff Barton's geographic baseline for a state."""

    tot_fractional_seats: float = 0.0
    tot_whole_seats: float = 0.0

    for precinct in neighborhoods:
        geoid: str = precinct["geoid"]
        neighborhood: List[str] = precinct["neighborhood"]

        pop: int = data[geoid][total_pop_field]

        Vf: float
        fractional_seats: float
        whole_seats: float
        Vf, fractional_seats, whole_seats = eval_partisan_lean(
            neighborhood,
            data,
            dem_votes_field,
            tot_votes_field,
        )

        proportion: float = ndistricts * (pop / state_pop)
        tot_fractional_seats += fractional_seats * proportion
        tot_whole_seats += whole_seats * proportion

    return tot_fractional_seats, tot_whole_seats


### END ###
