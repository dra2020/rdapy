#!/bin/bash

# scripts/SHARD.sh /path/to/plans.jsonl
# 
# Shards a JSONL file of redistricting plans in tagged format into multiple smaller files
# so scoring can be done in parallel.
#
# For the above example, ten shards (the default) are created in '/tmp'. They have the
# same base name as the input file, with a series of two-digit suffixes (00, 01, 02, etc.).

# Examples:
# scripts/SHARD.sh /path/to/plans.jsonl --shards 5
# scripts/SHARD.sh /path/to/plans.jsonl --output /path/to/output/dir
# scripts/SHARD.sh /path/to/plans.jsonl --shards 5 --output /path/to/output/dir

# Function to display usage information
function show_usage {
    echo "Usage: $0 <jsonl_file> [--shards <nshards>] [--output <output>]"
    echo "  <jsonl_file>        : Path to JSONL file containing redistricting plans"
    echo "  -s|--shards <nshards>: Number of shards (default: 10, min: 2, max: 100)"
    echo "  -d|--output <output>   : Output outputectory (default: /tmp)"
    exit 1
}

# Check if at least one argument is provided
if [ $# -lt 1 ]; then
    show_usage
fi

# Get the JSONL file path (first positional argument)
jsonl_file="$1"
shift

# Initialize default values
nshards=10
output="/tmp"

# Process remaining arguments (keyword arguments)
while [[ $# -gt 0 ]]; do
    case "$1" in
        --shards)
            nshards="$2"
            shift 2
            ;;
        --output)
            output="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            show_usage
            ;;
    esac
done

# Validate the JSONL file exists
if [ ! -f "$jsonl_file" ]; then
    echo "Error: JSONL file '$jsonl_file' not found"
    exit 1
fi

# Validate the number of shards
if ! [[ "$nshards" =~ ^[0-9]+$ ]]; then
    echo "Error: Number of shards must be an integer"
    exit 1
fi

if [ "$nshards" -lt 2 ]; then
    echo "Warning: Number of shards too small. Setting to minimum value (2)"
    nshards=2
fi

if [ "$nshards" -gt 100 ]; then
    echo "Warning: Number of shards too large. Setting to maximum value (100)"
    nshards=100
fi

# Validate the output outputectory exists or create it
if [ ! -d "$output" ]; then
    echo "Output outputectory '$output' does not exist. Creating it..."
    mkoutput -p "$output"
    if [ $? -ne 0 ]; then
        echo "Error: Failed to create output outputectory '$output'"
        exit 1
    fi
fi

# Get the base filename without extension
base_filename=$(basename "$jsonl_file" .jsonl)

# Create a temporary file to store filtered rows
temp_file=$(mktemp)

# Filter the JSONL file to include only rows with _tag_=plan
grep -E '"_tag_"[[:space:]]*:[[:space:]]*"plan"' "$jsonl_file" > "$temp_file"

# Count the total number of qualifying rows
total_rows=$(wc -l < "$temp_file")
echo "Found $total_rows qualifying rows with _tag_=plan"

if [ "$total_rows" -eq 0 ]; then
    echo "No qualifying rows found. No shards will be created."
    rm "$temp_file"
    exit 0
fi

# Calculate rows per shard (rounded up for all except possibly the last shard)
rows_per_shard=$(( (total_rows + nshards - 1) / nshards ))

# Create the shards
echo "Creating $nshards shards with approximately $rows_per_shard rows per shard..."

for ((i=0; i<nshards; i++)); do
    # Format shard number with leading zeros (00, 01, 02, etc.)
    shard_num=$(printf "%02d" $i)
    
    # Calculate start and end row for this shard
    start_row=$((i * rows_per_shard + 1))
    end_row=$(((i + 1) * rows_per_shard))
    
    # Ensure we don't exceed the total number of rows
    if [ $end_row -gt $total_rows ]; then
        end_row=$total_rows
    fi
    
    # If we've already processed all rows, break
    if [ $start_row -gt $total_rows ]; then
        break
    fi
    
    output_file="$output/${base_filename}_${shard_num}.jsonl"
    
    # Extract the rows for this shard
    sed -n "${start_row},${end_row}p" "$temp_file" > "$output_file"
    
    rows_in_shard=$(wc -l < "$output_file")
    echo "Shard $shard_num: $rows_in_shard rows written to $output_file"
done

# Clean up the temporary file
rm "$temp_file"

echo "Sharding complete."

### END ###