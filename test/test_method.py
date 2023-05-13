#!/usr/bin/env python3

"""
TEST PARTISAN METHOD
"""


from rdapy.partisan.method import *
from rdapy.partisan.constants import *
from testutils import *


class TestPartisanMethod:
    def test_seat_probabilities(self) -> None:
        # 35.0000% share

        assert approx_equal(est_seat_probability(0.350000), 0.000088, places=4)

        # 35.3030% share

        assert approx_equal(est_seat_probability(0.353030), 0.000119, places=4)

        # 35.6061% share

        assert approx_equal(est_seat_probability(0.356061), 0.000160, places=4)

        # 35.9091% share

        assert approx_equal(est_seat_probability(0.359091), 0.000214, places=4)

        # 36.2121% share

        assert approx_equal(est_seat_probability(0.362121), 0.000283, places=4)

        # 36.5152% share

        assert approx_equal(est_seat_probability(0.365152), 0.000374, places=4)

        # 36.8182% share

        assert approx_equal(est_seat_probability(0.368182), 0.000491, places=4)

        # 37.1212% share

        assert approx_equal(est_seat_probability(0.371212), 0.000642, places=4)

        # 37.4242% share

        assert approx_equal(est_seat_probability(0.374242), 0.000833, places=4)

        # 37.7273% share

        assert approx_equal(est_seat_probability(0.377273), 0.001077, places=4)

        # 38.0303% share

        assert approx_equal(est_seat_probability(0.380303), 0.001384, places=4)

        # 38.3333% share

        assert approx_equal(est_seat_probability(0.383333), 0.001769, places=4)

        # 38.6364% share

        assert approx_equal(est_seat_probability(0.386364), 0.002249, places=4)

        # 38.9394% share

        assert approx_equal(est_seat_probability(0.389394), 0.002845, places=4)

        # 39.2424% share

        assert approx_equal(est_seat_probability(0.392424), 0.003579, places=4)

        # 39.5455% share

        assert approx_equal(est_seat_probability(0.395455), 0.004479, places=4)

        # 39.8485% share

        assert approx_equal(est_seat_probability(0.398485), 0.005576, places=4)

        # 40.1515% share

        assert approx_equal(est_seat_probability(0.401515), 0.006906, places=4)

        # 40.4545% share

        assert approx_equal(est_seat_probability(0.404545), 0.008508, places=4)

        # 40.7576% share

        assert approx_equal(est_seat_probability(0.407576), 0.010427, places=4)

        # 41.0606% share

        assert approx_equal(est_seat_probability(0.410606), 0.012714, places=4)

        # 41.3636% share

        assert approx_equal(est_seat_probability(0.413636), 0.015422, places=4)

        # 41.6667% share

        assert approx_equal(est_seat_probability(0.416667), 0.018610, places=4)

        # 41.9697% share

        assert approx_equal(est_seat_probability(0.419697), 0.022344, places=4)

        # 42.2727% share

        assert approx_equal(est_seat_probability(0.422727), 0.026691, places=4)

        # 42.5758% share

        assert approx_equal(est_seat_probability(0.425758), 0.031722, places=4)

        # 42.8788% share

        assert approx_equal(est_seat_probability(0.428788), 0.037513, places=4)

        # 43.1818% share

        assert approx_equal(est_seat_probability(0.431818), 0.044140, places=4)

        # 43.4848% share

        assert approx_equal(est_seat_probability(0.434848), 0.051679, places=4)

        # 43.7879% share

        assert approx_equal(est_seat_probability(0.437879), 0.060208, places=4)

        # 44.0909% share

        assert approx_equal(est_seat_probability(0.440909), 0.069801, places=4)

        # 44.3939% share

        assert approx_equal(est_seat_probability(0.443939), 0.080530, places=4)

        # 44.6970% share

        assert approx_equal(est_seat_probability(0.446970), 0.092460, places=4)

        # 45.0000% share

        assert approx_equal(est_seat_probability(0.450000), 0.105650, places=4)

        # 45.3030% share

        assert approx_equal(est_seat_probability(0.453030), 0.120149, places=4)

        # 45.6061% share

        assert approx_equal(est_seat_probability(0.456061), 0.135996, places=4)

        # 45.9091% share

        assert approx_equal(est_seat_probability(0.459091), 0.153218, places=4)

        # 46.2121% share

        assert approx_equal(est_seat_probability(0.462121), 0.171827, places=4)

        # 46.5152% share

        assert approx_equal(est_seat_probability(0.465152), 0.191819, places=4)

        # 46.8182% share

        assert approx_equal(est_seat_probability(0.468182), 0.213175, places=4)

        # 47.1212% share

        assert approx_equal(est_seat_probability(0.471212), 0.235856, places=4)

        # 47.4242% share

        assert approx_equal(est_seat_probability(0.474242), 0.259807, places=4)

        # 47.7273% share

        assert approx_equal(est_seat_probability(0.477273), 0.284956, places=4)

        # 48.0303% share

        assert approx_equal(est_seat_probability(0.480303), 0.311210, places=4)

        # 48.3333% share

        assert approx_equal(est_seat_probability(0.483333), 0.338461, places=4)

        # 48.6364% share

        assert approx_equal(est_seat_probability(0.486364), 0.366586, places=4)

        # 48.9394% share

        assert approx_equal(est_seat_probability(0.489394), 0.395446, places=4)

        # 49.2424% share

        assert approx_equal(est_seat_probability(0.492424), 0.424892, places=4)

        # 49.5455% share

        assert approx_equal(est_seat_probability(0.495455), 0.454763, places=4)

        # 49.8485% share

        assert approx_equal(est_seat_probability(0.498485), 0.484892, places=4)

        # 50.1515% share

        assert approx_equal(est_seat_probability(0.501515), 0.515108, places=4)

        # 50.4545% share

        assert approx_equal(est_seat_probability(0.504545), 0.545237, places=4)

        # 50.7576% share

        assert approx_equal(est_seat_probability(0.507576), 0.575108, places=4)

        # 51.0606% share

        assert approx_equal(est_seat_probability(0.510606), 0.604554, places=4)

        # 51.3636% share

        assert approx_equal(est_seat_probability(0.513636), 0.633414, places=4)

        # 51.6667% share

        assert approx_equal(est_seat_probability(0.516667), 0.661539, places=4)

        # 51.9697% share

        assert approx_equal(est_seat_probability(0.519697), 0.688790, places=4)

        # 52.2727% share

        assert approx_equal(est_seat_probability(0.522727), 0.715044, places=4)

        # 52.5758% share

        assert approx_equal(est_seat_probability(0.525758), 0.740193, places=4)

        # 52.8788% share

        assert approx_equal(est_seat_probability(0.528788), 0.764144, places=4)

        # 53.1818% share

        assert approx_equal(est_seat_probability(0.531818), 0.786825, places=4)

        # 53.4848% share

        assert approx_equal(est_seat_probability(0.534848), 0.808181, places=4)

        # 53.7879% share

        assert approx_equal(est_seat_probability(0.537879), 0.828173, places=4)

        # 54.0909% share

        assert approx_equal(est_seat_probability(0.540909), 0.846782, places=4)

        # 54.3939% share

        assert approx_equal(est_seat_probability(0.543939), 0.864004, places=4)

        # 54.6970% share

        assert approx_equal(est_seat_probability(0.546970), 0.879851, places=4)

        # 55.0000% share

        assert approx_equal(est_seat_probability(0.550000), 0.894350, places=4)

        # 55.3030% share

        assert approx_equal(est_seat_probability(0.553030), 0.907540, places=4)

        # 55.6061% share

        assert approx_equal(est_seat_probability(0.556061), 0.919470, places=4)

        # 55.9091% share

        assert approx_equal(est_seat_probability(0.559091), 0.930199, places=4)

        # 56.2121% share

        assert approx_equal(est_seat_probability(0.562121), 0.939792, places=4)

        # 56.5152% share

        assert approx_equal(est_seat_probability(0.565152), 0.948321, places=4)

        # 56.8182% share

        assert approx_equal(est_seat_probability(0.568182), 0.955860, places=4)

        # 57.1212% share

        assert approx_equal(est_seat_probability(0.571212), 0.962487, places=4)

        # 57.4242% share

        assert approx_equal(est_seat_probability(0.574242), 0.968278, places=4)

        # 57.7273% share

        assert approx_equal(est_seat_probability(0.577273), 0.973309, places=4)

        # 58.0303% share

        assert approx_equal(est_seat_probability(0.580303), 0.977656, places=4)

        # 58.3333% share

        assert approx_equal(est_seat_probability(0.583333), 0.981390, places=4)

        # 58.6364% share

        assert approx_equal(est_seat_probability(0.586364), 0.984578, places=4)

        # 58.9394% share

        assert approx_equal(est_seat_probability(0.589394), 0.987286, places=4)

        # 59.2424% share

        assert approx_equal(est_seat_probability(0.592424), 0.989573, places=4)

        # 59.5455% share

        assert approx_equal(est_seat_probability(0.595455), 0.991492, places=4)

        # 59.8485% share

        assert approx_equal(est_seat_probability(0.598485), 0.993094, places=4)

        # 60.1515% share

        assert approx_equal(est_seat_probability(0.601515), 0.994424, places=4)

        # 60.4545% share

        assert approx_equal(est_seat_probability(0.604545), 0.995521, places=4)

        # 60.7576% share

        assert approx_equal(est_seat_probability(0.607576), 0.996421, places=4)

        # 61.0606% share

        assert approx_equal(est_seat_probability(0.610606), 0.997155, places=4)

        # 61.3636% share

        assert approx_equal(est_seat_probability(0.613636), 0.997751, places=4)

        # 61.6667% share

        assert approx_equal(est_seat_probability(0.616667), 0.998231, places=4)

        # 61.9697% share

        assert approx_equal(est_seat_probability(0.619697), 0.998616, places=4)

        # 62.2727% share

        assert approx_equal(est_seat_probability(0.622727), 0.998923, places=4)

        # 62.5758% share

        assert approx_equal(est_seat_probability(0.625758), 0.999167, places=4)

        # 62.8788% share

        assert approx_equal(est_seat_probability(0.628788), 0.999358, places=4)

        # 63.1818% share

        assert approx_equal(est_seat_probability(0.631818), 0.999509, places=4)

        # 63.4848% share

        assert approx_equal(est_seat_probability(0.634848), 0.999626, places=4)

        # 63.7879% share

        assert approx_equal(est_seat_probability(0.637879), 0.999717, places=4)

        # 64.0909% share

        assert approx_equal(est_seat_probability(0.640909), 0.999786, places=4)

        # 64.3939% share

        assert approx_equal(est_seat_probability(0.643939), 0.999840, places=4)

        # 64.6970% share

        assert approx_equal(est_seat_probability(0.646970), 0.999881, places=4)

        # 65.0000% share

        assert approx_equal(est_seat_probability(0.650000), 0.999912, places=4)

    def test_seat_probabilities_2(self) -> None:
        # CO districts
        rV: list[float] = [
            0.678999,
            0.575848,
            0.480675,
            0.389881,
            0.361222,
            0.491961,
            0.540539,
        ]

        # Benchmarks from original Python code
        Sf: list[float] = [
            0.9999961789873051,
            0.9710331984032442,
            0.3145034920338179,
            0.0029528202902014966,
            0.0002607625652328305,
            0.4203590611657488,
            0.8445833342516753,
        ]

        approx_equal(est_seat_probability(rV[0]), Sf[0], places=4)
        approx_equal(est_seat_probability(rV[1]), Sf[1], places=4)
        approx_equal(est_seat_probability(rV[2]), Sf[2], places=4)
        approx_equal(est_seat_probability(rV[3]), Sf[3], places=4)
        approx_equal(est_seat_probability(rV[4]), Sf[4], places=4)
        approx_equal(est_seat_probability(rV[5]), Sf[5], places=4)
        approx_equal(est_seat_probability(rV[6]), Sf[6], places=4)

        # CO probable seats
        approx_equal(est_seats(rV), 3.5536888476972255, places=4)

    def test_district_responsiveness(self) -> None:
        # 35.0000% share

        assert approx_equal(est_district_responsiveness(0.350000), 0.000354, places=4)

        # 35.3030% share

        assert approx_equal(est_district_responsiveness(0.353030), 0.000477, places=4)

        # 35.6061% share

        assert approx_equal(est_district_responsiveness(0.356061), 0.000640, places=4)

        # 35.9091% share

        assert approx_equal(est_district_responsiveness(0.359091), 0.000854, places=4)

        # 36.2121% share

        assert approx_equal(est_district_responsiveness(0.362121), 0.001134, places=4)

        # 36.5152% share

        assert approx_equal(est_district_responsiveness(0.365152), 0.001496, places=4)

        # 36.8182% share

        assert approx_equal(est_district_responsiveness(0.368182), 0.001964, places=4)

        # 37.1212% share

        assert approx_equal(est_district_responsiveness(0.371212), 0.002565, places=4)

        # 37.4242% share

        assert approx_equal(est_district_responsiveness(0.374242), 0.003331, places=4)

        # 37.7273% share

        assert approx_equal(est_district_responsiveness(0.377273), 0.004303, places=4)

        # 38.0303% share

        assert approx_equal(est_district_responsiveness(0.380303), 0.005528, places=4)

        # 38.3333% share

        assert approx_equal(est_district_responsiveness(0.383333), 0.007063, places=4)

        # 38.6364% share

        assert approx_equal(est_district_responsiveness(0.386364), 0.008977, places=4)

        # 38.9394% share

        assert approx_equal(est_district_responsiveness(0.389394), 0.011347, places=4)

        # 39.2424% share

        assert approx_equal(est_district_responsiveness(0.392424), 0.014265, places=4)

        # 39.5455% share

        assert approx_equal(est_district_responsiveness(0.395455), 0.017837, places=4)

        # 39.8485% share

        assert approx_equal(est_district_responsiveness(0.398485), 0.022181, places=4)

        # 40.1515% share

        assert approx_equal(est_district_responsiveness(0.401515), 0.027433, places=4)

        # 40.4545% share

        assert approx_equal(est_district_responsiveness(0.404545), 0.033742, places=4)

        # 40.7576% share

        assert approx_equal(est_district_responsiveness(0.407576), 0.041274, places=4)

        # 41.0606% share

        assert approx_equal(est_district_responsiveness(0.410606), 0.050208, places=4)

        # 41.3636% share

        assert approx_equal(est_district_responsiveness(0.413636), 0.060735, places=4)

        # 41.6667% share

        assert approx_equal(est_district_responsiveness(0.416667), 0.073056, places=4)

        # 41.9697% share

        assert approx_equal(est_district_responsiveness(0.419697), 0.087380, places=4)

        # 42.2727% share

        assert approx_equal(est_district_responsiveness(0.422727), 0.103914, places=4)

        # 42.5758% share

        assert approx_equal(est_district_responsiveness(0.425758), 0.122865, places=4)

        # 42.8788% share

        assert approx_equal(est_district_responsiveness(0.428788), 0.144424, places=4)

        # 43.1818% share

        assert approx_equal(est_district_responsiveness(0.431818), 0.168765, places=4)

        # 43.4848% share

        assert approx_equal(est_district_responsiveness(0.434848), 0.196033, places=4)

        # 43.7879% share

        assert approx_equal(est_district_responsiveness(0.437879), 0.226332, places=4)

        # 44.0909% share

        assert approx_equal(est_district_responsiveness(0.440909), 0.259716, places=4)

        # 44.3939% share

        assert approx_equal(est_district_responsiveness(0.443939), 0.296180, places=4)

        # 44.6970% share

        assert approx_equal(est_district_responsiveness(0.446970), 0.335645, places=4)

        # 45.0000% share

        assert approx_equal(est_district_responsiveness(0.450000), 0.377952, places=4)

        # 45.3030% share

        assert approx_equal(est_district_responsiveness(0.453030), 0.422853, places=4)

        # 45.6061% share

        assert approx_equal(est_district_responsiveness(0.456061), 0.470006, places=4)

        # 45.9091% share

        assert approx_equal(est_district_responsiveness(0.459091), 0.518970, places=4)

        # 46.2121% share

        assert approx_equal(est_district_responsiveness(0.462121), 0.569210, places=4)

        # 46.5152% share

        assert approx_equal(est_district_responsiveness(0.465152), 0.620098, places=4)

        # 46.8182% share

        assert approx_equal(est_district_responsiveness(0.468182), 0.670925, places=4)

        # 47.1212% share

        assert approx_equal(est_district_responsiveness(0.471212), 0.720911, places=4)

        # 47.4242% share

        assert approx_equal(est_district_responsiveness(0.474242), 0.769230, places=4)

        # 47.7273% share

        assert approx_equal(est_district_responsiveness(0.477273), 0.815024, places=4)

        # 48.0303% share

        assert approx_equal(est_district_responsiveness(0.480303), 0.857433, places=4)

        # 48.3333% share

        assert approx_equal(est_district_responsiveness(0.483333), 0.895621, places=4)

        # 48.6364% share

        assert approx_equal(est_district_responsiveness(0.486364), 0.928803, places=4)

        # 48.9394% share

        assert approx_equal(est_district_responsiveness(0.489394), 0.956274, places=4)

        # 49.2424% share

        assert approx_equal(est_district_responsiveness(0.492424), 0.977435, places=4)

        # 49.5455% share

        assert approx_equal(est_district_responsiveness(0.495455), 0.991814, places=4)

        # 49.8485% share

        assert approx_equal(est_district_responsiveness(0.498485), 0.999087, places=4)

        # 50.1515% share

        assert approx_equal(est_district_responsiveness(0.501515), 0.999087, places=4)

        # 50.4545% share

        assert approx_equal(est_district_responsiveness(0.504545), 0.991814, places=4)

        # 50.7576% share

        assert approx_equal(est_district_responsiveness(0.507576), 0.977435, places=4)

        # 51.0606% share

        assert approx_equal(est_district_responsiveness(0.510606), 0.956274, places=4)

        # 51.3636% share

        assert approx_equal(est_district_responsiveness(0.513636), 0.928803, places=4)

        # 51.6667% share

        assert approx_equal(est_district_responsiveness(0.516667), 0.895621, places=4)

        # 51.9697% share

        assert approx_equal(est_district_responsiveness(0.519697), 0.857433, places=4)

        # 52.2727% share

        assert approx_equal(est_district_responsiveness(0.522727), 0.815024, places=4)

        # 52.5758% share

        assert approx_equal(est_district_responsiveness(0.525758), 0.769230, places=4)

        # 52.8788% share

        assert approx_equal(est_district_responsiveness(0.528788), 0.720911, places=4)

        # 53.1818% share

        assert approx_equal(est_district_responsiveness(0.531818), 0.670925, places=4)

        # 53.4848% share

        assert approx_equal(est_district_responsiveness(0.534848), 0.620098, places=4)

        # 53.7879% share

        assert approx_equal(est_district_responsiveness(0.537879), 0.569210, places=4)

        # 54.0909% share

        assert approx_equal(est_district_responsiveness(0.540909), 0.518970, places=4)

        # 54.3939% share

        assert approx_equal(est_district_responsiveness(0.543939), 0.470006, places=4)

        # 54.6970% share

        assert approx_equal(est_district_responsiveness(0.546970), 0.422853, places=4)

        # 55.0000% share

        assert approx_equal(est_district_responsiveness(0.550000), 0.377952, places=4)

        # 55.3030% share

        assert approx_equal(est_district_responsiveness(0.553030), 0.335645, places=4)

        # 55.6061% share

        assert approx_equal(est_district_responsiveness(0.556061), 0.296180, places=4)

        # 55.9091% share

        assert approx_equal(est_district_responsiveness(0.559091), 0.259716, places=4)

        # 56.2121% share

        assert approx_equal(est_district_responsiveness(0.562121), 0.226332, places=4)

        # 56.5152% share

        assert approx_equal(est_district_responsiveness(0.565152), 0.196033, places=4)

        # 56.8182% share

        assert approx_equal(est_district_responsiveness(0.568182), 0.168765, places=4)

        # 57.1212% share

        assert approx_equal(est_district_responsiveness(0.571212), 0.144424, places=4)

        # 57.4242% share

        assert approx_equal(est_district_responsiveness(0.574242), 0.122865, places=4)

        # 57.7273% share

        assert approx_equal(est_district_responsiveness(0.577273), 0.103914, places=4)

        # 58.0303% share

        assert approx_equal(est_district_responsiveness(0.580303), 0.087380, places=4)

        # 58.3333% share

        assert approx_equal(est_district_responsiveness(0.583333), 0.073056, places=4)

        # 58.6364% share

        assert approx_equal(est_district_responsiveness(0.586364), 0.060735, places=4)

        # 58.9394% share

        assert approx_equal(est_district_responsiveness(0.589394), 0.050208, places=4)

        # 59.2424% share

        assert approx_equal(est_district_responsiveness(0.592424), 0.041274, places=4)

        # 59.5455% share

        assert approx_equal(est_district_responsiveness(0.595455), 0.033742, places=4)

        # 59.8485% share

        assert approx_equal(est_district_responsiveness(0.598485), 0.027433, places=4)

        # 60.1515% share

        assert approx_equal(est_district_responsiveness(0.601515), 0.022181, places=4)

        # 60.4545% share

        assert approx_equal(est_district_responsiveness(0.604545), 0.017837, places=4)

        # 60.7576% share

        assert approx_equal(est_district_responsiveness(0.607576), 0.014265, places=4)

        # 61.0606% share

        assert approx_equal(est_district_responsiveness(0.610606), 0.011347, places=4)

        # 61.3636% share

        assert approx_equal(est_district_responsiveness(0.613636), 0.008977, places=4)

        # 61.6667% share

        assert approx_equal(est_district_responsiveness(0.616667), 0.007063, places=4)

        # 61.9697% share

        assert approx_equal(est_district_responsiveness(0.619697), 0.005528, places=4)

        # 62.2727% share

        assert approx_equal(est_district_responsiveness(0.622727), 0.004303, places=4)

        # 62.5758% share

        assert approx_equal(est_district_responsiveness(0.625758), 0.003331, places=4)

        # 62.8788% share

        assert approx_equal(est_district_responsiveness(0.628788), 0.002565, places=4)

        # 63.1818% share

        assert approx_equal(est_district_responsiveness(0.631818), 0.001964, places=4)

        # 63.4848% share

        assert approx_equal(est_district_responsiveness(0.634848), 0.001496, places=4)

        # 63.7879% share

        assert approx_equal(est_district_responsiveness(0.637879), 0.001134, places=4)

        # 64.0909% share

        assert approx_equal(est_district_responsiveness(0.640909), 0.000854, places=4)

        # 64.3939% share

        assert approx_equal(est_district_responsiveness(0.643939), 0.000640, places=4)

        # 64.6970% share

        assert approx_equal(est_district_responsiveness(0.646970), 0.000477, places=4)

        # 65.0000% share

        assert approx_equal(est_district_responsiveness(0.650000), 0.000354, places=4)

    def test_FPTP_seats(self) -> None:
        rV: list[float]

        # Shutout 0–3

        rV = [0.40, 0.40, 0.40]
        assert est_fptp_seats(rV) == 0

        # Sweep 3–0

        rV = [0.60, 0.60, 0.60]
        assert est_fptp_seats(rV) == 3

        # Split 1–2

        rV = [(0.50 - EPSILON), (0.50 - EPSILON), (0.50 + EPSILON)]
        assert est_fptp_seats(rV) == 1

        # Split 2–1

        rV = [(0.50 + EPSILON), (0.50 + EPSILON), (0.50 - EPSILON)]
        assert est_fptp_seats(rV) == 2

        # Perfectly balanced 0–3

        rV = [0.50, 0.50, 0.50]
        assert est_fptp_seats(rV) == 0

    def test_infer_sv_points(self) -> None:
        expected_sv_points: list[tuple[float, float]] = [
            (0.250000, 0.001285),
            (0.255000, 0.002078),
            (0.260000, 0.003237),
            (0.265000, 0.004857),
            (0.270000, 0.007030),
            (0.275000, 0.009826),
            (0.280000, 0.013279),
            (0.285000, 0.017380),
            (0.290000, 0.022071),
            (0.295000, 0.027248),
            (0.300000, 0.032781),
            (0.305000, 0.038531),
            (0.310000, 0.044370),
            (0.315000, 0.050200),
            (0.320000, 0.055961),
            (0.325000, 0.061632),
            (0.330000, 0.067222),
            (0.335000, 0.072754),
            (0.340000, 0.078258),
            (0.345000, 0.083754),
            (0.350000, 0.089255),
            (0.355000, 0.094764),
            (0.360000, 0.100280),
            (0.365000, 0.105810),
            (0.370000, 0.111371),
            (0.375000, 0.116996),
            (0.380000, 0.122730),
            (0.385000, 0.128634),
            (0.390000, 0.134771),
            (0.395000, 0.141205),
            (0.400000, 0.147996),
            (0.405000, 0.155195),
            (0.410000, 0.162841),
            (0.415000, 0.170965),
            (0.420000, 0.179590),
            (0.425000, 0.188731),
            (0.430000, 0.198400),
            (0.435000, 0.208604),
            (0.440000, 0.219347),
            (0.445000, 0.230633),
            (0.450000, 0.242462),
            (0.455000, 0.254833),
            (0.460000, 0.267741),
            (0.465000, 0.281180),
            (0.470000, 0.295141),
            (0.475000, 0.309616),
            (0.480000, 0.324591),
            (0.485000, 0.340052),
            (0.490000, 0.355983),
            (0.495000, 0.372361),
            (0.500000, 0.389162),
            (0.505000, 0.406351),
            (0.510000, 0.423888),
            (0.515000, 0.441723),
            (0.520000, 0.459797),
            (0.525000, 0.478042),
            (0.530000, 0.496382),
            (0.535000, 0.514734),
            (0.540000, 0.533010),
            (0.545000, 0.551119),
            (0.550000, 0.569931),
            (0.555000, 0.591386),
            (0.560000, 0.612788),
            (0.565000, 0.634024),
            (0.570000, 0.655012),
            (0.575000, 0.675697),
            (0.580000, 0.696061),
            (0.585000, 0.716114),
            (0.590000, 0.735887),
            (0.595000, 0.755425),
            (0.600000, 0.774768),
            (0.605000, 0.793940),
            (0.610000, 0.812933),
            (0.615000, 0.831697),
            (0.620000, 0.850135),
            (0.625000, 0.868103),
            (0.630000, 0.885421),
            (0.635000, 0.901885),
            (0.640000, 0.917287),
            (0.645000, 0.931435),
            (0.650000, 0.944176),
            (0.655000, 0.955405),
            (0.660000, 0.965080),
            (0.665000, 0.973220),
            (0.670000, 0.979902),
            (0.675000, 0.985251),
            (0.680000, 0.989422),
            (0.685000, 0.992591),
            (0.690000, 0.994935),
            (0.695000, 0.996621),
            (0.700000, 0.997802),
            (0.705000, 0.998606),
            (0.710000, 0.999138),
            (0.715000, 0.999481),
            (0.720000, 0.999696),
            (0.725000, 0.999826),
            (0.730000, 0.999904),
            (0.735000, 0.999948),
            (0.740000, 0.999973),
            (0.745000, 0.999986),
            (0.750000, 0.999993),
        ]

        v: int = 0
        s: int = 1

        # Infer SV points for the PA SCOPA-7S PLAN

        profile_path: str = "testdata/partisan/nagle/partisan-PA-SCOPA-7S.json"
        profile: dict = read_json(profile_path)

        rV: list[float] = profile["byDistrict"]
        N: int = len(rV)
        Vf: float = profile["statewide"]
        proportional: bool = True

        actual_sv_points: list[tuple[float, float]] = infer_sv_points(
            Vf, rV, proportional
        )

        # NOTE - The expects seat values above are seat *shares* (not #'s of seats)
        assert approx_equal(actual_sv_points[0][s] / N, expected_sv_points[0][s])
        assert approx_equal(actual_sv_points[50][s] / N, expected_sv_points[50][s])
        assert approx_equal(actual_sv_points[100][s] / N, expected_sv_points[100][s])

        # This is an exact copy of the previous test, except the Vf values are not sorted.

        profile_path: str = "testdata/partisan/nagle/partisan-PA-SCOPA-7S-unsorted.json"
        profile: dict = read_json(profile_path)

        rV: list[float] = profile["byDistrict"]
        N: int = len(rV)
        Vf: float = profile["statewide"]
        proportional: bool = True

        actual_sv_points: list[tuple[float, float]] = infer_sv_points(
            Vf, rV, proportional
        )

        assert approx_equal(actual_sv_points[0][s] / N, expected_sv_points[0][s])
        assert approx_equal(actual_sv_points[50][s] / N, expected_sv_points[50][s])
        assert approx_equal(actual_sv_points[100][s] / N, expected_sv_points[100][s])


### END ###
