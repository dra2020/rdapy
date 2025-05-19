"""
GEOGRAPHIC "NEIGHBORHOODS" A LA JON EGUIA & JEFF BARTON
"""

from typing import Any, List, Dict, Tuple, Set, NamedTuple, Generator

from ...partisan import est_seat_probability
from ...graph import is_connected, OUT_OF_STATE
from ...utils import approx_equal, DistanceLedger
from .packunpack import deserialize_bits, get_bit


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
    target_size: int,
    debug: bool = False,
) -> List[Neighbor]:
    """Find the 'neighborhood' around a precinct closest to the target size."""

    neighborhood: List[Neighbor] = list()
    neighborhood_pop: int = 0

    for i, neighbor in enumerate(
        nearest_connected_neighbor(
            geoid, data_by_geoid, total_pop_field, graph, ledger=ledger, debug=debug
        )
    ):
        if i == 0:
            neighborhood.append(neighbor)
            neighborhood_pop = neighbor.pop
            continue

        new_pop: int = neighborhood_pop + neighbor.pop

        if new_pop <= target_size:
            neighborhood.append(neighbor)
            neighborhood_pop += neighbor.pop
            continue

        if new_pop > target_size and (new_pop - target_size) < (
            target_size - neighborhood_pop
        ):
            neighborhood.append(neighbor)
            neighborhood_pop += neighbor.pop

        break

    assert len(neighborhood) > 0, f"Neighborhood is empty for {geoid}!"

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

    nneighbors: int = len(neighbors)
    checksum: int = sum(neighbors)

    assert geoid in neighborhood, f"{geoid} in not in own neighborhood"
    assert (
        nneighbors == packed_data["size"]
    ), f"Wrong size neighborhood for {geoid} ({nneighbors} vs. {packed_data['size']})"
    assert checksum == packed_data["checksum"], f"Checksum mismatch for {geoid}"

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
