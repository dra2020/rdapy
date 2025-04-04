#!/usr/bin/env python3

"""
TEST NORMALIZATION & RATINGS
"""

import random

from rdapy.rate import *
from rdapy.utils import *
from testutils import *

EPSILON: float = 1 / 10**6


class TestNormalizer:
    """Test Normalizer class"""

    def test_identity(self) -> None:
        x: float = random.random()
        n: Normalizer = Normalizer(x)
        n.identity()
        assert approx_equal(n.wip_num, x)

    def test_invert(self) -> None:
        n: Normalizer = Normalizer(0.75 / 100)
        n.invert()
        assert approx_equal(n.wip_num, 0.9925)

        n: Normalizer = Normalizer(0.0)
        n.invert()
        assert approx_equal(n.wip_num, 1.0)

        n: Normalizer = Normalizer(1.0)
        n.invert()
        assert approx_equal(n.wip_num, 0.0)

    def test_clip(self) -> None:
        n: Normalizer = Normalizer(0.3773)
        n.clip(0.25, 0.50)
        assert approx_equal(n.wip_num, 0.3773)

        n: Normalizer = Normalizer(0.2)
        n.clip(0.25, 0.50)
        assert approx_equal(n.wip_num, 0.25)

        n: Normalizer = Normalizer(0.55)
        n.clip(0.25, 0.50)
        assert approx_equal(n.wip_num, 0.5)

        n: Normalizer = Normalizer(0.25)
        n.clip(0.25, 0.50)
        assert approx_equal(n.wip_num, 0.25)

        n: Normalizer = Normalizer(0.5)
        n.clip(0.25, 0.50)
        assert approx_equal(n.wip_num, 0.5)

    def test_rebase(self) -> None:
        n: Normalizer = Normalizer(1.0)
        n.rebase(1.0)
        assert approx_equal(n.wip_num, 0.0)

        n: Normalizer = Normalizer(1.5)
        n.rebase(1.0)
        assert approx_equal(n.wip_num, 0.5)

        n: Normalizer = Normalizer(0.5)
        n.rebase(1.0)
        assert approx_equal(n.wip_num, -0.5)

        n: Normalizer = Normalizer(-2.0)
        n.rebase(1.0)
        assert approx_equal(n.wip_num, -3.0)

    def test_unitize(self) -> None:
        n: Normalizer = Normalizer(1.5)
        n.unitize(1.0, 2.0)
        assert approx_equal(n.wip_num, 0.5)

        n: Normalizer = Normalizer(1.0)
        n.unitize(1.0, 2.0)
        assert approx_equal(n.wip_num, 0.0)

        n: Normalizer = Normalizer(2.0)
        n.unitize(1.0, 2.0)
        assert approx_equal(n.wip_num, 1.0)

    def test_decay(self) -> None:
        n: Normalizer = Normalizer(0.90)
        n.decay()
        assert approx_equal(n.wip_num, 0.81)

        n: Normalizer = Normalizer(0.00)
        n.decay()
        assert approx_equal(n.wip_num, 0.0)

        n: Normalizer = Normalizer(1.00)
        n.decay()
        assert approx_equal(n.wip_num, 1.00)

    def test_rescale(self) -> None:
        n: Normalizer = Normalizer(0.63)
        n.rescale()
        assert n.normalized_num == 63

        n: Normalizer = Normalizer(0.6372)
        n.rescale()
        assert n.normalized_num == 64

        n: Normalizer = Normalizer(0.6312)
        n.rescale()
        assert n.normalized_num == 63

        n: Normalizer = Normalizer(0.0)
        n.rescale()
        assert n.normalized_num == 0

        n: Normalizer = Normalizer(1.0)
        n.rescale()
        assert n.normalized_num == 100


class TestRatings:
    def test_is_antimajoritarian(self) -> None:
        # Dem antimajoritarian
        assert is_antimajoritarian(0.5 - AVG_SV_ERROR - EPSILON, 0.50 + EPSILON)

        # Rep antimajoritarian
        assert is_antimajoritarian(0.5 + AVG_SV_ERROR + EPSILON, 0.5 - EPSILON)

        # Majority but not antimajoritarian
        assert not is_antimajoritarian(0.51, 0.53)

        # Minority but not antimajoritarian
        assert not is_antimajoritarian(0.49, 0.47)

        # Not big enough to be called antimajoritarian
        assert not is_antimajoritarian(0.5 - EPSILON, 0.5 - EPSILON)

    def test_extra_bonus(self) -> None:
        assert approx_equal(extra_bonus(0.50), 0.0)
        assert approx_equal(extra_bonus(0.55), 0.10 / 2)
        assert approx_equal(extra_bonus(0.60), 0.20 / 2)
        assert approx_equal(extra_bonus(0.45), 0.10 / 2)
        assert approx_equal(extra_bonus(0.40), 0.20 / 2)

    def test_adjust_deviation(self) -> None:
        # CA
        Vf: float = 0.64037
        bias: float = -0.1714
        extra: float = extra_bonus(Vf)
        assert approx_equal(extra, 0.1404, 4)
        assert approx_equal(adjust_deviation(Vf, bias, extra), -0.0310, 4)

        # NC
        Vf: float = 0.488799
        bias: float = 0.2268
        extra = extra_bonus(Vf)
        assert approx_equal(extra, 0.0112, 4)
        assert approx_equal(adjust_deviation(Vf, bias, extra), 0.2156, 4)

        # OH
        Vf: float = 0.486929
        bias: float = 0.2367
        extra = extra_bonus(Vf)
        assert approx_equal(extra, 0.0131, 4)
        assert approx_equal(adjust_deviation(Vf, bias, extra), 0.2236, 4)

        # PA
        Vf: float = 0.51148
        bias: float = 0.0397
        extra = extra_bonus(Vf)
        assert approx_equal(extra, 0.0115, 4)
        assert approx_equal(adjust_deviation(Vf, bias, extra), bias, 4)

        # TX
        Vf: float = 0.436994
        bias: float = 0.1216
        extra = extra_bonus(Vf)
        assert approx_equal(extra, 0.0630, 4)
        assert approx_equal(adjust_deviation(Vf, bias, extra), 0.0586, 4)

    def test_rate_proportionality(self) -> None:
        # Score proportionality, no winner bonus

        Vf = 0.5
        Sf = 0.5

        assert rate_proportionality(0.00, Vf, Sf) == 100  # Completely unbiased
        assert rate_proportionality(0.05, Vf, Sf) == 75  # 5% biased
        assert rate_proportionality(0.10, Vf, Sf) == 50  # 10% biased
        assert rate_proportionality(0.20, Vf, Sf) == 0  # 20% biased
        assert rate_proportionality(0.25, Vf, Sf) == 0  # 25% biased
        assert (
            rate_proportionality(0.01, 0.48 - EPSILON, 0.5 + EPSILON) == 0
        )  # Dem antimajoritarian
        assert (
            rate_proportionality(0.01, 1 - 0.48 + EPSILON, 1 - 0.5 - EPSILON) == 0
        )  # Rep antimajoritarian

        # Score proportionality, with winner bonus

        assert rate_proportionality(-0.1714, 0.6404, 43.0850 / 53) == 84  # CA 116th
        assert rate_proportionality(0.0006, 0.5286, 3.9959 / 7) == 100  # CO 116th
        assert rate_proportionality(-0.0585, 0.5838, 12.0531 / 18) == 100  # IL 116th
        assert rate_proportionality(-0.3331, 0.6321, 8.9985 / 9) == 0  # MA 116th
        assert rate_proportionality(-0.2500, 0.6336, 7.0000 / 8) == 42  # MD 116th
        assert rate_proportionality(0.2268, 0.4888, 3.0512 / 13) == 0  # NC 116th
        assert rate_proportionality(0.2367, 0.4869, 4.2120 / 16) == 0  # OH 116th
        assert rate_proportionality(0.2857, 0.4072, 1 / 7) == 4  # SC 116th
        assert rate_proportionality(0.1111, 0.3802, 2 / 9) == 100  # TN 116th
        assert rate_proportionality(0.1216, 0.4370, 11.6218 / 36) == 71  # TX 116th

    def test_rate_competitiveness(self) -> None:
        # Completely uncompetitive
        assert rate_competitiveness(0.00) == 0
        # 25% / 50% competitive
        assert rate_competitiveness(0.25) == 33
        # 50% / 50% competitive
        assert rate_competitiveness(0.50) == 67
        # Perfectly competitive
        assert rate_competitiveness(0.75) == 100
        # Over competitive
        assert rate_competitiveness(0.80) == 100

    def test_rate_minority_opportunity(self) -> None:
        bonus: int = 100

        # No possibilities
        assert rate_minority_opportunity(1, 0, 0, 0) == 0

        # No opportunities
        assert rate_minority_opportunity(0, 10, 0, 0) == 0

        # Half
        assert rate_minority_opportunity(5, 10, 0, 0) == round(bonus / 2)

        # All
        assert rate_minority_opportunity(10, 10, 0, 0) == bonus

        # Extra
        assert rate_minority_opportunity(11, 10, 0, 0) == bonus

        # Combined score

        # * Opportunity districts = (12.56 / 18) * 100 <<< 70
        # * Coalition districts = (22.92 / 18) * 100 <<< capped
        # * Combined = 70 + [0.5 * (100 - 70)]
        correct: int = 85
        assert rate_minority_opportunity(12.56, 18, 22.92, 18) == correct

    def test_rate_compactness(self) -> None:
        assert rate_compactness(30, 60) == 45

        # Reock compactness scorer
        # Reock: in range (AL)
        assert rate_reock(0.3848) == 54

        # Reock: in range (NC)
        assert rate_reock(0.3373) == 35

        # Reock: min
        assert rate_reock(REOCK_MIN) == 0

        # Reock: max
        assert rate_reock(REOCK_MAX) == 100

        # Reock: too low
        assert rate_reock(REOCK_MIN - EPSILON) == 0

        # Reock: too high
        assert rate_reock(REOCK_MAX + EPSILON) == 100

        # Polsby-Popper compactness scorer

        # Polsby-Popper: in range (AL)
        assert rate_polsby(0.1860) == 21

        # Polsby-Popper: in range (NC)
        assert rate_polsby(0.2418) == 35

        # Polsby-Popper: min
        assert rate_polsby(POLSBY_MIN) == 0

        # Polsby-Popper: max
        assert rate_polsby(POLSBY_MAX) == 100

        # Polsby-Popper: too low
        assert rate_polsby(POLSBY_MIN - EPSILON) == 0

        # Polsby-Popper: too high
        assert rate_polsby(POLSBY_MAX + EPSILON) == 100

    def test_rate_splitting(self) -> None:
        # Combine splitting ratings

        # Some county- & district splitting
        assert abs(rate_splitting(30, 60) - 45) <= 1

        # Little county- & district- splitting
        assert rate_splitting(99, 100) == 99

        # No county- & district- splitting
        assert rate_splitting(100, 100) == 100

        # Rate state splitting

        # XX	C	CD	C_DC'	C_CD'	UD	U_DC'	U_CD'	LD	L_DC'	L_CD'	C_CT	C_DT	C_RC	C_RD	C_R'	U_CT	U_DT	U_RC	U_RD	U_R'	L_CT	L_DT	L_RC	L_RD	L_R'
        # AL	67	7	1.1100	1.4470	35	1.4200	1.4500	105	1.6400	1.2600	1.02	1.20	73	38	56	1.10	1.20	13	38	26	1.20	1.13	0	64	32
        # AZ	15	9	1.3520	1.4240	30	1.7100	1.2000				1.11	1.20	33	44	39	1.20	1.09	0	71	36
        # CA	58	53	1.7890	1.2530	40	1.7400	1.3400	80	1.7000	1.1900	1.18	1.20	0	87	44	1.13	1.20	0	65	33	1.20	1.14	0	88	44
        # CO	64	7	1.1960	1.5010	35	1.2100	1.0800	65	1.2500	1.0700	1.02	1.20	48	25	37	1.11	1.20	72	100	86	1.20	1.19	88	100	94
        # CT	8	5	1.4800	1.5310	36	2.0800	1.1700	151	1.6800	1.0500	1.10	1.20	0	17	9	1.20	1.04	0	62	31	1.20	1.01	0	88	44
        # GA	159	14	1.2960	1.6400	56	1.5800	1.3900	180	1.7800	1.2700	1.02	1.20	17	0	9	1.07	1.20	0	53	27	1.20	1.18	0	76	38
        # IA	99	4	1.0000	1.0000	50	1.3300	1.2900	100	1.2600	1.2000	1.01	1.20	100	100	100	1.10	1.20	37	78	58	1.20	1.20	85	99	92
        # KY	120	6	1.0360	1.2230	38	1.2100	1.0800	100	1.4300	1.2000	1.01	1.20	92	94	93	1.06	1.20	58	100	79	1.17	1.20	32	100	66
        # PA	67	18	1.1780	1.4080	50	1.5200	1.3000	203	1.6500	1.1300	1.05	1.20	64	48	56	1.15	1.20	2	75	39	1.20	1.07	0	82	41
        # TN	95	9	1.0710	1.2670	33	1.1400	1.1000	99	1.1000	1.1400	1.02	1.20	84	83	84	1.07	1.20	80	100	90	1.20	1.19	100	100	100
        # TX	254	36	1.5790	1.4280	31	1.4600	1.3300	150	1.0800	1.0400	1.03	1.20	0	43	22	1.02	1.20	0	68	34	1.12	1.20	100	100	100
        # VA	133	11	1.2140	1.6900	40	1.6400	1.7000	100	1.8400	1.4200	1.02	1.20	41	0	21	1.06	1.20	0	0	0	1.15	1.20	0	45	23

        # With 2 minor exceptions, the test cases below are the subset above from the Excel spreadsheet I used to develop the ratings:
        # - There are some minor rounding differences between Excel & Typescript and
        # - The full Typescript implementation limits the max rating to 99 if there's any splitting. Only no splitting can get 100.

        # AL splitting

        nC: int = 67
        nCD: int = 7
        nUD: int = 35
        nLD: int = 105

        assert approx_equal(best_target(nC, nCD), 1.02, 2)
        assert approx_equal(best_target(nC, nUD), 1.10, 2)
        assert approx_equal(best_target(nC, nLD), 1.13, 2)

        assert rate_county_splitting(1.1100, nC, nCD) == 73
        assert rate_district_splitting(1.4470, nC, nCD) == 38
        assert abs(rate_splitting(73, 38) - 56) <= 1

        assert rate_county_splitting(1.4200, nC, nUD) == 12
        assert rate_district_splitting(1.4500, nC, nUD) == 37
        assert abs(rate_splitting(12, 37) - 25) <= 1

        assert rate_county_splitting(1.6400, nC, nLD) == 0
        assert rate_district_splitting(1.2600, nC, nLD) == 64
        assert abs(rate_splitting(0, 64) - 32) <= 1

        # AZ splitting

        nC: int = 15
        nCD: int = 9
        nUD: int = 30

        assert approx_equal(best_target(nC, nCD), 1.11, 2)
        assert approx_equal(best_target(nC, nUD), 1.09, 2)

        assert rate_county_splitting(1.3520, nC, nCD) == 33
        assert rate_district_splitting(1.4240, nC, nCD) == 43
        assert abs(rate_splitting(33, 43) - 38) <= 1

        assert rate_county_splitting(1.7100, nC, nUD) == 0
        assert rate_district_splitting(1.2000, nC, nUD) == 70
        assert abs(rate_splitting(0, 70) - 35) <= 1

        # CA splitting

        nC: int = 58
        nCD: int = 53
        nUD: int = 40
        nLD: int = 80

        assert approx_equal(best_target(nC, nCD), 1.18, 2)
        assert approx_equal(best_target(nC, nUD), 1.13, 2)
        assert approx_equal(best_target(nC, nLD), 1.14, 2)

        assert rate_county_splitting(1.7890, nC, nCD) == 0
        assert rate_district_splitting(1.2530, nC, nCD) == 87
        assert abs(rate_splitting(0, 65) - 33) <= 1

        assert rate_county_splitting(1.7400, nC, nUD) == 0
        assert rate_district_splitting(1.3400, nC, nUD) == 65
        assert abs(rate_splitting(0, 81) - 41) <= 1

        assert rate_county_splitting(1.7000, nC, nLD) == 0
        assert rate_district_splitting(1.1900, nC, nLD) == 87
        assert abs(rate_splitting(0, 87) - 44) <= 1

        # CO splitting

        nC: int = 64
        nCD: int = 7
        nUD: int = 35
        nLD: int = 65

        assert approx_equal(best_target(nC, nCD), 1.02, 2)
        assert approx_equal(best_target(nC, nUD), 1.11, 2)
        assert approx_equal(best_target(nC, nLD), 1.19, 2)

        assert rate_county_splitting(1.1960, nC, nCD) == 47
        assert rate_district_splitting(1.5010, nC, nCD) == 24
        assert abs(rate_splitting(47, 24) - 36) <= 1

        assert rate_county_splitting(1.2100, nC, nUD) == 72
        assert rate_district_splitting(1.0800, nC, nUD) == 99
        assert abs(rate_splitting(72, 99) - 86) <= 1

        assert rate_county_splitting(1.2500, nC, nLD) == 87
        assert rate_district_splitting(1.0700, nC, nLD) == 99
        assert abs(rate_splitting(87, 99) - 93) <= 1

        # CT splitting

        nC: int = 8
        nCD: int = 5
        nUD: int = 36
        nLD: int = 151

        assert approx_equal(best_target(nC, nCD), 1.10, 2)
        assert approx_equal(best_target(nC, nUD), 1.04, 2)
        assert approx_equal(best_target(nC, nLD), 1.01, 2)

        assert rate_county_splitting(1.4800, nC, nCD) == 0
        assert rate_district_splitting(1.5310, nC, nCD) == 16
        assert abs(rate_splitting(0, 16) - 8) <= 1

        assert rate_county_splitting(2.0800, nC, nUD) == 0
        assert rate_district_splitting(1.1700, nC, nUD) == 62
        assert abs(rate_splitting(0, 62) - 31) <= 1

        assert rate_county_splitting(1.6800, nC, nLD) == 0
        assert rate_district_splitting(1.0500, nC, nLD) == 88
        assert abs(rate_splitting(0, 88) - 44) <= 1

        # GA splitting

        nC: int = 159
        nCD: int = 14
        nUD: int = 56
        nLD: int = 180

        assert approx_equal(best_target(nC, nCD), 1.02, 2)
        assert approx_equal(best_target(nC, nUD), 1.07, 2)
        assert approx_equal(best_target(nC, nLD), 1.18, 2)

        assert rate_county_splitting(1.2960, nC, nCD) == 17
        assert rate_district_splitting(1.6400, nC, nCD) == 0
        assert abs(rate_splitting(0, 17) - 9) <= 1

        assert rate_county_splitting(1.5800, nC, nUD) == 0
        assert rate_district_splitting(1.3900, nC, nUD) == 52
        assert abs(rate_splitting(0, 52) - 26) <= 1

        assert rate_county_splitting(1.7800, nC, nLD) == 0
        assert rate_district_splitting(1.2700, nC, nLD) == 76
        assert abs(rate_splitting(0, 76) - 38) <= 1

        # IA splitting

        nC: int = 99
        nCD: int = 4
        nUD: int = 50
        nLD: int = 100

        assert approx_equal(best_target(nC, nCD), 1.01, 2)
        assert approx_equal(best_target(nC, nUD), 1.10, 2)
        assert approx_equal(best_target(nC, nLD), 1.20, 2)

        assert rate_county_splitting(1.0000, nC, nCD) == 100
        assert rate_district_splitting(1.0000, nC, nCD) == 100
        assert abs(rate_splitting(100, 100) - 100) <= 1

        assert rate_county_splitting(1.3300, nC, nUD) == 36
        assert rate_district_splitting(1.2900, nC, nUD) == 77
        assert abs(rate_splitting(36, 77) - 57) <= 1

        assert rate_county_splitting(1.2600, nC, nLD) == 85
        assert rate_district_splitting(1.2000, nC, nLD) == 99
        assert abs(rate_splitting(85, 99) - 92) <= 1

        # KY splitting

        nC: int = 120
        nCD: int = 6
        nUD: int = 38
        nLD: int = 100

        assert approx_equal(best_target(nC, nCD), 1.01, 2)
        assert approx_equal(best_target(nC, nUD), 1.06, 2)
        assert approx_equal(best_target(nC, nLD), 1.17, 2)

        assert rate_county_splitting(1.0360, nC, nCD) == 92
        assert rate_district_splitting(1.2230, nC, nCD) == 94
        assert abs(rate_splitting(92, 94) - 93) <= 1

        assert rate_county_splitting(1.2100, nC, nUD) == 58
        assert rate_district_splitting(1.0800, nC, nUD) == 99
        assert abs(rate_splitting(58, 99) - 79) <= 1

        assert rate_county_splitting(1.4300, nC, nLD) == 31
        assert rate_district_splitting(1.2000, nC, nLD) == 99
        assert abs(rate_splitting(31, 99) - 65) <= 1

        # PA splitting

        nC: int = 67
        nCD: int = 18
        nUD: int = 50
        nLD: int = 203

        assert approx_equal(best_target(nC, nCD), 1.05, 2)
        assert approx_equal(best_target(nC, nUD), 1.15, 2)
        assert approx_equal(best_target(nC, nLD), 1.07, 2)

        assert rate_county_splitting(1.1780, nC, nCD) == 63
        assert rate_district_splitting(1.4080, nC, nCD) == 47
        assert abs(rate_splitting(63, 47) - 55) <= 1

        assert rate_county_splitting(1.5200, nC, nUD) == 1
        assert rate_district_splitting(1.3000, nC, nUD) == 75
        assert abs(rate_splitting(1, 75) - 38) <= 1

        assert rate_county_splitting(1.6500, nC, nLD) == 0
        assert rate_district_splitting(1.1300, nC, nLD) == 82
        assert abs(rate_splitting(0, 82) - 41) <= 1

        # The is the user Ruth's PA Lower State House map.
        # The initial intended ratings "tanked" (85 => 53).
        # With these revised ratings, the drop is only half that much (85 => 70).
        assert rate_county_splitting(1.3100, nC, nLD) == 72
        assert rate_district_splitting(1.1800, nC, nLD) == 67
        assert abs(rate_splitting(72, 67) - 70) <= 1

        # TN splitting

        nC: int = 95
        nCD: int = 9
        nUD: int = 33
        nLD: int = 99

        assert approx_equal(best_target(nC, nCD), 1.02, 2)
        assert approx_equal(best_target(nC, nUD), 1.07, 2)
        assert approx_equal(best_target(nC, nLD), 1.19, 2)

        assert rate_county_splitting(1.0710, nC, nCD) == 84
        assert rate_district_splitting(1.2670, nC, nCD) == 83
        assert abs(rate_splitting(84, 83) - 84) <= 1

        assert rate_county_splitting(1.1400, nC, nUD) == 79
        assert rate_district_splitting(1.1000, nC, nUD) == 99
        assert abs(rate_splitting(79, 99) - 89) <= 1

        assert rate_county_splitting(1.1000, nC, nLD) == 99
        assert rate_district_splitting(1.1400, nC, nLD) == 99
        assert abs(rate_splitting(99, 99) - 99) <= 1

        # TX splitting

        nC: int = 254
        nCD: int = 36
        nUD: int = 31
        nLD: int = 150

        assert approx_equal(best_target(nC, nCD), 1.03, 2)
        assert approx_equal(best_target(nC, nUD), 1.02, 2)
        assert approx_equal(best_target(nC, nLD), 1.12, 2)

        assert rate_county_splitting(1.5790, nC, nCD) == 0
        assert rate_district_splitting(1.4280, nC, nCD) == 42
        assert abs(rate_splitting(0, 42) - 21) <= 1

        assert rate_county_splitting(1.4600, nC, nUD) == 0
        assert rate_district_splitting(1.3300, nC, nUD) == 67
        assert abs(rate_splitting(0, 67) - 34) <= 1

        assert rate_county_splitting(1.0800, nC, nLD) == 99
        assert rate_district_splitting(1.0400, nC, nLD) == 99
        assert abs(rate_splitting(99, 99) - 99) <= 1

        # VA splitting

        nC: int = 133
        nCD: int = 11
        nUD: int = 40
        nLD: int = 100

        assert approx_equal(best_target(nC, nCD), 1.02, 2)
        assert approx_equal(best_target(nC, nUD), 1.06, 2)
        assert approx_equal(best_target(nC, nLD), 1.15, 2)

        assert rate_county_splitting(1.2140, nC, nCD) == 41
        assert rate_district_splitting(1.6900, nC, nCD) == 0
        assert abs(rate_splitting(41, 0) - 21) <= 1

        assert rate_county_splitting(1.6400, nC, nUD) == 0
        assert rate_district_splitting(1.7000, nC, nUD) == 0
        assert abs(rate_splitting(0, 0) - 0) <= 1

        assert rate_county_splitting(1.8400, nC, nLD) == 0
        assert rate_district_splitting(1.4200, nC, nLD) == 44
        assert abs(rate_splitting(0, 44) - 22) <= 1


### END ###
