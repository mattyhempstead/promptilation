import argparse
from pathlib import Path  # Import pathlib.Path

from pcc import promptile

print("Promptiler v0.1")
print()

# Create the parser
parser = argparse.ArgumentParser(
    description="""\
Promptiler is a loose pseudocode compiler powered by LLMs.
""")

# Add the arguments
parser.add_argument("--input-file", type=Path, required=True, help="The input file path containing the pseudocode.")  # Change type to Path
parser.add_argument("--output-dir", type=Path, help="The output directory.", default=Path("build"))  # Change type to Path

# Extract arguments
args = parser.parse_args()
input_file: Path = args.input_file
output_dir: Path = args.output_dir

promptile(args.input_file, args.output_dir)
