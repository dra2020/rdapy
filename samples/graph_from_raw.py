#!/usr/bin/env python3

"""
Sample adjacencies analysis starting from raw data
"""

import os
from typing import Any, Optional, Iterable

from libpysal.weights import Rook, WSP
from shapely.geometry import (
    shape,
    Polygon,
    MultiPolygon,
    Point,
    MultiPoint,
    LineString,
    MultiLineString,
    LinearRing,
    GeometryCollection,
)
import fiona

from rdapy import *
from testutils import *

### FILES ###

data_dir: str = "~/local/sample-data"

# Exported from DRA
plan_file: str = "NC_2022_Congress_Official.csv"

# These are the Census TIGER/Line block shapes for the state.
shapes_file: str = "tl_2020_37_tabblock20/tl_2020_37_tabblock20.shp"

# These block-adjacencies dervied from the block shapes.
# It contains a virtual OUT_OF_STATE border node that surrounds the state.
contiguity_file: str = "block_contiguity.json"

### HELPERS ###


class Graph:
    """Make an adjacency graph from a shapefile, including virtual OUT_OF_STATE neighbors."""

    _data: dict
    _adjacencies: set[tuple[str, str]]

    def __init__(self, input: str, id_field: str = "") -> None:
        self._abs_path: str = os.path.abspath(input)
        self._id_field: Optional[str] = id_field
        self._data: dict = self._from_shapefile()
        self.is_consistent()
        self._shp_by_geoid: dict
        self._meta: Optional[dict[str, Any]]
        self._shp_by_geoid, self._meta = self._read_shapes(
            self._abs_path, self._id_field
        )
        self._data: dict = self._add_out_of_state_neighbors()

    def _from_shapefile(self) -> Any | dict[Any, Any]:
        """Extract a rook graph from a shapefile."""

        g: Rook | WSP = Rook.from_shapefile(self._abs_path, self._id_field)
        assert isinstance(g, Rook)

        return g.neighbors  # Get rid of all the extraneous PySAL stuff

    def is_consistent(self) -> bool:
        """Make sure each node is in every neighbor's neighbor list"""

        for node, neighbors in self._data.items():
            for neighbor in neighbors:
                neighbor_neighbors: list[str | int] = self._data[neighbor]
                if node in neighbor_neighbors:
                    pass
                else:
                    return False

        return True

    def _read_shapes(
        self, shp_file: str, id: str
    ) -> tuple[dict, Optional[dict[str, Any]]]:
        """Load a shapefile into a dictionary of shapes keyed by the value of the specified field."""

        shp_path: str = os.path.expanduser(shp_file)
        shapes_by_id: dict = dict()
        meta: Optional[dict[str, Any]] = None

        with fiona.Env():
            with fiona.open(shp_path) as source:
                if source:
                    meta = source.meta
                    for item in source:
                        obj_id: str = item["properties"][id]
                        shp: (
                            Point
                            | MultiPoint
                            | LineString
                            | MultiLineString
                            | Polygon
                            | MultiPolygon
                            | LinearRing
                            | GeometryCollection
                        ) = shape(
                            item["geometry"]
                        )  # type: ignore

                        shapes_by_id[obj_id] = shp

        return shapes_by_id, meta

    def _add_out_of_state_neighbors(self) -> dict:
        """Add the virtual OUT_OF_STATE geoids to reflect interstate borders."""

        new_graph: dict = dict()
        new_graph[OUT_OF_STATE] = []
        epsilon: float = 1.0e-12

        for node, neighbors in self._data.items():
            new_graph[node] = []

            node_shp: Polygon | MultiPolygon = self._shp_by_geoid[node]
            perimeter: float = node_shp.length
            total_shared_border: float = 0.0

            for neighbor in neighbors:
                new_graph[node].append(neighbor)

                neighbor_shp: Polygon | MultiPolygon = self._shp_by_geoid[neighbor]
                shared_edge = node_shp.intersection(neighbor_shp)
                shared_border: float = shared_edge.length

                total_shared_border += shared_border

            if (perimeter - total_shared_border) > epsilon:
                new_graph[node].append(OUT_OF_STATE)
                new_graph[OUT_OF_STATE].append(node)

        return new_graph

    def data(self) -> dict:
        """Return the graph data."""

        return self._data

    def nodes(self) -> list[str | int]:
        """Return the nodes in the graph."""

        return list(self._data.keys())

    def neighbors(self, node: str | int, *, excluding: list = []) -> list[str | int]:
        """Return the neighbors of a node."""

        if node not in self._data:
            return []

        if len(excluding) == 0:
            return self._data[node]
        else:
            return [n for n in self._data[node] if n not in excluding]


## 1 - READ A BLOCK-ASSIGNMENT FILE ###

plan_path: str = os.path.expanduser(f"{data_dir}/{plan_file}")
plan = read_csv(plan_path, [str, int])

### 2 - INVERT THE PLAN & INDEX IT BY GEOID ###

inverted_plan: defaultdict[int | str, set[str]] = defaultdict(set)
for row in plan:
    geoid: str = row["GEOID20"]  # Your field names may vary
    district: int = row["District"]  # Your field names may vary
    inverted_plan[district].add(geoid)

assignments_by_block: dict[str, int | str] = {
    row["GEOID20"]: row["District"] for row in plan
}

### 3 - READ or CONSTRUCT AN ADJACENCY GRAPH ###

# Read the adjacency graph from a file:
contiguity_path: str = os.path.expanduser(f"{data_dir}/{contiguity_file}")
adjacencies: dict[str, list[str]] = read_json(contiguity_path)

# Or construct one from a shapefile:
shapes_path: str = os.path.expanduser(f"{data_dir}/{shapes_file}")
g: Graph = Graph(shapes_path, id_field="GEOID20")
adjacencies: dict[str, list[str]] = g.data()

### 4 - CHECK CONTIGUITY & EMBEDDEDNESS ###

contiguity_by_district: dict[int | str, bool] = {}
for id, geos in inverted_plan.items():
    connected: bool = is_connected(list(geos), adjacencies)

    contiguity_by_district[id] = connected

not_embedded_by_district: dict[int | str, bool] = {}
for id, geos in inverted_plan.items():
    not_embedded: bool = not is_embedded(
        id, assignments_by_block, inverted_plan, adjacencies
    )
    not_embedded_by_district[id] = not_embedded

### 5 - PRINT THE RESULTS ###

print(f"Contiguous:")
for id, connected in sorted(contiguity_by_district.items()):
    print(f"- District {id}: {connected}")

print()

print(f"Not embedded:")
for id, not_embedded in sorted(not_embedded_by_district.items()):
    print(f"- District {id}: {not_embedded}")

### END ###
