#!/bin/bash

# scripts/CONCAT_FILES.sh /path/to/csvs "NC20C_scores_compactness_*.csv"
#
# Vertically concatenates CSV files in the specified directory with a given pattern,
# in sort order, e.g., "NC20C_scores_compactness_01.csv", "NC20C_scores_compactness_02.csv", etc.
# The files are assumed to have a header row which is not repeated in the output.
# 
# For the example above, it creates /path/to/csvs/NC20C_scores_compactness.csv.
#
# Examples:
# scripts/CONCAT_FILES.sh /path/to/csvs "NC20C_scores_general_*.csv"
# scripts/CONCAT_FILES.sh /path/to/csvs "NC20C_scores_partisan_*.csv"
# scripts/CONCAT_FILES.sh /path/to/csvs "NC20C_scores_minority_*.csv"
# scripts/CONCAT_FILES.sh /path/to/csvs "NC20C_scores_compactness_*.csv"
# scripts/CONCAT_FILES.sh /path/to/csvs "NC20C_scores_splitting_*.csv"

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 directory pattern"
    echo "Example: $0 /path/to/dir 'NC20C_scores_compactness_*.csv'"
    exit 1
fi

directory="$1"
pattern="$2"
ext="${pattern##*.}"

# echo "Concatenating files in $directory with pattern $pattern"

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
        # For subsequent files, skip first line (header)
        tail -n +2 "$file" >> "$temp_dir/temp.${ext}"
    fi
done

# Move final result
mv "$temp_dir/temp.${ext}" "$output_file"

# Cleanup
rm -r "$temp_dir"

# echo "Combined file created as $output_file"

### END ###