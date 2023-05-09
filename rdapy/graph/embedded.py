#!/usr/bin/env python3

"""
EMBEDDED - Is one district fully embedded w/in another district?
"""

from typing import Any

from .constants import *


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

    feature_ids: set[str] = inverted_plan[district_id]

    if not feature_ids:
        return True

    neighboring_districts: set[int | str] = set()

    for geoid in feature_ids:
        neighbors: list[str] = graph[geoid]

        for neighbor in neighbors:
            if neighbor == OUT_OF_STATE:
                return False

            neighboring_district: int | str = plan[neighbor]

            # Assume that a missing district assignment means that the feature is
            # "water-only" AND part of the border (vs.internal) and, therefore,
            # not in the plan / map.

            if neighboring_district == None:
                return False

            if neighboring_district != district_id:
                neighboring_districts.add(neighboring_district)
                if len(neighboring_districts) > 1:
                    return False

    return True


__all__ = ["is_embedded"]

### END ###
