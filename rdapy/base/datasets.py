"""
DATASET UTILTIES
"""

from typing import Any, Dict, List, TypeAlias, Literal

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

    # # HACK for legacy tests
    # if "version" not in metadata or metadata["version"] < 2:
    #     return [get_dataset(metadata, dataset_type)]

    return metadata[dataset_type]["datasets"]


def get_fields(
    metadata: Dict[str, Any], dataset_type: str, dataset: str = "default"
) -> Dict[str, str]:
    """Return the field mapping for a dataset type."""

    # Field names are prefixed with the dataset name
    fields: Dict[str, str] = {
        k: f"{dataset}_{v}" for k, v in metadata[dataset_type]["fields"].items()
    }
    # if "version" not in metadata or metadata["version"] < 2:
    #     # Legacy/v1 field names are fully specified
    #     fields = metadata[dataset_type]["fields"]
    # else:
    #     # v2+ field names are prefixed with the dataset name
    #     fields = {
    #         k: f"{dataset}_{v}" for k, v in metadata[dataset_type]["fields"].items()
    #     }

    return fields


def dataset_key(datasets: Dict[str, str], dataset_type: str) -> str:
    """Return the key for a dataset type."""

    assert dataset_type in datasets

    dataset_key: str = datasets[dataset_type] if datasets[dataset_type] else "default"

    return dataset_key


### END ###
