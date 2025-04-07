#!/bin/bash

# scripts/CONCAT_FILES.sh /path/to/csvs "NC_congress_scores_compactness_*.csv" 
# scripts/CONCAT_FILES.sh /path/to/csvs "NC_congress_by-district_compactness_*.jsonl" --no-header
#
# Vertically concatenates CSV files in the specified directory with a given pattern,
# in sort order, e.g., "NC_congress_scores_compactness_01.csv", "NC_congress_scores_compactness_02.csv", etc.
# 
# By default, the files are assumed to have a header or metadata row which is not repeated in the output.
# If the --no-header option is provided, files are simply appended without removing the first line.
#
# For the example above, it creates /path/to/csvs/NC_congress_scores_compactness.csv.
#
# Examples:
# scripts/CONCAT_FILES.sh /path/to/csvs "NC_congress_scores_general_*.csv"
# scripts/CONCAT_FILES.sh /path/to/csvs "NC_congress_scores_partisan_*.csv"
# scripts/CONCAT_FILES.sh /path/to/csvs "NC_congress_scores_minority_*.csv"
# scripts/CONCAT_FILES.sh /path/to/csvs "NC_congress_scores_compactness_*.csv"
# scripts/CONCAT_FILES.sh /path/to/csvs "NC_congress_scores_splitting_*.csv"

# Check for valid number of arguments
if [ "$#" -lt 2 ] || [ "$#" -gt 3 ]; then
    echo "Usage: $0 directory pattern [--no-header]"
    echo "Example: $0 /path/to/dir 'NC_congress_scores_compactness_*.csv'"
    echo "Example with --no-header: $0 /path/to/dir 'NC_congress_scores_compactness_*.csv' --no-header"
    exit 1
fi

directory="$1"
pattern="$2"
ext="${pattern##*.}"
no_header=false

# Check if third argument is provided and it's --no-header
if [ "$#" -eq 3 ] && [ "$3" = "--no-header" ]; then
    no_header=true
fi

# Extract base name by removing '_*' and last extension
base_name=$(echo "$pattern" | sed 's/_\*.*$//')
output_file="${directory}/${base_name}.${ext}"

# Change to specified directory
cd "$directory" || exit 1

# Create temp directory
temp_dir=$(mktemp -d)

# Process each file
first_file=true
for file in $pattern; do
    if [ "$first_file" = true ]; then
        # Copy first file as is
        cp "$file" "$temp_dir/temp.${ext}"
        first_file=false
    else
        if [ "$no_header" = true ]; then
            # When --no-header is specified, include all lines from subsequent files
            cat "$file" >> "$temp_dir/temp.${ext}"
        else
            # Default behavior: for subsequent files, skip first line (header)
            tail -n +2 "$file" >> "$temp_dir/temp.${ext}"
        fi
    fi
done

# Move final result
mv "$temp_dir/temp.${ext}" "$output_file"

# Cleanup
rm -r "$temp_dir"

### END ###