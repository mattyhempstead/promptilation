import argparse
import os
from pathlib import Path  # Import pathlib.Path

from pcc import promptile

# Create the parser
parser = argparse.ArgumentParser(description="Process input file and output directory")

# Add the arguments
parser.add_argument("--input-file", type=Path, required=True, help="The input file path")  # Change type to Path
parser.add_argument("--output-dir", type=Path, help="The output directory", default=Path("build"))  # Change type to Path

# Execute the parse_args() method
args = parser.parse_args()

input_file = args.input_file
output_dir = args.output_dir

# Check if the input file parameter is provided
if not input_file:
    raise ValueError("Error: '--input-file' argument is required")

# Print both input file and output directory
print(f"Input file: {input_file}")
print(f"Output directory: {output_dir}")

# If the output directory doesn't exist, create it
if not output_dir.exists():  # Use the exists() method from pathlib
    output_dir.mkdir(parents=True, exist_ok=True)  # Use the mkdir() method from pathlib
    print(f"Output directory '{output_dir}' created.")

promptile(input_file, output_dir)  # No need to change this call, promptile should handle Path objects if designed correctly
