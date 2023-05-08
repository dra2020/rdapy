#!/usr/bin/env python3

"""
DEBUG
"""

from rdapy.compactness import *
from testutils import *

shapes_path = "testdata/compactness/NC-116th-Congressional"
shapes, _ = load_shapes(shapes_path, id="id")

scorecard_path = "testdata/compactness/NC-116th-Congressional/expected.json"
scorecard = read_json(scorecard_path)

assert True  # TODO

### END ###
