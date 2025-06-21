#!/usr/bin/env python3

"""
TEST POPULATION DEVIATION
"""

from rdapy import *


class TestPopulationDeviation:
    def test_calc_population_deviation(self) -> None:
        assert approx_equal(
            calc_population_deviation(100, 100, 100), 0.0, places=4
        )  # Equal
        assert approx_equal(
            calc_population_deviation(105, 95, 100), 0.10, places=4
        )  # 10% deviation

        # NC 116th Congressional Districts
        profile: dict = read_json("testdata/population/population-NC-116th.json")
        max_pop: int = max(profile["byDistrict"])
        min_pop: int = min(profile["byDistrict"])
        target_pop: int = profile["targetSize"]
        assert approx_equal(
            calc_population_deviation(max_pop, min_pop, target_pop),
            0.016033,
            places=4,
        )

        # Extremely large deviation
        districts: list[int] = [
            485999,
            620961,
            971777,
            863420,
            167134,
            287085,
            549714,
            1827462,
        ]
        target_pop: int = 721694
        assert approx_equal(
            calc_population_deviation(max(districts), min(districts), target_pop),
            2.3006,
            places=4,
        )


### END ###
