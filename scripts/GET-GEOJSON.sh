#!/bin/bash

# Function to display usage
usage() {
    echo "Usage: $0 --state STATE_CODE --output OUTPUT_PATH --version VERSION"
    echo "  --state    Two-character state code (e.g., NC, CA, TX)"
    echo "  --output   Path where the file should be downloaded"
    echo "  --version  Version of the data file (e.g., v06, v07)"
    echo ""
    echo "Examples:"
    echo "  $0 --state NC --output /tmp/NC_Geojson.zip --version v06"
    echo "  $0 --state CA --output /tmp/CA_data.zip --version v07"
    exit 1
}

# Initialize variables
STATE=""
OUTPUT=""
VERSION=""

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --state)
            STATE="$2"
            shift 2
            ;;
        --output)
            OUTPUT="$2"
            shift 2
            ;;
        --version)
            VERSION="$2"
            shift 2
            ;;
        -h|--help)
            usage
            ;;
        *)
            echo "Unknown option: $1"
            usage
            ;;
    esac
done

# Validate arguments
if [[ -z "$STATE" ]]; then
    echo "Error: --state argument is required"
    usage
fi

if [[ -z "$OUTPUT" ]]; then
    echo "Error: --output argument is required"
    usage
fi

if [[ -z "$VERSION" ]]; then
    echo "Error: --version argument is required"
    usage
fi

# Validate state code format (should be 2 characters)
if [[ ! "$STATE" =~ ^[A-Za-z]{2}$ ]]; then
    echo "Error: State code must be exactly 2 characters (e.g., NC, CA, TX)"
    exit 1
fi

# Convert state code to uppercase
STATE=$(echo "$STATE" | tr '[:lower:]' '[:upper:]')

# Create output directory if it doesn't exist
OUTPUT_DIR=$(dirname "$OUTPUT")
if [[ ! -d "$OUTPUT_DIR" ]]; then
    echo "Creating directory: $OUTPUT_DIR"
    mkdir -p "$OUTPUT_DIR"
fi

# Construct the URL
URL="https://raw.githubusercontent.com/dra2020/vtd_data/master/2020_VTD/${STATE}/Geojson_${STATE}.${VERSION}.zip"

# Download the file
echo "Downloading VTD data for state: $STATE (version: $VERSION)"
echo "URL: $URL"
echo "Output: $OUTPUT"
echo ""

if curl -L -o "$OUTPUT" "$URL"; then
    echo "Download completed successfully: $OUTPUT"
else
    echo "Error: Download failed"
    exit 1
fi