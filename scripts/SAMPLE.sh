#!/bin/bash

# For example:
# cat input.txt | scripts/SAMPLE.sh -k 100 | grep "pattern"

# Default sample rate
SAMPLE_RATE=100

# Function to display usage
usage() {
    echo "Usage: $0 [-k sample_rate]" >&2
    echo "Sample every kth line from stdin" >&2
    echo "  -k: sample rate (default: 100)" >&2
    echo "  -h: display this help message" >&2
    exit 1
}

# Process command line options
while getopts "k:h" opt; do
    case $opt in
        k)
            SAMPLE_RATE=$OPTARG
            # Validate that sample rate is a positive integer
            if ! [[ "$SAMPLE_RATE" =~ ^[0-9]+$ ]] || [ "$SAMPLE_RATE" -lt 1 ]; then
                echo "Error: Sample rate must be a positive integer" >&2
                exit 1
            fi
            ;;
        h)
            usage
            ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            usage
            ;;
    esac
done

# Shift the options out of the argument list
shift $((OPTIND-1))

# Sample every kth line from stdin
perl -ne "print if \$. % ${SAMPLE_RATE} == 0"
# awk "NR % ${SAMPLE_RATE} == 0"

### END ###