#!/bin/bash

# Function to display usage
usage() {
    echo "Usage: $0 --input <zip_file> --output <output_directory>"
    echo "  --input   Path to the zip file to extract"
    echo "  --output  Directory where files will be extracted"
    exit 1
}

# Initialize variables
INPUT_FILE=""
OUTPUT_DIR="" # OUTPUT

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --input)
            INPUT_FILE="$2"
            shift 2
            ;;
        --output)
            OUTPUT_DIR="$2"
            shift 2
            ;;
        -h|--help)
            usage
            ;;
        *)
            echo "Error: Unknown option $1"
            usage
            ;;
    esac
done

# Check if both arguments are provided
if [[ -z "$INPUT_FILE" || -z "$OUTPUT_DIR" ]]; then
    echo "Error: Both --input and --output arguments are required."
    usage
fi

# Check if input file exists
if [[ ! -f "$INPUT_FILE" ]]; then
    echo "Error: Input file '$INPUT_FILE' does not exist."
    exit 1
fi

# Check if input file is a zip file
if ! file "$INPUT_FILE" | grep -q -i zip; then
    echo "Error: '$INPUT_FILE' does not appear to be a zip file."
    exit 1
fi

# Create output directory if it doesn't exist
if [[ ! -d "$OUTPUT_DIR" ]]; then
    echo "Creating directory: $OUTPUT_DIR"
    mkdir -p "$OUTPUT_DIR"
    if [[ $? -ne 0 ]]; then
        echo "Error: Failed to create directory '$OUTPUT_DIR'."
        exit 1
    fi
fi

# Unzip the file
echo "Extracting '$INPUT_FILE' to '$OUTPUT_DIR'..."
unzip -q "$INPUT_FILE" -d "$OUTPUT_DIR"

if [[ $? -eq 0 ]]; then
    echo "Successfully extracted '$INPUT_FILE' to '$OUTPUT_DIR'"
else
    echo "Error: Failed to extract '$INPUT_FILE'"
    exit 1
fi