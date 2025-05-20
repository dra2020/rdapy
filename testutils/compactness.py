"""
KIWYSI READ HELPERS
"""

import csv

from shapely.geometry import shape
import fiona


def load_features(samples_csv):
    # Initialize a lists of samples & predictions
    samples = []
    predictions = []

    with open(samples_csv) as f_input:
        csv_file = csv.DictReader(f_input)

        # Number of features
        n = 7

        # Process each row in the .csv file
        for row in csv_file:
            values = list(row.values())

            sample_id = int(values[0])

            sample = [float(x) for x in values[1 : (n + 1)]]
            samples.append((sample_id, sample))

            prediction = float(values[n + 1])
            predictions.append((sample_id, prediction))

    return samples, predictions


def load_shapes(shp_file: str, id: str = "OBJECTID"):
    shapes_by_id = []
    with fiona.Env():
        with fiona.open(shp_file) as source:
            meta = source.meta
            for item in source:
                obj_id = item["properties"][id]
                shp = shape(item["geometry"])
                shapes_by_id.append((obj_id, shp))

    return shapes_by_id, meta


# DON'T LIMIT WHAT GETS EXPORTED

### END ###
