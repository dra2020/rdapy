#!/usr/bin/env python3

"""
TEST PARTISAN METRICS
"""

from rdapy import (
    read_json,
    approx_equal,
    infer_sv_points,
    est_responsiveness,
    est_responsive_districts,
    est_seats,
    est_seats_bias,
    est_votes_bias,
    est_fptp_seats,
    calc_efficiency_gap,
    calc_partisan_metrics,
)
from rdapy.partisan import key_RV_points


class TestPartisanMetrics:
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
        assert Rb < 0.50
        assert Ra > 0.50

        s: dict = calc_partisan_metrics(profile["statewide"], profile["byDistrict"])

        assert s["bias"]["bestS"] == 31
        assert approx_equal(s["bias"]["bestSf"], 0.5849, places=4)
        assert approx_equal(s["bias"]["estS"], 38.652689, places=4)
        assert approx_equal(s["bias"]["estSf"], 0.7293, places=4)
        assert approx_equal(s["bias"]["deviation"], -0.1444, places=4)
        assert approx_equal(s["bias"]["tOf"], -0.006566, places=4)
        assert approx_equal(s["bias"]["bS50"], -0.01792670, places=4)
        assert approx_equal(s["bias"]["bV50"], -0.00609430, places=4)
        assert approx_equal(s["bias"]["bSV"], 0.0330327, places=4)
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
        assert Rb < 0.50
        assert Ra > 0.50

        s: dict = calc_partisan_metrics(profile["statewide"], profile["byDistrict"])

        assert s["bias"]["bestS"] == 4
        assert approx_equal(s["bias"]["bestSf"], 0.5714, places=4)
        assert approx_equal(s["bias"]["estS"], 3.553689, places=4)
        assert approx_equal(s["bias"]["estSf"], 0.5077, places=4)
        assert approx_equal(s["bias"]["deviation"], 0.0638, places=4)
        assert approx_equal(s["bias"]["tOf"], 0.002829, places=4)
        assert approx_equal(s["bias"]["bS50"], 0.01355483, places=4)
        assert approx_equal(s["bias"]["bV50"], 0.00354176, places=4)
        assert approx_equal(s["bias"]["bSV"], 0.0137603, places=4)
        assert approx_equal(s["bias"]["gamma"], 1.35 / 100, places=4)
        assert approx_equal(s["bias"]["eG"], 0.00345216, places=4)
        assert approx_equal(s["bias"]["mMs"], 0.0135999999999999, places=4)
        assert approx_equal(s["bias"]["mMd"], 0.010771, places=4)
        assert approx_equal(s["bias"]["lO"], 0.313178142621696 / 100, places=4)
        assert approx_equal(s["responsiveness"]["littleR"], 3.801580, places=4)
        assert approx_equal(s["responsiveness"]["rD"], 2.487388, places=4)
        assert approx_equal(s["responsiveness"]["rDf"], 0.3553, places=4)

    def test_IL_2012(self) -> None:
        """IL 2012 from research project #2 w/ John Nagle."""

        profile_path: str = "testdata/partisan/nagle/partisan-IL-2012.json"
        profile: dict = read_json(profile_path)

        points: dict = key_RV_points(profile["byDistrict"])
        Sb: float = points["Sb"]
        Ra: float = points["Ra"]
        Rb: float = points["Rb"]
        Va: float = points["Va"]
        Vb: float = points["Vb"]

        assert Va >= 0.50
        assert Vb <= 0.50
        assert Rb < 0.50
        assert Ra > 0.50

        s: dict = calc_partisan_metrics(profile["statewide"], profile["byDistrict"])

        assert s["bias"]["bestS"] == 11
        assert approx_equal(s["bias"]["bestSf"], 0.6111, places=4)
        assert approx_equal(s["bias"]["estS"], 13.436476, places=4)
        assert approx_equal(s["bias"]["estSf"], 0.7465, places=4)
        assert approx_equal(s["bias"]["deviation"], -0.1354, places=4)
        assert approx_equal(s["bias"]["tOf"], -0.005924, places=4)
        assert approx_equal(s["bias"]["bS50"], 0.06529380, places=4)
        assert approx_equal(s["bias"]["bV50"], 0.01767461, places=4)
        assert approx_equal(s["bias"]["bSV"], 0.0250521, places=4)
        assert approx_equal(s["bias"]["gamma"], 6.87 / 100, places=4)
        assert approx_equal(s["bias"]["eG"], -0.04633487, places=4)
        assert approx_equal(s["bias"]["mMs"], 0.0216675, places=3)
        assert approx_equal(s["bias"]["mMd"], 0.027568, places=3)
        assert approx_equal(s["bias"]["lO"], 11.6630707932444 / 100, places=4)
        assert approx_equal(s["responsiveness"]["littleR"], 3.149669, places=4)
        assert approx_equal(s["responsiveness"]["rD"], 3.846940, places=4)
        assert approx_equal(s["responsiveness"]["rDf"], 0.2137, places=4)

    def test_MA_2012(self) -> None:
        """MA 2012 from research project #2 w/ John Nagle."""

        profile_path: str = "testdata/partisan/nagle/partisan-MA-2012.json"
        profile: dict = read_json(profile_path)

        s: dict = calc_partisan_metrics(profile["statewide"], profile["byDistrict"])

        # NOTE - Declination is undefined

        assert s["bias"]["bestS"] == 5
        assert approx_equal(s["bias"]["bestSf"], 0.5556, places=4)
        assert approx_equal(s["bias"]["estS"], 8.622034, places=4)
        assert approx_equal(s["bias"]["estSf"], 0.9580, places=4)
        assert approx_equal(s["bias"]["deviation"], -0.4024, places=4)
        assert approx_equal(s["bias"]["tOf"], -0.007300, places=4)
        assert approx_equal(s["bias"]["bS50"], 0.06718376, places=4)
        assert approx_equal(s["bias"]["bV50"], 0.01002969, places=4)
        assert approx_equal(s["bias"]["bSV"], -0.0303917, places=4)
        assert approx_equal(s["bias"]["gamma"], -26.02 / 100, places=4)
        assert approx_equal(s["bias"]["eG"], -0.25746580, places=4)
        assert approx_equal(s["bias"]["mMs"], 0.0230850624999998, places=4)
        assert approx_equal(s["bias"]["mMd"], 0.027185, places=2)
        # Lopsided outcomes are undefined
        assert approx_equal(s["responsiveness"]["littleR"], 1.972364, places=4)
        assert approx_equal(s["responsiveness"]["rD"], 1.383189, places=4)
        assert approx_equal(s["responsiveness"]["rDf"], 0.1537, places=4)

    def test_MD_2012(self) -> None:
        """MD 2012 from research project #2 w/ John Nagle"""

        profile_path: str = "testdata/partisan/nagle/partisan-MD-2012.json"
        profile: dict = read_json(profile_path)

        points: dict = key_RV_points(profile["byDistrict"])
        Sb: float = points["Sb"]
        Ra: float = points["Ra"]
        Rb: float = points["Rb"]
        Va: float = points["Va"]
        Vb: float = points["Vb"]

        assert Va >= 0.50
        assert Vb <= 0.50
        assert Rb < 0.50
        assert Ra > 0.50

        s: dict = calc_partisan_metrics(profile["statewide"], profile["byDistrict"])

        assert s["bias"]["bestS"] == 5
        assert approx_equal(s["bias"]["bestSf"], 0.6250, places=4)
        assert approx_equal(s["bias"]["estS"], 6.796640, places=4)
        assert approx_equal(s["bias"]["estSf"], 0.8496, places=4)
        assert approx_equal(s["bias"]["deviation"], -0.2246, places=4)
        assert approx_equal(s["bias"]["tOf"], -0.004063, places=4)
        assert approx_equal(s["bias"]["bS50"], -0.05453999, places=4)
        assert approx_equal(s["bias"]["bV50"], -0.01007575, places=4)
        assert approx_equal(s["bias"]["bSV"], 0.0137802, places=4)
        assert approx_equal(s["bias"]["gamma"], -24.9 / 100, places=4)
        assert approx_equal(s["bias"]["eG"], -0.16284202, places=4)
        assert approx_equal(s["bias"]["mMs"], -0.0109, places=4)
        assert approx_equal(s["bias"]["mMd"], -0.006817, places=4)
        assert approx_equal(s["bias"]["lO"], 4.05629795619783 / 100, places=4)
        assert approx_equal(s["responsiveness"]["littleR"], 1.076736, places=4)
        assert approx_equal(s["responsiveness"]["rD"], 0.702811, places=4)
        assert approx_equal(s["responsiveness"]["rDf"], 0.0879, places=4)

    def test_NC_2012(self) -> None:
        """NC 2012 from research project #2 w/ John Nagle"""

        profile_path: str = "testdata/partisan/nagle/partisan-NC-2012.json"
        profile: dict = read_json(profile_path)

        points: dict = key_RV_points(profile["byDistrict"])
        Sb: float = points["Sb"]
        Ra: float = points["Ra"]
        Rb: float = points["Rb"]
        Va: float = points["Va"]
        Vb: float = points["Vb"]

        assert Va >= 0.50
        assert Vb <= 0.50
        assert Rb < 0.50
        assert Ra > 0.50

        s: dict = calc_partisan_metrics(profile["statewide"], profile["byDistrict"])

        assert s["bias"]["bestS"] == 7
        assert approx_equal(s["bias"]["bestSf"], 0.5385, places=4)
        assert approx_equal(s["bias"]["estS"], 4.192437, places=4)
        assert approx_equal(s["bias"]["estSf"], 0.3225, places=4)
        assert approx_equal(s["bias"]["deviation"], 0.2160, places=4)
        assert approx_equal(s["bias"]["tOf"], -0.002295, places=4)
        assert approx_equal(s["bias"]["bS50"], 0.21716415, places=4)
        assert approx_equal(s["bias"]["bV50"], 0.04501325, places=4)
        assert approx_equal(s["bias"]["bSV"], 0.209849, places=4)
        assert approx_equal(s["bias"]["decl"], 36.51, places=1)
        assert approx_equal(s["bias"]["gamma"], 24.29 / 100, places=4)
        assert approx_equal(s["bias"]["eG"], 0.20757683, places=4)
        assert approx_equal(s["bias"]["mMs"], 0.0570306, places=4)
        assert approx_equal(s["bias"]["mMd"], 0.054731, places=2)
        assert approx_equal(s["bias"]["lO"], 11.0640578002419 / 100, places=4)
        assert approx_equal(s["responsiveness"]["littleR"], 4.350382, places=4)
        assert approx_equal(s["responsiveness"]["rD"], 4.020386, places=4)
        assert approx_equal(s["responsiveness"]["rDf"], 0.3093, places=4)

    def test_OH_2012(self) -> None:
        """OH 2012 from research project #2 w/ John Nagle"""

        profile_path: str = "testdata/partisan/nagle/partisan-OH-2012.json"
        profile: dict = read_json(profile_path)

        points: dict = key_RV_points(profile["byDistrict"])
        Sb: float = points["Sb"]
        Ra: float = points["Ra"]
        Rb: float = points["Rb"]
        Va: float = points["Va"]
        Vb: float = points["Vb"]

        assert Va >= 0.50
        assert Vb <= 0.50
        assert Rb < 0.50
        assert Ra > 0.50

        s: dict = calc_partisan_metrics(profile["statewide"], profile["byDistrict"])

        assert s["bias"]["bestS"] == 8
        assert approx_equal(s["bias"]["bestSf"], 0.5000, places=4)
        assert approx_equal(s["bias"]["estS"], 6.237092, places=4)
        assert approx_equal(s["bias"]["estSf"], 0.3898, places=4)
        assert approx_equal(s["bias"]["deviation"], 0.1102, places=4)
        assert approx_equal(s["bias"]["tOf"], -0.003045, places=4)
        assert approx_equal(s["bias"]["bS50"], 0.15497649, places=4)
        assert approx_equal(s["bias"]["bV50"], 0.03334768, places=4)
        assert approx_equal(s["bias"]["bSV"], 0.149474, places=4)
        assert approx_equal(s["bias"]["gamma"], 16.34 / 100, places=4)
        assert approx_equal(s["bias"]["eG"], 0.13630573, places=4)
        assert approx_equal(s["bias"]["mMs"], 0.0416622777777778, places=4)
        assert approx_equal(s["bias"]["mMd"], 0.043962, places=2)
        assert approx_equal(s["bias"]["lO"], 6.93912595785785 / 100, places=4)
        assert approx_equal(s["responsiveness"]["littleR"], 4.076508, places=4)
        assert approx_equal(s["responsiveness"]["rD"], 6.073901, places=4)
        assert approx_equal(s["responsiveness"]["rDf"], 0.3796, places=4)

    def test_PA_2012(self) -> None:
        """PA 2012 from research project #2 w/ John Nagle"""

        profile_path: str = "testdata/partisan/nagle/partisan-PA-2012.json"
        profile: dict = read_json(profile_path)

        points: dict = key_RV_points(profile["byDistrict"])
        Sb: float = points["Sb"]
        Ra: float = points["Ra"]
        Rb: float = points["Rb"]
        Va: float = points["Va"]
        Vb: float = points["Vb"]

        assert Va >= 0.50
        assert Vb <= 0.50
        assert Rb < 0.50
        assert Ra > 0.50

        s: dict = calc_partisan_metrics(profile["statewide"], profile["byDistrict"])

        assert s["bias"]["bestS"] == 10
        assert approx_equal(s["bias"]["bestSf"], 0.5556, places=4)
        assert approx_equal(s["bias"]["estS"], 7.500995, places=4)
        assert approx_equal(s["bias"]["estSf"], 0.4167, places=4)
        assert approx_equal(s["bias"]["deviation"], 0.1388, places=4)
        assert approx_equal(s["bias"]["tOf"], 0.002316, places=4)
        assert approx_equal(s["bias"]["bS50"], 0.16923261, places=4)
        assert approx_equal(s["bias"]["bV50"], 0.04711839, places=4)
        assert approx_equal(s["bias"]["bSV"], 0.155534, places=4)
        assert approx_equal(s["bias"]["gamma"], 18.35 / 100, places=4)
        assert approx_equal(s["bias"]["eG"], 0.14212207, places=4)
        assert approx_equal(s["bias"]["mMs"], 0.0574219090909092, places=4)
        assert approx_equal(s["bias"]["mMd"], 0.055106, places=4)
        assert approx_equal(s["bias"]["lO"], 8.73772850436113 / 100, places=4)
        assert approx_equal(s["responsiveness"]["littleR"], 3.407693, places=4)
        assert approx_equal(s["responsiveness"]["rD"], 6.077222, places=4)
        assert approx_equal(s["responsiveness"]["rDf"], 0.3376, places=4)

    def test_SC_2012(self) -> None:
        """SC 2012 from research project #2 w/ John Nagle"""

        profile_path: str = "testdata/partisan/nagle/partisan-SC-2012.json"
        profile: dict = read_json(profile_path)

        points: dict = key_RV_points(profile["byDistrict"])
        Sb: float = points["Sb"]
        Ra: float = points["Ra"]
        Rb: float = points["Rb"]
        Va: float = points["Va"]
        Vb: float = points["Vb"]

        assert Va >= 0.50
        assert Vb <= 0.50
        assert Rb < 0.50
        assert Ra > 0.50

        s: dict = calc_partisan_metrics(profile["statewide"], profile["byDistrict"])

        assert s["bias"]["bestS"] == 3
        assert approx_equal(s["bias"]["bestSf"], 0.4286, places=4)
        assert approx_equal(s["bias"]["estS"], 1.108305, places=4)
        assert approx_equal(s["bias"]["estSf"], 0.1583, places=4)
        assert approx_equal(s["bias"]["deviation"], 0.2702, places=4)
        assert approx_equal(s["bias"]["tOf"], -0.001194, places=4)
        assert approx_equal(s["bias"]["bS50"], 0.15016984, places=4)
        assert approx_equal(s["bias"]["bV50"], 0.02378688, places=4)
        assert approx_equal(s["bias"]["bSV"], 0.00651749, places=4)
        assert approx_equal(s["bias"]["gamma"], 28.08 / 100, places=4)
        assert approx_equal(s["bias"]["eG"], 0.20172665, places=4)
        assert approx_equal(s["bias"]["mMs"], 0.0472668571428571, places=4)
        assert approx_equal(s["bias"]["mMd"], 0.048467, places=4)
        assert approx_equal(s["bias"]["lO"], 4.24207200633289 / 100, places=4)
        assert approx_equal(s["responsiveness"]["littleR"], 0.869641, places=4)
        assert approx_equal(s["responsiveness"]["rD"], 0.407811, places=4)
        assert approx_equal(s["responsiveness"]["rDf"], 0.0583, places=4)

    def test_TN_2012(self) -> None:
        """TN 2012 from research project #2 w/ John Nagle"""

        profile_path: str = "testdata/partisan/nagle/partisan-TN-2012.json"
        profile: dict = read_json(profile_path)

        points: dict = key_RV_points(profile["byDistrict"])
        Sb: float = points["Sb"]
        Ra: float = points["Ra"]
        Rb: float = points["Rb"]
        Va: float = points["Va"]
        Vb: float = points["Vb"]

        assert Va >= 0.50
        assert Vb <= 0.50
        assert Rb < 0.50
        assert Ra > 0.50

        s: dict = calc_partisan_metrics(profile["statewide"], profile["byDistrict"])

        assert s["bias"]["bestS"] == 4
        assert approx_equal(s["bias"]["bestSf"], 0.4444, places=4)
        assert approx_equal(s["bias"]["estS"], 1.896111, places=4)
        assert approx_equal(s["bias"]["estSf"], 0.2107, places=4)
        assert approx_equal(s["bias"]["deviation"], 0.2338, places=4)
        assert approx_equal(s["bias"]["tOf"], -0.002074, places=4)
        assert approx_equal(s["bias"]["bS50"], 0.18353175, places=4)
        assert approx_equal(s["bias"]["bV50"], 0.03247332, places=4)
        assert approx_equal(s["bias"]["bSV"], -0.0320523, places=4)
        assert approx_equal(s["bias"]["decl"], 34.85449, places=1)
        assert approx_equal(s["bias"]["gamma"], 24.96 / 100, places=4)
        assert approx_equal(s["bias"]["eG"], 0.12119106, places=4)
        assert approx_equal(s["bias"]["mMs"], 0.0413316666666666, places=4)
        assert approx_equal(s["bias"]["mMd"], 0.043432, places=4)
        assert approx_equal(s["bias"]["lO"], 0.59256529415822 / 100, places=4)
        assert approx_equal(s["responsiveness"]["littleR"], 0.472979, places=4)
        assert approx_equal(s["responsiveness"]["rD"], 0.396007, places=4)
        assert approx_equal(s["responsiveness"]["rDf"], 0.0440, places=4)

    def test_TX_2012(self) -> None:
        """TX 2012 from research project #2 w/ John Nagle"""

        profile_path: str = "testdata/partisan/nagle/partisan-TX-2012.json"
        profile: dict = read_json(profile_path)

        points: dict = key_RV_points(profile["byDistrict"])
        Sb: float = points["Sb"]
        Ra: float = points["Ra"]
        Rb: float = points["Rb"]
        Va: float = points["Va"]
        Vb: float = points["Vb"]

        assert Va >= 0.50
        assert Vb <= 0.50
        assert Rb < 0.50
        assert Ra > 0.50

        s: dict = calc_partisan_metrics(profile["statewide"], profile["byDistrict"])

        assert s["bias"]["bestS"] == 15
        assert approx_equal(s["bias"]["bestSf"], 0.4167, places=4)
        assert approx_equal(s["bias"]["estS"], 10.417401, places=4)
        assert approx_equal(s["bias"]["estSf"], 0.2894, places=4)
        assert approx_equal(s["bias"]["deviation"], 0.1273, places=4)
        assert approx_equal(s["bias"]["tOf"], -0.022282, places=4)
        assert approx_equal(s["bias"]["bS50"], 0.05457906, places=4)
        assert approx_equal(s["bias"]["bV50"], 0.01354120, places=4)
        assert approx_equal(s["bias"]["bSV"], -0.0833849, places=4)
        assert approx_equal(s["bias"]["gamma"], 9.87 / 100, places=4)
        assert approx_equal(s["bias"]["eG"], 0.01927575, places=4)
        assert approx_equal(s["bias"]["mMs"], 0.0213738333333333, places=4)
        assert approx_equal(s["bias"]["mMd"], 0.043674, places=4)
        assert approx_equal(s["bias"]["lO"], -2.95999047419546 / 100, places=4)
        assert approx_equal(s["responsiveness"]["littleR"], 1.169951, places=4)
        assert approx_equal(s["responsiveness"]["rD"], 2.805144, places=4)
        assert approx_equal(s["responsiveness"]["rDf"], 0.0779, places=4)

    def test_CO_most_competitive(self) -> None:
        """This map is so extreme that it broke the declination calculations"""

        profile_path: str = "testdata/partisan/issues/profile-CO-competitive.json"
        profile: dict = read_json(profile_path)

        points: dict = key_RV_points(profile["partisanship"]["byDistrict"])
        Sb: float = points["Sb"]
        Ra: float = points["Ra"]
        Rb: float = points["Rb"]
        Va: float = points["Va"]
        Vb: float = points["Vb"]

        assert Va >= 0.50
        assert Vb <= 0.50
        assert Rb < 0.50
        assert Ra > 0.50


### END ###
