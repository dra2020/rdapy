"""
MAJORITARIAN-MINORITY DISTRICTS (MMD) SCORES
"""

from typing import List, Dict, Optional

from collections import defaultdict

from .aggregate import NamedAggregates


def calculate_mmd_with_comparisons(
    cvap_aggs: NamedAggregates,
    shape_aggs: NamedAggregates,
    census_aggs: NamedAggregates,
) -> Dict[str, Optional[float | int]]:
    """
    Count majority-minority districts (MMD).

    NOTE -- The way this is implemented counts the # of districts correctl, but is
    potentially confusing. There are 3 mutually exclusive scenarios for MMD:
    1. Black alone majority-minority district
    2. Hispanic alone majority-minority district, and
    3. A coalition majority-minority district where Blacks and Hispanics *together*
       constitute a major though neither alone do (Scenarios 1 & 2).

    NOTE - This version is used by scripts/score_global.py.
    """

    mdd_count: int = 0
    mdds: List[int | str] = list()

    j: int = 0
    for black, hispanic, total in zip(
        cvap_aggs["black_cvap"][1:],
        cvap_aggs["hispanic_cvap"][1:],
        cvap_aggs["total_cvap"][1:],
    ):
        j += 1

        # Black majority-minority district
        scenario_1: bool = (black / total) > 0.5

        # Hispanic majority-minority district
        scenario_2: bool = (hispanic / total) > 0.5

        # Coalition majority-minority district
        scenario_3: bool = ((black + hispanic) / total) > 0.5

        if scenario_1 or scenario_2 or scenario_3:
            mdd_count += 1
            mdds.append(j)

        pass

    # Initialize averages for no MMD
    mdd_scores: Dict[str, Optional[float | int]] = dict()
    mdd_scores["mmd_districts"] = mdd_count

    data_access: Dict = {
        "reock": shape_aggs,
        "polsby_popper": shape_aggs,
        "district_splitting": census_aggs,
    }

    averages: List[str] = [
        "mmd_reock",
        "mmd_polsby_popper",
        "mmd_district_splitting",
    ]
    for a in averages:
        mdd_scores[a] = None

    # If there are MDD, calculate the averages for select metrics for them
    if mdd_count > 0:
        mdd_averages: Dict[str, float] = defaultdict(float)
        for d in mdds:
            i: int = int(d) - 1
            for a in averages:
                derived_from: str = a.split("mmd_")[1]
                aggs: NamedAggregates = data_access[derived_from]
                mdd_averages[a] += aggs[derived_from][i]

        mdd_averages = {k: v / mdd_count for k, v in mdd_averages.items()}
        mdd_scores.update(mdd_averages)

    return mdd_scores


def calculate_mmd_simple(
    cvap_aggs: NamedAggregates,
) -> Dict[str, int]:
    """
    Count majority-minority districts (MMD) in 3 separate, mutually exclusive buckets.

    1. Black alone majority-minority district
    2. Hispanic alone majority-minority district, and
    3. A coalition majority-minority district where Blacks and Hispanics *together*
       constitute a major though neither alone do (Scenarios 1 & 2).

    NOTE - This version is used by mainline scoring scripts/score_ensemble.py.
    """

    mmd_counts: Dict[str, int] = {"mmd_black": 0, "mmd_hispanic": 0, "mmd_coalition": 0}

    for black, hispanic, total in zip(
        cvap_aggs["black_cvap"][1:],
        cvap_aggs["hispanic_cvap"][1:],
        cvap_aggs["total_cvap"][1:],
    ):
        # Black majority-minority district
        if is_single_demo_mmd(black, total):
            mmd_counts["mmd_black"] += 1
            continue

        # Hispanic majority-minority district
        if is_single_demo_mmd(hispanic, total):
            mmd_counts["mmd_hispanic"] += 1
            continue

        # Coalition majority-minority district
        if is_coalition_mmd([black, hispanic], total):
            mmd_counts["mmd_coalition"] += 1
            continue

    return mmd_counts


def is_single_demo_mmd(demo_cvap: int, total_cvap: int) -> bool:
    """Check if a district is a single demographic MMD."""

    return (demo_cvap / total_cvap) > 0.5


def is_coalition_mmd(demo_cvaps: List[int], total_cvap: int) -> bool:
    """
    Check if a district is a coalition MMD:
    1. Each individual race/ethnicity must be <= half total CVAP, and
    2. All minority races/ethnicities together must be > half total CVAP

    """

    return (
        all(demo / total_cvap <= 0.5 for demo in demo_cvaps)
        and sum(demo_cvaps) / total_cvap > 0.5
    )


### END ###
