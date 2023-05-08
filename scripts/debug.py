#!/usr/bin/env python3

"""
DEBUG
"""

from rdapy.compactness import *
from testutils import *

INDEX: int = 0
VALUE: int = 1

shapes_path = "testdata/compactness/NC-116th-Congressional"
shapes, _ = load_shapes(shapes_path, id="id")
shapes = [item[VALUE] for item in shapes]  # discard the id

expected_path = "testdata/compactness/NC-116th-Congressional/expected.json"
expected = read_json(expected_path)

actual: dict = calc_compactness(shapes)

print(f"avgReock: {actual['avgReock']} | {expected['avgReock']}")
print(f"avgPolsby: {actual['avgPolsby']} | {expected['avgPolsby']}")
print(f"avgKIWYSI: {actual['avgKIWYSI']} | {expected['avgKIWYSI']}")

for i in range(len(actual["byDistrict"])):
    print(f"District {i+1}")
    print(
        f"  reock: {actual['byDistrict'][i]['reock']} | {expected['byDistrict'][i]['reock']}"
    )
    print(
        f"  polsby: {actual['byDistrict'][i]['polsby']} | {expected['byDistrict'][i]['polsby']}"
    )
    print(
        f"  kiwysiRank: {actual['byDistrict'][i]['kiwysiRank']} | {expected['byDistrict'][i]['kiwysiRank']}"
    )

# assert dict_approx_equal(actual, expected, int_threshold=1)

pass

### END ###
