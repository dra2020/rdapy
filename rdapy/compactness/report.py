#!/usr/bin/env python3

"""
OUTPUT HELPERS
"""

import csv

from shapely.geometry import shape
import fiona

from .kiwysi import score_shape, score_features, featureize_shape

# CONSTANTS FOR SAMPLE TUPLES

INDEX = 0
VALUE = 1


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


def score_shapes(sample_shapes, predictions, geodesic=True):
    print()
    print("Predicted compactness scores (for shapes):")
    print("-" * 64)
    for i in range(len(sample_shapes)):
        shp = sample_shapes[i][VALUE]
        calc = score_shape(shp, geodesic)
        correct = predictions[i][VALUE]
        print(
            "Sample {:2} - Prediction = {:.2f}, Answer = {:.2f}, Delta % = {:>+6.1%}".format(
                i + 1, calc, correct, ((calc - correct) / correct)
            )
        )
    print()
    print()


def score_featureized_shapes(featureized_shapes, predictions):
    print()
    print("Predicted compactness scores (for features):")
    print("-" * 64)
    for i in range(len(featureized_shapes)):
        calc = score_features(featureized_shapes[i][VALUE])
        correct = predictions[i][VALUE]
        print(
            "Sample {:2} - Prediction = {:.2f}, Answer = {:.2f}, Delta % = {:>+6.1%}".format(
                i + 1, calc, correct, ((calc - correct) / correct)
            )
        )
    print()
    print()


def featureize_shapes(sample_shapes, featureized_shapes, geodesic=True):
    print()
    print("Computed features for shapes:")
    print()
    print(
        "{:<2} = {:<12} | {:<12} | {:<12} | {:<12} | {:<12} | {:<12} | {:<12}".format(
            "##", "sym_x", "sym_y", "reock", "bbox", "polsby", "hull", "schwartzberg"
        )
    )
    print("-" * 119)

    for i in range(len(sample_shapes)):
        sample_ix = sample_shapes[i][INDEX]
        shp = sample_shapes[i][VALUE]

        corrects = featureized_shapes[i][VALUE]
        calcs = featureize_shape(shp, geodesic)
        deltas = [(calcs[i] - corrects[i]) / corrects[i] for i in range(len(calcs))]

        print(
            "{:2} = {:.10f} | {:.10f} | {:.10f} | {:.10f} | {:.10f} | {:.10f} | {:.10f}".format(
                sample_ix,
                calcs[0],
                calcs[1],
                calcs[2],
                calcs[3],
                calcs[4],
                calcs[5],
                calcs[6],
            ),
            "<<< Calc'd",
        )
        print(
            "     {:.10f} | {:.10f} | {:.10f} | {:.10f} | {:.10f} | {:.10f} | {:.10f}".format(
                corrects[0],
                corrects[1],
                corrects[2],
                corrects[3],
                corrects[4],
                corrects[5],
                corrects[6],
            ),
            "    Correct",
        )
        print(
            "     {:<+10.1%}   | {:<+10.1%}   | {:<+10.1%}   | {:<+10.1%}   | {:<+10.1%}   | {:<+10.1%}   | {:<+10.1%}   ".format(
                deltas[0],
                deltas[1],
                deltas[2],
                deltas[3],
                deltas[4],
                deltas[5],
                deltas[6],
            ),
            "   Delta %",
        )
        print("-" * 119)
    print()
    print()


# END


# DON'T LIMIT WHAT GETS EXPORTED
