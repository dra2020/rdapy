---
layout: page
title: Data Maps
permalink: data-maps/
---

TODO - FINISH THIS.

The `extract_data.py` script takes a `geojson` and a `data-map` as arguments.

```bash
scripts/extract_data.py \
--geojson path/to/DRA.geojson \
--data-map path/to/data_map.json \
--graph path/to/adjacency_graph.json \
--data path/to/input_data.jsonl
```

The `geosjson` is a DRA GeoJSON file that contains many different datasets for each precinct.
A `data-map` is a JSON file that specifies what data to extract data from the GeoJSON file, and
how to map it to fields that the scoring tools expect.

An example data map for North Carolina is below.

* There are four types of data in the 
* Datasets
* Fields
* Election data


```
{
    "version": 3,
    "source": "path/to/DRA/geojsons/",
    "path": "NC.geojson",
    "geoid": "id",
    "census": {
        "fields": {
            "total_pop": "Tot"
        },
        "datasets": [
            "D20F"
        ]
    },
    "vap": {
        "fields": {
            "total_vap": "Tot",
            "white_vap": "Wh",
            "hispanic_vap": "His",
            "black_vap": "BlC",
            "native_vap": "NatC",
            "asian_vap": "AsnC",
            "pacific_vap": "PacC",
            "minority_vap": "Min_derived"
        },
        "datasets": [
            "D20T"
        ]
    },
    "cvap": {
        "fields": {
            "total_cvap": "Tot",
            "white_cvap": "Wh",
            "hispanic_cvap": "His",
            "black_cvap": "BlC",
            "native_cvap": "NatC",
            "asian_cvap": "AsnC",
            "pacific_cvap": "PacC",
            "minority_cvap": "Min_derived"
        },
        "datasets": [
            "D20TACS"
        ]
    },
    "election": {
        "fields": {
            "tot_votes": "Tot",
            "dem_votes": "D",
            "rep_votes": "R"
        },
        "datasets": [
            "C16GCO",
            "E20GPR",
            "E20GGO",
            "E20GSE",
            "E16GPR",
            "E20GAG",
            "E16GSE"
        ]
    },
    "shapes": {
        "fields": {
            "geometry": "geometry"
        },
        "datasets": [
            "DRA_simplified_shapes"
        ]
    }
}
```