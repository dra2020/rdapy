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


### END ###
