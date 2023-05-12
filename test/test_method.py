#!/usr/bin/env python3

"""
TEST PARTISAN METHOD
"""


from rdapy.partisan.method import *
from testutils import *


class TestPartisanMethod:
    def test_seat_probabilities(self) -> None:
        # 35.0000% share

        assert approx_equal(est_seat_probability(0.350000), 0.000088, places=5)

        # 35.3030% share

        assert approx_equal(est_seat_probability(0.353030), 0.000119, places=5)

        # 35.6061% share

        assert approx_equal(est_seat_probability(0.356061), 0.000160, places=5)

        # 35.9091% share

        assert approx_equal(est_seat_probability(0.359091), 0.000214, places=5)

        # 36.2121% share

        assert approx_equal(est_seat_probability(0.362121), 0.000283, places=5)

        # 36.5152% share

        assert approx_equal(est_seat_probability(0.365152), 0.000374, places=5)

        # 36.8182% share

        assert approx_equal(est_seat_probability(0.368182), 0.000491, places=5)

        # 37.1212% share

        assert approx_equal(est_seat_probability(0.371212), 0.000642, places=5)

        # 37.4242% share

        assert approx_equal(est_seat_probability(0.374242), 0.000833, places=5)

        # 37.7273% share

        assert approx_equal(est_seat_probability(0.377273), 0.001077, places=5)

        # 38.0303% share

        assert approx_equal(est_seat_probability(0.380303), 0.001384, places=5)

        # 38.3333% share

        assert approx_equal(est_seat_probability(0.383333), 0.001769, places=5)

        # 38.6364% share

        assert approx_equal(est_seat_probability(0.386364), 0.002249, places=5)

        # 38.9394% share

        assert approx_equal(est_seat_probability(0.389394), 0.002845, places=5)

        # 39.2424% share

        assert approx_equal(est_seat_probability(0.392424), 0.003579, places=5)

        # 39.5455% share

        assert approx_equal(est_seat_probability(0.395455), 0.004479, places=5)

        # 39.8485% share

        assert approx_equal(est_seat_probability(0.398485), 0.005576, places=5)

        # 40.1515% share

        assert approx_equal(est_seat_probability(0.401515), 0.006906, places=5)

        # 40.4545% share

        assert approx_equal(est_seat_probability(0.404545), 0.008508, places=5)

        # 40.7576% share

        assert approx_equal(est_seat_probability(0.407576), 0.010427, places=5)

        # 41.0606% share

        assert approx_equal(est_seat_probability(0.410606), 0.012714, places=5)

        # 41.3636% share

        assert approx_equal(est_seat_probability(0.413636), 0.015422, places=5)

        # 41.6667% share

        assert approx_equal(est_seat_probability(0.416667), 0.018610, places=5)

        # 41.9697% share

        assert approx_equal(est_seat_probability(0.419697), 0.022344, places=5)

        # 42.2727% share

        assert approx_equal(est_seat_probability(0.422727), 0.026691, places=5)

        # 42.5758% share

        assert approx_equal(est_seat_probability(0.425758), 0.031722, places=5)

        # 42.8788% share

        assert approx_equal(est_seat_probability(0.428788), 0.037513, places=5)

        # 43.1818% share

        assert approx_equal(est_seat_probability(0.431818), 0.044140, places=5)

        # 43.4848% share

        assert approx_equal(est_seat_probability(0.434848), 0.051679, places=5)

        # 43.7879% share

        assert approx_equal(est_seat_probability(0.437879), 0.060208, places=5)

        # 44.0909% share

        assert approx_equal(est_seat_probability(0.440909), 0.069801, places=5)

        # 44.3939% share

        assert approx_equal(est_seat_probability(0.443939), 0.080530, places=5)

        # 44.6970% share

        assert approx_equal(est_seat_probability(0.446970), 0.092460, places=5)

        # 45.0000% share

        assert approx_equal(est_seat_probability(0.450000), 0.105650, places=5)

        # 45.3030% share

        assert approx_equal(est_seat_probability(0.453030), 0.120149, places=5)

        # 45.6061% share

        assert approx_equal(est_seat_probability(0.456061), 0.135996, places=5)

        # 45.9091% share

        assert approx_equal(est_seat_probability(0.459091), 0.153218, places=5)

        # 46.2121% share

        assert approx_equal(est_seat_probability(0.462121), 0.171827, places=5)

        # 46.5152% share

        assert approx_equal(est_seat_probability(0.465152), 0.191819, places=5)

        # 46.8182% share

        assert approx_equal(est_seat_probability(0.468182), 0.213175, places=5)

        # 47.1212% share

        assert approx_equal(est_seat_probability(0.471212), 0.235856, places=5)

        # 47.4242% share

        assert approx_equal(est_seat_probability(0.474242), 0.259807, places=5)

        # 47.7273% share

        assert approx_equal(est_seat_probability(0.477273), 0.284956, places=5)

        # 48.0303% share

        assert approx_equal(est_seat_probability(0.480303), 0.311210, places=5)

        # 48.3333% share

        assert approx_equal(est_seat_probability(0.483333), 0.338461, places=5)

        # 48.6364% share

        assert approx_equal(est_seat_probability(0.486364), 0.366586, places=5)

        # 48.9394% share

        assert approx_equal(est_seat_probability(0.489394), 0.395446, places=5)

        # 49.2424% share

        assert approx_equal(est_seat_probability(0.492424), 0.424892, places=5)

        # 49.5455% share

        assert approx_equal(est_seat_probability(0.495455), 0.454763, places=5)

        # 49.8485% share

        assert approx_equal(est_seat_probability(0.498485), 0.484892, places=5)

        # 50.1515% share

        assert approx_equal(est_seat_probability(0.501515), 0.515108, places=5)

        # 50.4545% share

        assert approx_equal(est_seat_probability(0.504545), 0.545237, places=5)

        # 50.7576% share

        assert approx_equal(est_seat_probability(0.507576), 0.575108, places=5)

        # 51.0606% share

        assert approx_equal(est_seat_probability(0.510606), 0.604554, places=5)

        # 51.3636% share

        assert approx_equal(est_seat_probability(0.513636), 0.633414, places=5)

        # 51.6667% share

        assert approx_equal(est_seat_probability(0.516667), 0.661539, places=5)

        # 51.9697% share

        assert approx_equal(est_seat_probability(0.519697), 0.688790, places=5)

        # 52.2727% share

        assert approx_equal(est_seat_probability(0.522727), 0.715044, places=5)

        # 52.5758% share

        assert approx_equal(est_seat_probability(0.525758), 0.740193, places=5)

        # 52.8788% share

        assert approx_equal(est_seat_probability(0.528788), 0.764144, places=5)

        # 53.1818% share

        assert approx_equal(est_seat_probability(0.531818), 0.786825, places=5)

        # 53.4848% share

        assert approx_equal(est_seat_probability(0.534848), 0.808181, places=5)

        # 53.7879% share

        assert approx_equal(est_seat_probability(0.537879), 0.828173, places=5)

        # 54.0909% share

        assert approx_equal(est_seat_probability(0.540909), 0.846782, places=5)

        # 54.3939% share

        assert approx_equal(est_seat_probability(0.543939), 0.864004, places=5)

        # 54.6970% share

        assert approx_equal(est_seat_probability(0.546970), 0.879851, places=5)

        # 55.0000% share

        assert approx_equal(est_seat_probability(0.550000), 0.894350, places=5)

        # 55.3030% share

        assert approx_equal(est_seat_probability(0.553030), 0.907540, places=5)

        # 55.6061% share

        assert approx_equal(est_seat_probability(0.556061), 0.919470, places=5)

        # 55.9091% share

        assert approx_equal(est_seat_probability(0.559091), 0.930199, places=5)

        # 56.2121% share

        assert approx_equal(est_seat_probability(0.562121), 0.939792, places=5)

        # 56.5152% share

        assert approx_equal(est_seat_probability(0.565152), 0.948321, places=5)

        # 56.8182% share

        assert approx_equal(est_seat_probability(0.568182), 0.955860, places=5)

        # 57.1212% share

        assert approx_equal(est_seat_probability(0.571212), 0.962487, places=5)

        # 57.4242% share

        assert approx_equal(est_seat_probability(0.574242), 0.968278, places=5)

        # 57.7273% share

        assert approx_equal(est_seat_probability(0.577273), 0.973309, places=5)

        # 58.0303% share

        assert approx_equal(est_seat_probability(0.580303), 0.977656, places=5)

        # 58.3333% share

        assert approx_equal(est_seat_probability(0.583333), 0.981390, places=5)

        # 58.6364% share

        assert approx_equal(est_seat_probability(0.586364), 0.984578, places=5)

        # 58.9394% share

        assert approx_equal(est_seat_probability(0.589394), 0.987286, places=5)

        # 59.2424% share

        assert approx_equal(est_seat_probability(0.592424), 0.989573, places=5)

        # 59.5455% share

        assert approx_equal(est_seat_probability(0.595455), 0.991492, places=5)

        # 59.8485% share

        assert approx_equal(est_seat_probability(0.598485), 0.993094, places=5)

        # 60.1515% share

        assert approx_equal(est_seat_probability(0.601515), 0.994424, places=5)

        # 60.4545% share

        assert approx_equal(est_seat_probability(0.604545), 0.995521, places=5)

        # 60.7576% share

        assert approx_equal(est_seat_probability(0.607576), 0.996421, places=5)

        # 61.0606% share

        assert approx_equal(est_seat_probability(0.610606), 0.997155, places=5)

        # 61.3636% share

        assert approx_equal(est_seat_probability(0.613636), 0.997751, places=5)

        # 61.6667% share

        assert approx_equal(est_seat_probability(0.616667), 0.998231, places=5)

        # 61.9697% share

        assert approx_equal(est_seat_probability(0.619697), 0.998616, places=5)

        # 62.2727% share

        assert approx_equal(est_seat_probability(0.622727), 0.998923, places=5)

        # 62.5758% share

        assert approx_equal(est_seat_probability(0.625758), 0.999167, places=5)

        # 62.8788% share

        assert approx_equal(est_seat_probability(0.628788), 0.999358, places=5)

        # 63.1818% share

        assert approx_equal(est_seat_probability(0.631818), 0.999509, places=5)

        # 63.4848% share

        assert approx_equal(est_seat_probability(0.634848), 0.999626, places=5)

        # 63.7879% share

        assert approx_equal(est_seat_probability(0.637879), 0.999717, places=5)

        # 64.0909% share

        assert approx_equal(est_seat_probability(0.640909), 0.999786, places=5)

        # 64.3939% share

        assert approx_equal(est_seat_probability(0.643939), 0.999840, places=5)

        # 64.6970% share

        assert approx_equal(est_seat_probability(0.646970), 0.999881, places=5)

        # 65.0000% share

        assert approx_equal(est_seat_probability(0.650000), 0.999912, places=5)

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

        approx_equal(est_seat_probability(rV[0]), Sf[0], places=5)
        approx_equal(est_seat_probability(rV[1]), Sf[1], places=5)
        approx_equal(est_seat_probability(rV[2]), Sf[2], places=5)
        approx_equal(est_seat_probability(rV[3]), Sf[3], places=5)
        approx_equal(est_seat_probability(rV[4]), Sf[4], places=5)
        approx_equal(est_seat_probability(rV[5]), Sf[5], places=5)
        approx_equal(est_seat_probability(rV[6]), Sf[6], places=5)

        # CO probable seats
        approx_equal(est_seats(rV), 3.5536888476972255, places=5)


### END ###
