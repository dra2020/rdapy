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

    def test_hypothetical_B(self) -> None:
        """Hypothetical B (2-proportionality)"""

        profile_path: str = "testdata/partisan/warrington/partisan-Hypothetical-B.json"
        profile: dict = read_json(profile_path)

        s: dict = calc_partisan_metrics(profile["statewide"], profile["byDistrict"])

        assert s["bias"]["bestS"] == 15
        assert approx_equal(s["bias"]["bestSf"], 0.6000, places=4)
        assert approx_equal(s["bias"]["estS"], 17.3000, places=4)
        assert approx_equal(s["bias"]["estSf"], 0.6920, places=4)
        assert approx_equal(s["bias"]["deviation"], -0.0920, places=4)
        assert approx_equal(s["responsiveness"]["littleR"], 1.6134, places=4)
        assert approx_equal(s["responsiveness"]["rD"], 4.3329, places=4)
        assert approx_equal(s["responsiveness"]["rDf"], 0.1733, places=4)

    def test_hypothetical_C(self) -> None:
        """Hypothetical C (3-proportionality)"""

        profile_path: str = "testdata/partisan/warrington/partisan-Hypothetical-C.json"
        profile: dict = read_json(profile_path)

        s: dict = calc_partisan_metrics(profile["statewide"], profile["byDistrict"])

        assert s["bias"]["bestS"] == 15
        assert approx_equal(s["bias"]["bestSf"], 0.6000, places=4)
        assert approx_equal(s["bias"]["estS"], 19.9419, places=4)
        assert approx_equal(s["bias"]["estSf"], 0.7977, places=4)
        assert approx_equal(s["bias"]["deviation"], -0.1977, places=4)
        assert approx_equal(s["responsiveness"]["littleR"], 2.4315, places=4)
        assert approx_equal(s["responsiveness"]["rD"], 6.5433, places=4)
        assert approx_equal(s["responsiveness"]["rDf"], 0.2617, places=4)

    def test_hypothetical_D(self) -> None:
        """Hypothetical D (Sweep)"""

        profile_path: str = "testdata/partisan/warrington/partisan-Hypothetical-D.json"
        profile: dict = read_json(profile_path)

        s: dict = calc_partisan_metrics(profile["statewide"], profile["byDistrict"])

        assert s["bias"]["bestS"] == 6
        assert approx_equal(s["bias"]["bestSf"], 0.6000, places=4)
        assert approx_equal(s["bias"]["estS"], 9.8384, places=4)
        assert approx_equal(s["bias"]["estSf"], 0.9838, places=4)
        assert approx_equal(s["bias"]["deviation"], -0.3838, places=4)
        assert approx_equal(s["responsiveness"]["littleR"], 0.7471, places=4)
        assert approx_equal(s["responsiveness"]["rD"], 0.5947, places=4)
        assert approx_equal(s["responsiveness"]["rDf"], 0.0595, places=4)

    def test_hypothetical_E(self) -> None:
        """Hypothetical E (Competitive)"""

        profile_path: str = "testdata/partisan/warrington/partisan-Hypothetical-E.json"
        profile: dict = read_json(profile_path)

        s: dict = calc_partisan_metrics(profile["statewide"], profile["byDistrict"])

        assert s["bias"]["bestS"] == 6
        assert approx_equal(s["bias"]["bestSf"], 0.5000, places=4)
        assert approx_equal(s["bias"]["estS"], 7.9977, places=4)
        assert approx_equal(s["bias"]["estSf"], 0.6665, places=4)
        assert approx_equal(s["bias"]["deviation"], -0.1665, places=4)
        assert approx_equal(s["responsiveness"]["littleR"], 8.0289, places=4)
        assert approx_equal(s["responsiveness"]["rD"], 9.1389, places=4)
        assert approx_equal(s["responsiveness"]["rDf"], 0.7616, places=4)

    def test_hypothetical_F(self) -> None:
        """Hypothetical F (Competitive even)"""

        profile_path: str = "testdata/partisan/warrington/partisan-Hypothetical-F.json"
        profile: dict = read_json(profile_path)

        s: dict = calc_partisan_metrics(profile["statewide"], profile["byDistrict"])

        assert s["bias"]["bestS"] == 5
        assert approx_equal(s["bias"]["bestSf"], 0.5000, places=4)
        assert approx_equal(s["bias"]["estS"], 5.6574, places=4)
        assert approx_equal(s["bias"]["estSf"], 0.5657, places=4)
        assert approx_equal(s["bias"]["deviation"], -0.0657, places=4)
        assert approx_equal(s["responsiveness"]["littleR"], 4.9970, places=4)
        assert approx_equal(s["responsiveness"]["rD"], 4.5606, places=4)
        assert approx_equal(s["responsiveness"]["rDf"], 0.4561, places=4)

    def test_hypothetical_G(self) -> None:
        """Hypothetical G (Uncompetitive)"""

        profile_path: str = "testdata/partisan/warrington/partisan-Hypothetical-G.json"
        profile: dict = read_json(profile_path)

        s: dict = calc_partisan_metrics(profile["statewide"], profile["byDistrict"])

        assert s["bias"]["bestS"] == 5
        assert approx_equal(s["bias"]["bestSf"], 0.5000, places=4)
        assert approx_equal(s["bias"]["estS"], 5.9932, places=4)
        assert approx_equal(s["bias"]["estSf"], 0.5993, places=4)
        assert approx_equal(s["bias"]["deviation"], -0.0993, places=4)
        assert approx_equal(s["responsiveness"]["littleR"], 0.0541, places=4)
        assert approx_equal(s["responsiveness"]["rD"], 0.0273, places=4)
        assert approx_equal(s["responsiveness"]["rDf"], 0.0027, places=4)

    def test_hypothetical_H(self) -> None:
        """Hypothetical H (Very uncompetitive)"""

        profile_path: str = "testdata/partisan/warrington/partisan-Hypothetical-H.json"
        profile: dict = read_json(profile_path)

        s: dict = calc_partisan_metrics(profile["statewide"], profile["byDistrict"])

        assert s["bias"]["bestS"] == 5
        assert approx_equal(s["bias"]["bestSf"], 0.5000, places=4)
        assert approx_equal(s["bias"]["estS"], 6.0000, places=4)
        assert approx_equal(s["bias"]["estSf"], 0.6000, places=4)
        assert approx_equal(s["bias"]["deviation"], -0.1000, places=4)
        assert approx_equal(s["responsiveness"]["littleR"], 0.0000, places=4)
        assert approx_equal(s["responsiveness"]["rD"], 0.0000, places=4)
        assert approx_equal(s["responsiveness"]["rDf"], 0.0000, places=4)

    def test_hypothetical_I(self) -> None:
        """Hypothetical I (Cubic)"""

        profile_path: str = "testdata/partisan/warrington/partisan-Hypothetical-I.json"
        profile: dict = read_json(profile_path)

        s: dict = calc_partisan_metrics(profile["statewide"], profile["byDistrict"])

        assert s["bias"]["bestS"] == 6
        assert approx_equal(s["bias"]["bestSf"], 0.6000, places=4)
        assert approx_equal(s["bias"]["estS"], 7.3984, places=4)
        assert approx_equal(s["bias"]["estSf"], 0.7398, places=4)
        assert approx_equal(s["bias"]["deviation"], -0.1398, places=4)
        assert approx_equal(s["responsiveness"]["littleR"], 1.9415, places=4)
        assert approx_equal(s["responsiveness"]["rD"], 1.7073, places=4)
        assert approx_equal(s["responsiveness"]["rDf"], 0.1707, places=4)

    def test_hypothetical_J(self) -> None:
        """Hypothetical J (Anti-majoritarian)"""

        profile_path: str = "testdata/partisan/warrington/partisan-Hypothetical-J.json"
        profile: dict = read_json(profile_path)

        s: dict = calc_partisan_metrics(profile["statewide"], profile["byDistrict"])

        assert s["bias"]["bestS"] == 4
        assert approx_equal(s["bias"]["bestSf"], 0.4000, places=4)
        assert approx_equal(s["bias"]["estS"], 5.5598, places=4)
        assert approx_equal(s["bias"]["estSf"], 0.5560, places=4)
        assert approx_equal(s["bias"]["deviation"], -0.1560, places=4)
        assert approx_equal(s["responsiveness"]["littleR"], 1.6239, places=4)
        assert approx_equal(s["responsiveness"]["rD"], 1.3331, places=4)
        assert approx_equal(s["responsiveness"]["rDf"], 0.1333, places=4)

    def test_hypothetical_K(self) -> None:
        """Hypothetical K (Classic)"""

        profile_path: str = "testdata/partisan/warrington/partisan-Hypothetical-K.json"
        profile: dict = read_json(profile_path)

        s: dict = calc_partisan_metrics(profile["statewide"], profile["byDistrict"])

        assert s["bias"]["bestS"] == 5
        assert approx_equal(s["bias"]["bestSf"], 0.5000, places=4)
        assert approx_equal(s["bias"]["estS"], 3.3882, places=4)
        assert approx_equal(s["bias"]["estSf"], 0.3388, places=4)
        assert approx_equal(s["bias"]["deviation"], 0.1612, places=4)
        assert approx_equal(s["responsiveness"]["littleR"], 1.3046, places=4)
        assert approx_equal(s["responsiveness"]["rD"], 1.2957, places=4)
        assert approx_equal(s["responsiveness"]["rDf"], 0.1296, places=4)

    def test_hypothetical_L(self) -> None:
        """Hypothetical L (Inverted)"""

        profile_path: str = "testdata/partisan/warrington/partisan-Hypothetical-L.json"
        profile: dict = read_json(profile_path)

        s: dict = calc_partisan_metrics(profile["statewide"], profile["byDistrict"])

        assert s["bias"]["bestS"] == 3
        assert approx_equal(s["bias"]["bestSf"], 0.3000, places=4)
        assert approx_equal(s["bias"]["estS"], 1.7961, places=4)
        assert approx_equal(s["bias"]["estSf"], 0.1796, places=4)
        assert approx_equal(s["bias"]["deviation"], 0.1204, places=4)
        assert approx_equal(s["responsiveness"]["littleR"], 5.025, places=4)
        assert approx_equal(s["responsiveness"]["rD"], 2.8831, places=4)
        assert approx_equal(s["responsiveness"]["rDf"], 0.2883, places=4)

    def test_CA_2012(self) -> None:
        """CA 2012 from research project #2 w/ John Nagle"""

        profile_path: str = "testdata/partisan/nagle/partisan-CA-2012.json"
        profile: dict = read_json(profile_path)

        points: dict = key_RV_points(profile["byDistrict"])
        Sb: float = points["Sb"]
        Ra: float = points["Ra"]
        Rb: float = points["Rb"]
        Va: float = points["Va"]
        Vb: float = points["Vb"]

        assert Va >= 0.50
        assert Vb <= 0.50
        assert Rb <= 0.50
        assert Ra >= 0.50

        s: dict = calc_partisan_metrics(profile["statewide"], profile["byDistrict"])

        assert s["bias"]["bestS"] == 31
        assert approx_equal(s["bias"]["bestSf"], 0.5849, places=4)
        assert approx_equal(s["bias"]["estS"], 38.652689, places=4)
        assert approx_equal(s["bias"]["estSf"], 0.7293, places=4)
        assert approx_equal(s["bias"]["deviation"], -0.1444, places=4)
        assert approx_equal(s["bias"]["tOf"], -0.006566, places=4)
        assert approx_equal(s["bias"]["bS50"], -0.01792670, places=4)
        assert approx_equal(s["bias"]["bV50"], -0.00609430, places=4)
        # assert approx_equal(s["bias"]["bSV"], 0.0330327, places=4)  # TODO: Check this
        assert approx_equal(s["bias"]["gamma"], -5.07 / 100, places=4)
        assert approx_equal(s["bias"]["eG"], -0.04511401, places=4)

        assert approx_equal(s["bias"]["mMs"], -0.00972344444444451, places=4)
        assert approx_equal(s["bias"]["mMd"], -0.003123, places=4)
        assert approx_equal(s["bias"]["lO"], 9.23242870162867 / 100, places=4)

        assert approx_equal(s["responsiveness"]["littleR"], 1.939018, places=4)
        assert approx_equal(s["responsiveness"]["rD"], 8.534675, places=4)
        assert approx_equal(s["responsiveness"]["rDf"], 0.1610, places=4)

    def test_CO_2012(self) -> None:
        """C0 2012 from research project #2 w/ John Nagle.

        NOTE - These districts are *not* sorted in order by Vf."""

        profile_path: str = "testdata/partisan/nagle/partisan-CO-2012.json"
        profile: dict = read_json(profile_path)

        points: dict = key_RV_points(profile["byDistrict"])
        Sb: float = points["Sb"]
        Ra: float = points["Ra"]
        Rb: float = points["Rb"]
        Va: float = points["Va"]
        Vb: float = points["Vb"]

        assert Va >= 0.50
        assert Vb <= 0.50
        assert Rb <= 0.50
        assert Ra >= 0.50

        s: dict = calc_partisan_metrics(profile["statewide"], profile["byDistrict"])

        assert s["bias"]["bestS"] == 4
        assert approx_equal(s["bias"]["bestSf"], 0.5714, places=4)
        assert approx_equal(s["bias"]["estS"], 3.553689, places=4)
        assert approx_equal(s["bias"]["estSf"], 0.5077, places=4)
        assert approx_equal(s["bias"]["deviation"], 0.0638, places=4)
        assert approx_equal(s["bias"]["tOf"], 0.002829, places=4)
        assert approx_equal(s["bias"]["bS50"], 0.01355483, places=4)
        assert approx_equal(s["bias"]["bV50"], 0.00354176, places=4)
        # assert approx_equal(s["bias"]["bSV"], 0.0137603, places=4)  # TODO: Check this
        assert approx_equal(s["bias"]["gamma"], 1.35 / 100, places=4)
        assert approx_equal(s["bias"]["eG"], 0.00345216, places=4)

        assert approx_equal(s["bias"]["mMs"], 0.0135999999999999, places=4)
        assert approx_equal(s["bias"]["mMd"], 0.010771, places=4)
        assert approx_equal(s["bias"]["lO"], 0.313178142621696 / 100, places=4)

        assert approx_equal(s["responsiveness"]["littleR"], 3.801580, places=4)
        assert approx_equal(s["responsiveness"]["rD"], 2.487388, places=4)
        assert approx_equal(s["responsiveness"]["rDf"], 0.3553, places=4)


### END ###
