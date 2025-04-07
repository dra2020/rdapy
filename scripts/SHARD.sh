#!/bin/bash

# For example:
# scripts/SHARD.sh \
# --shard 100 \
# --output ~/'temp/NC20C_plans_{shard:02d}.jsonl'

# Function to print usage
usage() {
    echo "Usage: $0 --shard <number> --output <file pattern>"
    exit 1
}

HPC=false

# Initialize variables
shard=""
compressed=""

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --shard)
            shard="$2"
            shift 2
            ;;
        --output)
            output="$2"
            shift 2
            ;;
        --hpc)
            HPC=true
            shift
            ;;
        *)
            echo "Unknown argument: $1"
            usage
            ;;
    esac
done

# Check if all required arguments are provided
if [[ -z "$shard" ]] || [[ -z "$output" ]]; then
    echo "Error: All arguments are required"
    usage
fi

exe_path=bin/distill
if $HPC; then
    exe_path=$HOME/rdatools/bin/distill-x86_64-linux
fi

echo "Sharding ($compressed) to ($output)"

# Creating shard files from xz compressed file
$exe_path \
    --from compress \
    --to assignment \
    --shard $shard \
    --output $output

### END ###