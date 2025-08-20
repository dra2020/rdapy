#!/usr/bin/env python3

"""
THIS IS A HELPER SCRIPT TO COMPARE THE ADJACENCY GRAPHS I USED IN A PAPER WITH THOSE FROM THE DRA GEOJSON PACKAGE
"""

import os

study_states = ["FL", "IL", "MI", "NC", "NY", "OH", "WI"]

for xx in study_states:
    print(f">>> {xx} <<<")
    command: str = (
        f"scripts/graphs/compare_2_graphs.py --graph1 ~/dev/vtd_data/2020_VTD/{xx}/{xx}_2020_graph.json --graph2 ~/Downloads/dra_vtd_data/{xx}_2020_graph.json"
    )
    os.system(command)

### END ###
