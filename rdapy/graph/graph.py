#!/usr/bin/env python3

"""
ADJACENCY/CONTIGUITY GRAPHS
"""

import os

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

from typing import Any, Optional, Iterable

from .constants import *


class Graph:
    """NOTE: Cloned from the baseline repo & cut down, to show how to make a graph from a shapefile."""

    _data: dict
    _adjacencies: set[tuple[str, str]]

    def __init__(self, input: str | dict, id_field: str = "") -> None:
        if isinstance(input, dict):
            self._data = input
            return

        if isinstance(input, str):
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
            return

        raise TypeError("Input must be a string or a dict")

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
                        shp: Point | MultiPoint | LineString | MultiLineString | Polygon | MultiPolygon | LinearRing | GeometryCollection = shape(
                            item["geometry"]
                        )

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


### END ###
