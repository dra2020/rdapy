#!/usr/bin/env python3

"""
Compute statistics on delta values for reverse weighted county splitting.
"""

import os
import pandas as pd
import numpy as np
from pathlib import Path


def process_csv_files(directory):
    """
    Process all CSV files in a directory and calculate statistics.

    Args:
        directory: Path to directory containing CSV files
    """
    # Get all CSV files in the directory
    csv_files = list(Path(directory).glob("*.csv"))

    if not csv_files:
        print(f"No CSV files found in {directory}")
        return

    # Store results for all files
    results = []

    for csv_file in csv_files:
        # Read the CSV file
        df = pd.read_csv(csv_file)

        # Calculate the two new columns
        df["raw_delta"] = df["county_splitting_reverse"] - df["county_splitting"]
        df["rating_delta"] = df["splitting_reverse"] - df["splitting"]

        # Calculate statistics for both columns in one row
        stats = {
            "file": csv_file.name,
            "raw_mean": df["raw_delta"].mean(),
            "raw_median": df["raw_delta"].median(),
            "raw_min": df["raw_delta"].min(),
            "raw_max": df["raw_delta"].max(),
            "raw_std": df["raw_delta"].std(),
            "rating_mean": df["rating_delta"].mean(),
            "rating_median": df["rating_delta"].median(),
            "rating_min": df["rating_delta"].min(),
            "rating_max": df["rating_delta"].max(),
            "rating_std": df["rating_delta"].std(),
        }

        results.append(stats)

    # Create DataFrame from results
    results_df = pd.DataFrame(results)

    # Format the columns
    raw_columns = ["raw_mean", "raw_median", "raw_min", "raw_max", "raw_std"]
    rating_columns = [
        "rating_mean",
        "rating_median",
        "rating_min",
        "rating_max",
        "rating_std",
    ]

    for col in raw_columns:
        results_df[col] = results_df[col].apply(lambda x: f"{x:.4f}")

    for col in rating_columns:
        results_df[col] = results_df[col].apply(lambda x: f"{x:.1f}")

    # Print the results table with grouped headers
    print("\nStatistics by File:")
    print("=" * 140)

    # Print group headers (centered over "min" column, which is the 3rd column in each group)
    print(
        f"{'file':<30} {'':<10} {'':<10} {'Raw':^10} {'':<10} {'':<10} {'':<10} {'':<10} {'Rating':^10} {'':<10} {'':<10}"
    )
    print(
        f"{'':<30} {'mean':>10} {'median':>10} {'min':>10} {'max':>10} {'std':>10} {'mean':>10} {'median':>10} {'min':>10} {'max':>10} {'std':>10}"
    )
    print("-" * 140)

    # Print data rows
    for _, row in results_df.iterrows():
        print(
            f"{row['file']:<30} {row['raw_mean']:>10} {row['raw_median']:>10} {row['raw_min']:>10} {row['raw_max']:>10} {row['raw_std']:>10} {row['rating_mean']:>10} {row['rating_median']:>10} {row['rating_min']:>10} {row['rating_max']:>10} {row['rating_std']:>10}"
        )

    print("=" * 140)


if __name__ == "__main__":
    # # Specify your directory path here
    # directory_path = "~/local/reverse-weighting"

    # You can also accept it as a command line argument
    import sys

    if len(sys.argv) > 1:
        directory_path = sys.argv[1]

    process_csv_files(directory_path)

### END ###
