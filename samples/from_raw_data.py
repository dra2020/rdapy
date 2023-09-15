#!/usr/bin/env python3

"""
Sample starting from raw data
"""

from rdapy import *
from testutils import *

# Parameters

xx: str = "NC"
data_path: str = "~/local/sample-data"

do_shapes: bool = False

# Shapes

if do_shapes:
    shapes_path: str = os.path.expanduser(f"{data_path}/tl_2020_37_tabblock20")
    shapes, _ = load_shapes(shapes_path, id="GEOID20")
    # shapes = [item[1] for item in shapes]  # discard the id

    # TODO: More

pass
