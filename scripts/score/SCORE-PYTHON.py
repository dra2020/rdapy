#!/usr/bin/env python3

"""
This is a Python implementation of SCORE.sh which is a *nix shell script.
This should run on Windows.

Call it with the same arguments, e.g.:

$ scripts/score/SCORE-PYTHON.py \
--state NC \
--plan-type congress \
--geojson /dir/for/unzipped/files/NC_2020_VD_tabblock.vtd.datasets.geojson \
--graph /dir/for/unzipped/files/NC_2020_graph.json \
--precomputed testdata/examples/NC_congress_precomputed.json \
--plans testdata/plans/NC_congress_plans.tagged.jsonl \
--scores /path/to/TEST_scores.csv \
--by-district /path/to/TEST_by-district.jsonl

"""

import argparse
import os
import sys
import tempfile
import subprocess


def main():
    # Default values
    default_values = {
        "geojson": "",
        "graph": "",
        "precomputed": "",
        "plans": "",
        "scores": "",
        "by_district": "",
        "mode": "all",
        "census": "T_20_CENS",
        "vap": "V_20_VAP",
        "cvap": "V_20_CVAP",
        "elections": "E_16-20_COMP",
        "expand_composites": False,
        "prefixes": False,
    }

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Score redistricting plans")
    parser.add_argument("--state", type=str, help="State abbreviation")
    parser.add_argument("--plan-type", type=str, help="Plan type (chamber)")
    parser.add_argument("--geojson", type=str, help="Path to GeoJSON file")
    parser.add_argument("--graph", type=str, help="Path to graph file")
    parser.add_argument(
        "--precomputed", type=str, help="Path to precomputed data (optional)"
    )
    parser.add_argument("--plans", type=str, help="Path to plans file")
    parser.add_argument("--scores", type=str, help="Path to scores output file")
    parser.add_argument(
        "--by-district", type=str, help="Path to by-district output file"
    )
    parser.add_argument(
        "--mode",
        type=str,
        default=default_values["mode"],
        help="Analysis mode (default: all)",
    )
    parser.add_argument(
        "--census",
        type=str,
        default=default_values["census"],
        help="Census data to use (default: T_20_CENS)",
    )
    parser.add_argument(
        "--vap",
        type=str,
        default=default_values["vap"],
        help="Voting age population data to use (default: V_20_VAP)",
    )
    parser.add_argument(
        "--cvap",
        type=str,
        default=default_values["cvap"],
        help="Citizen voting age population data to use (default: V_20_CVAP)",
    )
    parser.add_argument(
        "--elections",
        type=str,
        default=default_values["elections"],
        help="Election data to use (default: E_16-20_COMP)",
    )
    parser.add_argument(
        "--expand-composites", action="store_true", help="Expand composite elections"
    )
    parser.add_argument("--prefixes", action="store_true", help="Use prefixes")

    args = parser.parse_args()

    # Check if all required arguments are provided
    required_args = [
        "state",
        "plan_type",
        "geojson",
        "graph",
        "plans",
        "scores",
        "by_district",
    ]
    missing_args = [arg for arg in required_args if not getattr(args, arg)]

    if missing_args:
        print("Error: Missing required arguments")
        print(
            "Usage: score_script.py --state <xx> --plan-type <chamber> --geojson <path> --graph <path> "
            "--plans <path> --scores <path> --by-district <path>"
        )
        print("Optional arguments:")
        print("  --precomputed <path>  Path to precomputed data (optional)")
        print("  --mode <mode>         Analysis mode (default: all)")
        print("  --census <census>     Census data to use (default: T_20_CENS)")
        print(
            "  --vap <vap>           Voting age population data to use (default: V_20_VAP)"
        )
        print(
            "  --cvap <cvap>         Citizen voting age population data to use (default: V_20_CVAP)"
        )
        print("  --elections <elec>    Election data to use (default: E_16-20_COMP)")
        sys.exit(1)

    # Validate the mode argument
    valid_modes = ["all", "general", "partisan", "minority", "compactness", "splitting"]
    if args.mode not in valid_modes:
        print(
            f"Error: Invalid mode '{args.mode}'. Must be one of: {', '.join(valid_modes)}"
        )
        sys.exit(1)

    # Create temporary files
    temp_data_map = tempfile.mktemp(prefix="data-map.", dir="/tmp")
    temp_data = tempfile.mktemp(prefix="data.", dir="/tmp")

    try:
        # Build command arguments
        precomputed_flag = (
            f"--precomputed {args.precomputed}" if args.precomputed else ""
        )
        expand_composites_flag = "--expand-composites" if args.expand_composites else ""
        prefixes_flag = "--prefixes" if args.prefixes else ""

        # Run map_scoring_data.py
        map_cmd = [
            "scripts/data/map_scoring_data.py",
            "--geojson",
            args.geojson,
            "--census",
            args.census,
            "--vap",
            args.vap,
            "--cvap",
            args.cvap,
            "--elections",
            args.elections,
            "--data-map",
            temp_data_map,
        ]
        if expand_composites_flag:
            map_cmd.append(expand_composites_flag)

        subprocess.run(map_cmd, check=True)

        # Run extract_data.py
        extract_cmd = [
            "scripts/data/extract_data.py",
            "--geojson",
            args.geojson,
            "--data-map",
            temp_data_map,
            "--graph",
            args.graph,
            "--data",
            temp_data,
        ]

        subprocess.run(extract_cmd, check=True)

        # Read plans file and pipe through the pipeline
        with open(args.plans, "r") as plans_file:
            # Run aggregate.py
            aggregate_cmd = [
                "scripts/score/aggregate.py",
                "--state",
                args.state,
                "--plan-type",
                args.plan_type,
                "--data",
                temp_data,
                "--graph",
                args.graph,
                "--mode",
                args.mode,
            ]

            agg_process = subprocess.Popen(
                aggregate_cmd, stdin=plans_file, stdout=subprocess.PIPE, text=True
            )

            # Run score.py
            score_cmd = [
                "scripts/score/score.py",
                "--state",
                args.state,
                "--plan-type",
                args.plan_type,
                "--data",
                temp_data,
                "--graph",
                args.graph,
                "--mode",
                args.mode,
            ]

            if precomputed_flag:
                score_cmd.extend(["--precomputed", args.precomputed])

            score_process = subprocess.Popen(
                score_cmd, stdin=agg_process.stdout, stdout=subprocess.PIPE, text=True
            )

            agg_process.stdout.close()  # Allow agg_process to receive SIGPIPE if score_process exits

            # Run write.py
            write_cmd = [
                "scripts/score/write.py",
                "--data",
                temp_data,
                "--scores",
                args.scores,
                "--by-district",
                args.by_district,
            ]

            if prefixes_flag:
                write_cmd.append(prefixes_flag)

            write_process = subprocess.run(
                write_cmd, stdin=score_process.stdout, text=True, check=True
            )

            score_process.stdout.close()

        print()
        print("Done!")
        print()

    finally:
        # Clean up temporary files
        for temp_file in [temp_data_map, temp_data]:
            try:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
            except Exception as e:
                print(f"Warning: Failed to remove temporary file {temp_file}: {e}")


if __name__ == "__main__":
    main()
