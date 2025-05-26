#!/bin/bash

# scripts/JOIN_CSVS.sh /path/to/csvs "NC_congress_scores_*.csv"
#
# Horizontally joins CSV files in the specified directory with a given pattern.
# The individual files instantiate the patter with "general", "partisan", "minority", "compactness", and "splitting",
# the scoring 'modes'.
#
# For the example above, it creates: /path/to/csvs/NC_congress_scores.csv.

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 directory pattern"
    echo "Example: $0 /path/to/dir 'NC_congress_scores_*.csv'"
    exit 1
fi

directory="$1"
pattern="$2"

echo "Joining CSVs in $directory with pattern $pattern"

# Extract base name for output file (remove trailing underscore)
base_pattern=$(echo "$pattern" | sed 's/_\*.*$//')
output_file="${directory}/${base_pattern}.csv"

cd "$directory" || exit 1

# Define file order
declare -a categories=("general" "partisan" "minority" "compactness" "splitting")

# Create temp directory
temp_dir=$(mktemp -d)

# Process first file (partisan) to get map column
first_file="${base_pattern}_${categories[0]}.csv"
cut -d',' -f1 "$first_file" | tr -d '\r' > "$temp_dir/combined.csv"

# Process each file in specified order
for category in "${categories[@]}"; do
    file="${base_pattern}_${category}.csv"
    if [ ! -f "$file" ]; then
        echo "Warning: $file not found"
        continue
    fi
    
    # Get number of columns in file
    num_cols=$(head -n 1 "$file" | tr ',' '\n' | wc -l)
    
    # Create cut list for all columns except 'map'
    cut_list=""
    for i in $(seq 2 "$num_cols"); do
        cut_list="${cut_list}${cut_list:+,}${i}"
    done
    
    # Cut columns and remove carriage returns
    cut -d',' -f"$cut_list" "$file" | tr -d '\r' > "$temp_dir/temp.csv"
    
    # Paste side by side with existing result
    paste -d',' "$temp_dir/combined.csv" "$temp_dir/temp.csv" > "$temp_dir/temp2.csv"
    mv "$temp_dir/temp2.csv" "$temp_dir/combined.csv"
done

# Add back carriage return at end of each line
sed 's/$/\r/' "$temp_dir/combined.csv" > "$output_file"

rm -r "$temp_dir"
echo "Combined CSV created as $output_file"

### END ###