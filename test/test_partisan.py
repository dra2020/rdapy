#!/usr/bin/env python3

"""
TEST PARTIAN SCORECARD
"""


from rdapy.partisan.partisan import *
from testutils import *


class TestPartisanScorecard:
    def test_PA_SCOPA_7S(self) -> None:
        """PA SCOPA-7S plan"""

        profile_path: str = "testdata/partisan/nagle/partisan-PA-SCOPA-7S.json"
        profile: dict = read_json(profile_path)

        rV: list[float] = profile["byDistrict"]
        N: int = len(rV)
        Vf: float = profile["statewide"]
        proportional: bool = True

        actual_sv_points: list[tuple[float, float]] = infer_sv_points(
            Vf, rV, proportional
        )

        # Estimate # of responsive districts

        assert approx_equal(est_responsive_districts(rV), 6.57, places=2)

        # Estimate responsive at statewide Vf

        assert approx_equal(est_responsiveness(Vf, actual_sv_points, N), 3.76, places=2)

        # Estimate simple seat bias @ V = 50%

        assert approx_equal(est_seats_bias(actual_sv_points, N), 2.0, places=1)

        # Estimate simple votes bias @ V = 50%

        assert approx_equal(est_votes_bias(actual_sv_points, N), 0.0310, places=4)

        # Calculate the efficiency gap (FPTP)

        fptpSf: float = est_fptp_seats(rV) / N
        assert approx_equal(calc_efficiency_gap(Vf, fptpSf), 0.0418, places=4)

        # Calculate the efficiency gap (w/ seat probabilities)

        estS: float = est_seats(rV)
        estSf: float = estS / N
        assert approx_equal(calc_efficiency_gap(Vf, estSf), 0.033, places=3)

    def test_hypothetical_A(self) -> None:
        """Hypothetical A (1-proportionality)"""

        profile_path: str = "testdata/partisan/warrington/partisan-Hypothetical-A.json"
        profile: dict = read_json(profile_path)

        s: dict = calc_partisan_metrics(profile["statewide"], profile["byDistrict"])

        # Estimate ^S#

        assert s["bias"]["bestS"] == 14

        # Estimate ^S%

        assert approx_equal(s["bias"]["bestSf"], 0.6087, places=4)

        # Estimate S#

        assert approx_equal(s["bias"]["estS"], 13.8076, places=4)

        # S%

        assert approx_equal(s["bias"]["estSf"], 0.6003, places=4)

        # Estimate B%

        assert approx_equal(s["bias"]["deviation"], 0.0084, places=4)

        # Estimate R#

        assert approx_equal(s["responsiveness"]["littleR"], 0.8431, places=4)

        # Estimate Rd

        assert approx_equal(s["responsiveness"]["rD"], 2.0833, places=4)

        # Estimate Rd%

        assert approx_equal(s["responsiveness"]["rDf"], 0.0906, places=4)


### END ###
