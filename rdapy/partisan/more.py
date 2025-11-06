"""
ADDITIONAL PARTISAN METRICS -- These are not calculated in DRA proper.
"""

from typing import List


def calc_efficiency_gap_wasted_votes(
    dem_votes_by_district: List[int], rep_votes_by_district: List[int]
) -> float:
    """
    Calculate efficiency gap using wasted votes (instead of the statewide formula).

    https://www.brennancenter.org/sites/default/files/legal-work/How_the_Efficiency_Gap_Standard_Works.pdf
    """

    total_votes: int = sum(dem_votes_by_district) + sum(rep_votes_by_district)

    assert len(dem_votes_by_district) == len(rep_votes_by_district)
    assert total_votes > 0

    dem_wasted_votes: int = 0
    rep_wasted_votes: int = 0

    for d, r in zip(dem_votes_by_district, rep_votes_by_district):
        threshold = (d + r) // 2 + 1
        if d > r:
            dem_wasted_votes += d - threshold
            rep_wasted_votes += r
        else:
            rep_wasted_votes += r - threshold
            dem_wasted_votes += d

    EGwv: float = (dem_wasted_votes - rep_wasted_votes) / total_votes

    return EGwv


def calc_average_margin(Vf_array: List[float]) -> float:
    """Calculate the average margin of victory."""

    margin: float = sum([abs(v - 0.5000) for v in Vf_array]) / len(Vf_array)

    return margin


def calc_gallagher_index(Vf_array: List[float], Sf_array: List[float]) -> float:
    """
    Calculate the Gallagher Index.
    https://en.wikipedia.org/wiki/Gallagher_index

    Vf_array: List of vote shares for parties.
    Sf_array: List of seat shares for parties.

    TODO - Splice this into the pipeline.
    """

    assert len(Vf_array) == len(Sf_array)

    sum_squared_diff: float = sum(
        [(Sf - Vf) ** 2 for Vf, Sf in zip(Vf_array, Sf_array)]
    )

    GI: float = (0.5 * sum_squared_diff) ** 0.5

    return GI


def calc_electability_index(Vf: float, district_magnitude: int) -> float:
    """
    The Electability Index for a given vote share and district magnitude
    is the vote share divided by the threshold of exclusion.

    Vf: Vote share (between 0 and 1)
    district_magnitude: Number of seats in the district
    """

    assert Vf >= 0 and Vf <= 1
    assert district_magnitude > 0

    threshold: float = 1 / (district_magnitude + 1)

    EI: float = Vf / threshold

    return EI


### END ###
