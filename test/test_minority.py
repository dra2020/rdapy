#!/usr/bin/env python3

"""
TEST MINORITY OPPORTUNITY
"""

from rdapy import (
    calc_proportional_districts,
    est_minority_opportunity,
    calc_minority_opportunity,
    approx_equal,
    read_json,
    DEMOGRAPHICS,
    EPSILON,
)


class TestMinority:
    def test_calc_proportional_districts(self) -> None:
        n_districts = 10

        # Zero
        assert calc_proportional_districts(0.0, n_districts) == 0

        # Not quite one
        assert (
            calc_proportional_districts((1 / n_districts) - 0.05 - EPSILON, n_districts)
            == 0
        )

        # One
        assert calc_proportional_districts(1 / n_districts, n_districts) == 1

        # Not quite two
        assert (
            calc_proportional_districts(
                (2 * (1 / n_districts)) - 0.05 - EPSILON, n_districts
            )
            == 1
        )

        # Two
        assert calc_proportional_districts(2 * (1 / n_districts), n_districts) == 2

    def test_est_minority_opportunity(self) -> None:
        # 35%
        assert approx_equal(est_minority_opportunity(0.3500), 0.0)
        # 37%
        assert approx_equal(est_minority_opportunity(0.3700), 0.6914624612740132)
        # 38%
        assert approx_equal(est_minority_opportunity(0.3800), 0.773372647623132)
        # 49%
        assert approx_equal(est_minority_opportunity(0.4900), 0.9997673709209645)
        # 50%
        assert approx_equal(est_minority_opportunity(0.5000), 0.9999115827147992)
        # 51%
        assert approx_equal(est_minority_opportunity(0.5100), 0.9999683287581669)
        # 90%
        assert approx_equal(est_minority_opportunity(0.9000), 1.0)

    def test_calc_minority_opportunity(self) -> None:
        """Evaluate TX minority opportunity"""

        p: dict = read_json("testdata/CD116/profile-TX-CD116.json")
        # Proportional districts by demographic

        n_districts: int = p["nDistricts"]
        statewide_demos: dict[str, float] = p["demographics"]["statewide"]
        statewide_demos.pop("white")
        correct: list[int] = [18, 4, 12, 0, 2, 0]

        districts_by_demo: dict[str, int] = {
            x: calc_proportional_districts(statewide_demos[x], n_districts)
            for x in DEMOGRAPHICS[1:]
        }
        assert list(districts_by_demo.values()) == correct

        # Estimate opportunity & coalition districts', () =>
        demos_by_district: list[dict[str, float]] = p["demographics"]["byDistrict"]
        ms: dict = calc_minority_opportunity(statewide_demos, demos_by_district)
        assert approx_equal(ms["opportunity_districts"], 12.56, 2)
        assert approx_equal(ms["proportional_opportunities"], 18)
        assert approx_equal(ms["coalition_districts"], 22.92, 2)
        assert approx_equal(ms["proportional_coalitions"], 18)


### END ###
