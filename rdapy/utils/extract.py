"""
HELPERS FOR EXTRACTING DATA FROM GEOJSON FILES
"""

from typing import Any, List, Dict, Tuple

from geopandas import GeoDataFrame
from shapely.geometry import (
    shape,
    Polygon,
    MultiPolygon,
    Point,
)

from ..graph import OUT_OF_STATE

# TODO - Consolidate this into constants.py
OUT_OF_STATE_THRESHOLD: float = 1.0e-12


def index_shapes(gdf: GeoDataFrame, geoid_field: str = "id") -> Dict[
    str,
    Polygon | MultiPolygon,
]:
    """Index the shapes by the geoid."""

    shapes_by_id: Dict[
        str,
        Polygon | MultiPolygon,
    ] = dict()

    for i, row in gdf.iterrows():
        geoid: str = getattr(row, geoid_field)
        shp: Polygon | MultiPolygon = shape(row["geometry"])  # type: ignore

        shapes_by_id[geoid] = shp

    return shapes_by_id


def abstract_data(feature, data_map: Dict[str, Any]) -> Dict[str, Any]:
    """Abstract the census, demographic, election, and shape data from a GeoJSON feature"""

    data_abstract: Dict[str, Any] = dict()

    qualified_field: str
    for dataset_type in ["census", "vap", "cvap", "election", "shapes"]:
        datasets: List[str] = data_map[dataset_type]["datasets"]
        for dataset in datasets:
            match dataset_type:
                case "shapes":
                    field: str = "geometry"
                    qualified_field = f"{field}"
                    data_abstract[qualified_field] = feature[
                        data_map["shapes"]["fields"][field]
                    ]
                case "census" | "vap" | "cvap" | "election":
                    fields: Dict[str, str] = data_map[dataset_type]["fields"].copy()

                    # Handle VAP_NH special case
                    if dataset_type == "vap" and dataset.endswith("VAP_NH"):
                        for k, v in fields.items():
                            if k in [
                                "black_vap",
                                "asian_vap",
                                "pacific_vap",
                                "native_vap",
                            ]:
                                fields[k] = v + "Alone"
                        pass  # for debugging
                    ###

                    i: int = 0
                    j: int = 0
                    for k, v in fields.items():
                        if dataset_type == "vap" and k == "minority_vap":
                            continue
                        if dataset_type == "cvap" and k == "minority_cvap":
                            continue
                        i += 1
                        qualified_field = f"{dataset}_{v}"
                        data_abstract[qualified_field] = 0  # Guard against missing data
                        if dataset in feature["properties"]["datasets"]:
                            data_abstract[qualified_field] = feature["properties"][
                                "datasets"
                            ][dataset][v]
                        else:
                            j += 1
                            id: str = feature["properties"]["id"]
                            print(
                                f"WARNING: Dataset {dataset} not in feature {id}'s properties! {j} of {i}"
                            )

                    if dataset_type == "vap" or dataset_type == "cvap":
                        minority_field: str = f"minority_{dataset_type}"
                        total_field: str = f"total_{dataset_type}"
                        white_field: str = f"white_{dataset_type}"
                        qualified_field = f"{dataset}_{fields[minority_field]}"
                        total: int = data_abstract[f"{dataset}_{fields[total_field]}"]
                        white: int = data_abstract[f"{dataset}_{fields[white_field]}"]
                        minority: int = total - white
                        data_abstract[qualified_field] = minority
                case _:
                    raise ValueError(f"Unknown dataset type: {dataset_type}")

    return data_abstract


def abstract_shape(
    shp_by_geoid: Dict[str, Polygon | MultiPolygon],
    neighbors_by_geoid: Dict[str, Any],
    geoid: str,
    shp: Polygon | MultiPolygon,
) -> Dict[str, Any]:
    """Abstract the shape"""

    center: Tuple[float, float] = find_center(shp)
    area: float = shp.area

    arcs: Dict[str, float] = dict()  # The shared border lengths by neighbor
    neighbors: List[str] = neighbors_by_geoid[geoid]
    perimeter: float = shp.length
    total_shared_border: float = 0.0

    for neighbor in neighbors:
        if neighbor == OUT_OF_STATE:
            continue
        if neighbor not in shp_by_geoid:
            print(f"WARNING: {neighbor} not in shapes by geoid!")
            continue

        neighbor_shp: Polygon | MultiPolygon = shp_by_geoid[neighbor]

        shared_edge = shp.intersection(neighbor_shp)
        shared_border: float = shared_edge.length

        arcs[neighbor] = shared_border
        total_shared_border += shared_border

    remaining: float = perimeter - total_shared_border
    if remaining > OUT_OF_STATE_THRESHOLD:
        arcs[OUT_OF_STATE] = remaining

    ch = shp.convex_hull
    pts: List[Tuple[float, float]] = list(ch.exterior.coords)  # type: ignore

    shp_abstract: Dict[str, Any] = {
        "center": center,
        "area": area,
        "arcs": arcs,
        "exterior": pts,
    }

    return shp_abstract


def find_center(shp) -> Tuple[float, float]:
    """Get a centroid-like point guaranteed to be w/in the feature"""

    x: float = shp.centroid.x
    y: float = shp.centroid.y

    if not shp.contains(Point(x, y)):
        pt: Point = shp.representative_point()
        x: float = pt.x
        y: float = pt.y

    return x, y


### END ###
