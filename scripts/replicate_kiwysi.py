#!/usr/bin/env python3

"""
Run this code to replicate the KIWYSI compactness model against the sample shapes.
"""


from rdapy.compactness import *
from testutils import *

INDEX: int = 0
VALUE: int = 1


def kiwysi_rank_shapes(sample_shapes, predictions, geodesic=True):
    print()
    print("Predicted compactness scores (for shapes):")
    print("-" * 64)
    for i in range(len(sample_shapes)):
        shp = sample_shapes[i][VALUE]
        calc = kiwysi_rank_shape(shp, geodesic=geodesic, revised=False)
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
        calc = score_features(featureized_shapes[i][VALUE], revised=False)
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


def main() -> None:
    """
    Generate the report
    """

    # Load the sample shapes and the features derived from them
    sample_shapes_shp = "testdata/compactness/first20"
    source_shapes, _ = load_shapes(sample_shapes_shp)

    sample_features_csv = "testdata/compactness/first20/smartfeats_first20.csv"
    featureized_shapes, predictions = load_features(sample_features_csv)

    # Replicate predicted compactness scores from feature-ized sample shapes
    score_featureized_shapes(featureized_shapes, predictions)

    # Replicate feature-ization of sample shapes (geodesic calcs)
    featureize_shapes(source_shapes, featureized_shapes)

    # Replicate predicted compactness scores from sample shapes
    kiwysi_rank_shapes(source_shapes, predictions)


if __name__ == "__main__":
    main()

### END ###
