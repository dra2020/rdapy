"""
AGGREGATE DATA BY DISTRICT
"""

from typing import Any, List, Dict, TypeAlias, Literal, Tuple, OrderedDict, TextIO

import json

from .utils import (
    District,
    GeoIDIndex,
    ParseGeoID,
    County,
    Graph,
    OUT_OF_STATE,
    is_water_only,
    approx_equal,
    collect_metadata,
)
from .smallestenclosingcircle import wl_make_circle

Metric: TypeAlias = str
Aggregate: TypeAlias = List[int | float]
NamedAggregates: TypeAlias = Dict[Metric, Any]
Datasets: TypeAlias = Dict[str, List[str]]
DatasetType = Literal["census", "vap", "cvap", "election", "shapes"]
DatasetKey: TypeAlias = str
Aggregates: TypeAlias = Dict[DatasetType, Dict[DatasetKey, NamedAggregates]]


# TODO - DELETE
# def aggregate_plans(
#     input_stream: TextIO,
#     state: str,
#     plan_type: str,
#     data_map: Dict[str, Any],
#     data: List[Dict[str, Any]],
#     graph: Dict[str, List[str]],
#     output_stream: TextIO,
#     mode="all",
#     *,
#     debug=False,
#     verbose: bool = False,
# ):
#     """
#     For each plan in the input stream, aggregate the districts and write the plan with aggregates to the output stream.
#     Plans can either be in _tag_'d format or simple dictionaries of geoid:district assignment pairs.
#     Pass through a metadata record.
#     """

#     geoids = [precinct["geoid"] for precinct in data]
#     metadata = collect_metadata(state, plan_type, geoids)

#     j = 0
#     for i, line in enumerate(input_stream):
#         # Parse the JSON string into a Python dictionary
#         parsed_line = json.loads(line)

#         # Process each input line (some of which may not be plans)
#         if "_tag_" not in parsed_line and is_flat_dict(parsed_line):
#             # Case 1: No "_tag_" key and simple dict - process the line as geoid:district pairs

#             j += 1
#             assignments = {str(k): int(v) for k, v in parsed_line.items()}
#             plan_with_aggs = aggregate_districts(
#                 assignments,
#                 data,
#                 graph,
#                 metadata,
#                 which=mode,
#                 data_metadata=data_map,
#             )
#             print(json.dumps(plan_with_aggs), file=output_stream)

#         elif "_tag_" in parsed_line and parsed_line["_tag_"] == "plan":
#             # Case 2: Has "_tag_" key with value "plan" - reset the plan to value of the "plan" key and process

#             j += 1
#             assignments = {str(k): int(v) for k, v in parsed_line["plan"].items()}
#             plan_with_aggs = aggregate_districts(
#                 assignments,
#                 data,
#                 graph,
#                 metadata,
#                 which=mode,
#                 data_metadata=data_map,
#             )
#             print(json.dumps(plan_with_aggs), file=output_stream)

#         elif "_tag_" in parsed_line and parsed_line["_tag_"] == "metadata":
#             # Case 3: Has "_tag_" key with value "metadata" - pass it along

#             print(json.dumps(parsed_line), file=output_stream)
#             continue

#         else:
#             # Case 4: Something else - skip the line, e.g., adjacency graph, etc.

#             continue

#         if j == 1:
#             break

#         pass


# def is_flat_dict(d: Dict[str, Any]) -> bool:
#     """
#     Determines whether a dictionary simply contains key:value pairs where values
#     are integers or strings, or whether it has a more complex hierarchical structure.

#     Args:
#         d: A dictionary object (parsed from JSON)

#     Returns:
#         bool: True if all values are integers or strings, False otherwise
#     """
#     for v in d.values():
#         if not (isinstance(v, int) or isinstance(v, str)):
#             return False

#     return True


### AGGREGATE DATA & SHAPES BY DISTRICT FOR ONE PLAN ###


def get_dataset(metadata: Dict[str, Any], dataset_type: str, i: int = 0) -> DatasetKey:
    dataset: DatasetKey = "default" if dataset_type != "cvap" else "N/A"
    if dataset_type in metadata and metadata[dataset_type]["datasets"][i] != "":
        dataset = metadata[dataset_type]["datasets"][i]

    # dataset: DatasetKey = (
    #     metadata[dataset_type]["datasets"][i]
    #     if metadata[dataset_type]["datasets"][i] != ""
    #     else "default"
    # )

    return dataset


def get_fields(
    metadata: Dict[str, Any], dataset_type: str, dataset: str = "default"
) -> Dict[str, str]:
    """Return the field mapping for a dataset type."""

    fields: Dict[str, str]

    if "version" not in metadata or metadata["version"] < 2:
        # Legacy/v1 field names are fully specified
        fields = metadata[dataset_type]["fields"]
    else:
        # v2+ field names are prefixed with the dataset name
        fields = {
            k: f"{dataset}_{v}" for k, v in metadata[dataset_type]["fields"].items()
        }

    return fields


def aggregate_districts(
    geoid_index: GeoIDIndex,
    data: List[Dict[str, Any]],
    graph: Graph,
    metadata: Dict[str, Any],
    *,
    which: str,
    data_metadata: Dict[str, Any],
) -> Aggregates:
    """Aggregate input data & shapes by district *for one set of datasets*."""

    assert which != "extended"  # Extended scoring moved out separately

    n_districts: int = metadata["D"]
    n_counties: int = metadata["C"]
    county_to_index: Dict[County, int] = metadata["county_to_index"]
    district_to_index: Dict[District, int] = metadata["district_to_index"]

    aggs: Aggregates = dict()

    if which == "all" or which != "compactness":
        data_aggregates: Aggregates = aggregate_data_by_district(
            geoid_index,
            data,
            n_districts,
            n_counties,
            county_to_index,
            district_to_index,
            which=which,
            data_metadata=data_metadata,
        )
        for type_, data_ in data_aggregates.items():
            aggs[type_] = data_

    if which == "all" or which == "compactness":
        geo_props: Aggregates = aggregate_shapes_by_district(
            geoid_index,
            data,
            graph,
            n_districts,
            which=which,
            data_metadata=data_metadata,
        )
        for type_, data_ in geo_props.items():
            aggs[type_] = data_

    return aggs


def aggregate_data_by_district(
    geoid_index: GeoIDIndex,
    data: List[Dict[str, Any]],
    n_districts: int,
    n_counties: int,
    county_to_index: Dict[County, int],
    district_to_index: Dict[District, int],
    *,
    which: str,
    data_metadata: Dict[str, Any],
    debug: bool = False,
) -> Aggregates:
    """
    Aggregate census & election data by district.

    NOTE - District values are 1-N. The 0th element is a total for the state, if applicable.
    """

    assert which != "compactness"

    census_dataset: DatasetKey = get_dataset(data_metadata, "census")
    vap_dataset: DatasetKey = get_dataset(data_metadata, "vap")
    cvap_dataset: DatasetKey = get_dataset(data_metadata, "cvap")
    # TODO - Enable multiple election datasets
    election_dataset: DatasetKey = get_dataset(data_metadata, "election")

    # Set up the aggregates

    pop_by_district: Aggregate = [0] * (n_districts + 1)
    dem_by_district: Aggregate = [0] * (n_districts + 1)
    tot_by_district: Aggregate = [0] * (n_districts + 1)
    vaps_by_district: Dict[str, List[int]] = {
        demo: [0] * (n_districts + 1)
        for demo in get_fields(data_metadata, "vap", vap_dataset)
    }
    cvaps_by_district: Dict[str, List[int]] = dict()
    if cvap_dataset != "N/A":
        cvaps_by_district = {
            demo: [0] * (n_districts + 1)
            for demo in get_fields(data_metadata, "cvap", cvap_dataset)
        }
    CxD: List[List[float]] = [[0.0] * n_counties for _ in range(n_districts)]

    # Aggregate the data

    for precinct in data:
        geoid: str = precinct["geoid"]
        pop: int = int(
            precinct[get_fields(data_metadata, "census", census_dataset)["total_pop"]]
        )
        if geoid not in geoid_index:
            if pop == 0:
                continue
            else:
                raise ValueError(f"Populated geoid ({geoid}) not in the plan!")
        district: int = geoid_index[geoid]

        # pop: int
        # if which in ["all", "general", "splitting"]:
        #     pop = int(
        #         precinct[
        #             get_fields(data_metadata, "census", census_dataset)["total_pop"]
        #         ]
        #     )

        if which in ["all", "general"]:
            pop_by_district[district] += pop
            pop_by_district[0] += pop

        if which in ["all", "partisan"]:
            dem: int = int(
                precinct[
                    get_fields(data_metadata, "election", election_dataset)["dem_votes"]
                ]
            )
            tot: int = int(
                precinct[
                    get_fields(data_metadata, "election", election_dataset)["dem_votes"]
                ]
            ) + int(
                precinct[
                    get_fields(data_metadata, "election", election_dataset)["rep_votes"]
                ]
            )
            dem_by_district[district] += dem
            dem_by_district[0] += dem
            tot_by_district[district] += tot
            tot_by_district[0] += tot

        if which in ["all", "minority"]:
            # for dem's' in vap & cvap fields:
            for demo, field in get_fields(data_metadata, "vap", vap_dataset).items():
                demo_tot: int = int(precinct[field])
                vaps_by_district[demo][district] += demo_tot
                vaps_by_district[demo][0] += demo_tot

            if cvap_dataset != "N/A":
                for demo, field in get_fields(
                    data_metadata, "cvap", cvap_dataset
                ).items():
                    demo_tot: int = int(precinct[field])
                    cvaps_by_district[demo][district] += demo_tot
                    cvaps_by_district[demo][0] += demo_tot

        if which in ["all", "splitting"]:
            county: str = ParseGeoID(geoid).county[2:]
            i: int = district_to_index[district]
            j: int = county_to_index[county]
            CxD[i][j] += pop

    # Compose the aggregates bound to the dataset keys

    aggs: Aggregates = dict()
    dataset: DatasetKey

    if which in ["all", "general", "splitting"]:
        aggs["census"] = {census_dataset: {}}

        if which in ["all", "general"]:
            aggs["census"][census_dataset].update({"pop_by_district": pop_by_district})

        if which in ["all", "splitting"]:
            aggs["census"][census_dataset].update({"CxD": CxD})

    if which in ["all", "partisan"]:
        aggs["election"] = {election_dataset: {}}
        aggs["election"][election_dataset].update(
            {
                "dem_by_district": dem_by_district,
                "tot_by_district": tot_by_district,
            }
        )

    if which in ["all", "minority"]:
        aggs["vap"] = {vap_dataset: {}}
        aggs["vap"][vap_dataset].update(vaps_by_district)
        if cvap_dataset != "N/A":
            aggs["cvap"] = {cvap_dataset: {}}
            aggs["cvap"][cvap_dataset].update(cvaps_by_district)

    return aggs


def aggregate_shapes_by_district(
    geoid_index: GeoIDIndex,
    data: List[Dict[str, Any]],
    graph: Dict[str, List[str]],
    n_districts: int,
    *,
    which: str,
    data_metadata: Dict[str, Any],
    debug: bool = False,
) -> Aggregates:
    """Aggregate shape data by district for compactness calculations."""

    assert which == "all" or which == "compactness"

    data_by_geoid: Dict[str, Any] = {precinct["geoid"]: precinct for precinct in data}

    if debug:
        arcs_are_symmetric(data_by_geoid)

    # TODO - Enable multiple datasets per type
    shapes_dataset: DatasetKey = get_dataset(data_metadata, "shapes")
    census_dataset: DatasetKey = get_dataset(data_metadata, "census")

    # Set up aggregates

    by_district: Dict[str, List[float]] = {
        "area": [0.0] * (n_districts + 1),
        "perimeter": [0.0] * (n_districts + 1),
        "diameter": [0.0] * (n_districts + 1),
    }  # The 0th element is a total for the state, if applicable
    by_district_temp: Dict[str, List[Any]] = {
        "exterior": [[] for _ in range(n_districts + 1)]
    }

    # Aggregate the shape properties

    for precinct in data:
        geoid: str = precinct["geoid"]
        pop: int = int(
            precinct[get_fields(data_metadata, "census", census_dataset)["total_pop"]]
        )
        if geoid not in geoid_index:
            if pop == 0:
                continue
            else:
                raise ValueError(f"Populated geoid ({geoid}) not in the plan!")
        district: int = geoid_index[geoid]

        by_district["area"][district] += precinct["area"]
        by_district["area"][0] += precinct["area"]
        by_district["perimeter"][district] += border_length(
            geoid, district, geoid_index, data_by_geoid, graph
        )
        by_district_temp["exterior"][district].extend(
            exterior(geoid, district, geoid_index, data_by_geoid, graph)
        )

    # for geoid, district in geoid_index.items():
    #     by_district["area"][district] += data[geoid]["area"]
    #     by_district["area"][0] += data[geoid]["area"]
    #     by_district["perimeter"][district] += border_length(
    #         geoid, district, geoid_index, data, graph
    #     )
    #     by_district_temp["exterior"][district].extend(
    #         exterior(geoid, district, geoid_index, data, graph)
    #     )

    # Calculate district diameters

    for i, ext in enumerate(by_district_temp["exterior"]):
        if i == 0:
            continue  # Skip the state total

        _, _, r = wl_make_circle(ext)
        diameter: float = 2 * r

        by_district["diameter"][i] = diameter

    # Compose the aggregates bound to the dataset keys

    aggs: Aggregates = dict()
    aggs["shapes"] = {shapes_dataset: {}}
    aggs["shapes"][shapes_dataset].update(by_district)

    return aggs


def border_length(
    geoid: str,
    district: int,
    geoid_index: GeoIDIndex,
    data_by_geoid: Dict[str, Any],
    graph: Dict[str, List[str]],
) -> float:
    """Sum the length of the border with other districts or the state border."""

    arc_length: float = 0.0

    for n in graph[geoid]:
        if n == OUT_OF_STATE:
            if n in data_by_geoid[geoid]["arcs"]:
                arc_length += data_by_geoid[geoid]["arcs"][n]
        elif is_water_only(n) and (
            n not in geoid_index
        ):  # elif (n in OTHER_POTENTIAL_BORDERS) and (n not in geoid_index):
            if n in data_by_geoid[geoid]["arcs"]:
                arc_length += data_by_geoid[geoid]["arcs"][n]
        elif geoid_index[n] != district:
            arc_length += data_by_geoid[geoid]["arcs"][n]

    return arc_length


def exterior(
    geoid: str,
    district: int,
    geoid_index: GeoIDIndex,
    data_by_geoid: Dict[str, Any],
    graph: Dict[str, List[str]],
) -> list:
    """points on exterior of district(-ish)"""

    ext = []

    for n in graph[geoid]:
        if n == OUT_OF_STATE:
            if n in data_by_geoid[geoid]["arcs"]:
                ext.extend(data_by_geoid[geoid]["exterior"])
        elif is_water_only(n) and (
            n not in geoid_index
        ):  # elif (n in OTHER_POTENTIAL_BORDERS) and (n not in geoid_index):
            if n in data_by_geoid[geoid]["arcs"]:
                ext.extend(data_by_geoid[geoid]["exterior"])
        elif geoid_index[n] != district:
            ext.extend(data_by_geoid[geoid]["exterior"])

    return ext


def arcs_are_symmetric(data_by_geoid: Dict[str, Any]) -> bool:
    symmetric: bool = True
    narcs: int = 0
    nasymmetric: int = 0

    for from_geoid, abstract in data_by_geoid.items():
        for to_geoid, from_border in abstract["arcs"].items():
            if to_geoid != "OUT_OF_STATE":
                narcs += 1
                to_border = data_by_geoid[to_geoid]["arcs"][from_geoid]
                if not approx_equal(from_border, to_border, places=4):
                    symmetric = False
                    nasymmetric += 1
                    print(
                        f"Arcs between {from_geoid} & {to_geoid} are not symmetric: {from_border} & {to_border}."
                    )

    if not symmetric:
        print(f"Total arcs: {narcs}, non-symmetric arcs: {nasymmetric}")

    return symmetric


def dataset_key(datasets: Dict[str, str], dataset_type: str) -> str:
    """Return the key for a dataset type."""

    assert dataset_type in datasets

    dataset_key: str = datasets[dataset_type] if datasets[dataset_type] else "default"

    return dataset_key


### END ###
