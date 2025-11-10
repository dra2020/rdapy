"""
DATASET UTILTIES
"""

from typing import Any, Dict, List, Tuple, TypeAlias, Literal

Metric: TypeAlias = str
Aggregate: TypeAlias = List[int | float]
NamedAggregates: TypeAlias = Dict[Metric, Any]
Datasets: TypeAlias = Dict[str, List[str]]
DatasetKey: TypeAlias = str
DatasetType = Literal["census", "vap", "cvap", "election", "shapes"]
Aggregates: TypeAlias = Dict[DatasetType, Dict[DatasetKey, NamedAggregates]]


def get_dataset(metadata: Dict[str, Any], dataset_type: str) -> DatasetKey:
    """Return the first dataset for a dataset type. Some legacy logic."""

    dataset: DatasetKey = "default" if dataset_type != "cvap" else "N/A"
    if dataset_type in metadata and metadata[dataset_type]["datasets"][0] != "":
        dataset = metadata[dataset_type]["datasets"][0]

    return dataset


def get_datasets(metadata: Dict[str, Any], dataset_type: str) -> List[DatasetKey]:
    """Return all datasets for a dataset type."""

    assert dataset_type in metadata

    # HACK for legacy tests
    if "version" not in metadata or metadata["version"] == "1":
        return [get_dataset(metadata, dataset_type)]

    return metadata[dataset_type]["datasets"]


def get_fields(
    metadata: Dict[str, Any], dataset_type: str, dataset: str = "default"
) -> Dict[str, str]:
    """Return the field mapping for a dataset type."""

    if "version" not in metadata or metadata["version"] == "1":
        # HACK for legacy tests -- field names are fully specified
        fields = metadata[dataset_type]["fields"]
    else:
        # Field names are prefixed with the dataset name
        fields = {
            k: f"{dataset}_{v}" for k, v in metadata[dataset_type]["fields"].items()
        }

    return fields


def dataset_key(datasets: Dict[str, str], dataset_type: str) -> str:
    """Return the key for a dataset type."""

    assert dataset_type in datasets

    dataset_key: str = datasets[dataset_type] if datasets[dataset_type] else "default"

    return dataset_key


def get_dataset_keys(
    data_metadata: Dict[str, Any],
) -> Tuple[DatasetKey, DatasetKey, DatasetKey, List[DatasetKey]]:

    census_dataset: DatasetKey = get_dataset(data_metadata, "census")
    vap_dataset: DatasetKey = get_dataset(data_metadata, "vap")
    cvap_dataset: DatasetKey = get_dataset(data_metadata, "cvap")
    election_datasets: List[DatasetKey] = get_datasets(data_metadata, "election")

    return census_dataset, vap_dataset, cvap_dataset, election_datasets


### END ###
