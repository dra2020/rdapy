#!/usr/bin/env python3

"""
POPULATION DEVIATION
"""


def calc_population_deviation(max_pop: int, min_pop: int, target_pop: int) -> float:
    """Compute the population deviation for a set of districts."""

    deviation: float = (max_pop - min_pop) / target_pop

    return deviation


### END ###
