#!/usr/bin/env python3

"""
NORMALIZE
"""

# Constants

NORMALIZED_RANGE: int = 100
DISTANCE_WEIGHT: int = 2  # Square deviations from the ideal


class Normalizer:
    raw_num: float
    wip_num: float
    normalized_num: int

    def __init__(self, raw_value: float) -> None:
        self.raw_num = raw_value
        self.wip_num = raw_value

    # *Don't* transform the input.
    def identity(self) -> float:
        return self.wip_num

    def positive(self) -> float:
        self.wip_num = abs(self.wip_num)
        return self.wip_num

    # Invert a value in the unit range [0.0–1.0] (so that bigger is better).
    def invert(self) -> float:
        assert (self.wip_num >= 0.0) and (self.wip_num <= 1.0)

        self.wip_num = 1.0 - self.wip_num
        return self.wip_num

    # Constrain the value to be within a specified range.
    def clip(self, begin_range: float, end_range: float) -> float:
        # Handle the ends of the range being given either order
        min_range: float = min(begin_range, end_range)
        max_range: float = max(begin_range, end_range)

        self.wip_num = max(min(self.wip_num, max_range), min_range)

        return self.wip_num

    # Recast the value as the delta from a baseline value. NOOP if it is zero.
    # NOTE - Values can be + or -.
    def rebase(self, base: float) -> float:
        self.wip_num -= base
        return self.wip_num

    # Re-scale a value into the [0.0 – 1.0] range, using a given range.
    # NOTE - This assumes that values have alrady been clipped into the range.
    def unitize(self, begin_range: float, end_range: float) -> float:
        # Handle the ends of the range being given either order
        min_range: float = min(begin_range, end_range)
        max_range: float = max(begin_range, end_range)

        assert (self.wip_num >= min_range) and (self.wip_num <= max_range)

        ranged: float = self.wip_num - min_range
        self.wip_num = abs(ranged / (end_range - begin_range))

        return self.wip_num

    # Decay a value in the unit range [0.0–1.0] by its distance from zero.
    # NOTE - If the range is already such that "bigger is better," then the closer
    #   the value is to 1.0 (the best) the *less* it will decay.
    def decay(self) -> float:
        assert (self.wip_num >= 0.0) and (self.wip_num <= 1.0)

        self.wip_num = pow(self.wip_num, DISTANCE_WEIGHT)
        return self.wip_num

    # Translate a value in the unit range to the user-friendly range [0 – 100].
    def rescale(self) -> int:
        assert (self.wip_num >= 0.0) and (self.wip_num <= 1.0)

        self.normalized_num = round(self.wip_num * NORMALIZED_RANGE)
        return self.normalized_num


### END ###
