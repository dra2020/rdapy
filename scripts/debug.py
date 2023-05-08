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

scorecard_path = "testdata/compactness/NC-116th-Congressional/expected.json"
scorecard = read_json(scorecard_path)

make_compactness_scorecard(shapes)

pass

### END ###
