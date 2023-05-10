#!/usr/bin/env python3

"""
DEBUG
"""

from rdapy.splitting import *
from testutils import *

communities = [
    {"name": "one", "splits": [0.33, 0.33, 0.34]},
    {"name": "two", "splits": [0.92, 0.05, 0.03]},
]

analysis = calc_coi_splitting(communities)
print(analysis)
pass

### END ###
