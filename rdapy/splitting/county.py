#!/usr/bin/env python3

"""
COUNTY-DISTRICT SPLITTING -- building on Moon Duchin's work
"""

import math


def split_score(split: list[float]) -> float:
    """Moon Duchin's raw split score"""

    if len(split) > 0:
        return sum(map(math.sqrt, split))
    else:
        return 1.0


# LIMIT WHAT GETS EXPORTED.

__all__ = ["split_score"]

### END ###
