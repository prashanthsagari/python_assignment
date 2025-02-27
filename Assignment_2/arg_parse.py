import argparse

# Create argument parser
parser = argparse.ArgumentParser(description="Count the number of lines in a file.")
parser.add_argument("filename", type=str, help="Path to the file")

# Parse arguments
args = parser.parse_args()

# Count lines in the file
try:
    with open(args.filename, "r") as file:
        line_count = sum(1 for _ in file)  # generator expression that yields 1 for every line
    print(f"Number of lines in '{args.filename}': {line_count}")
except FileNotFoundError:
    print(f"Error: File '{args.filename}' not found.")
except Exception as e:
    print(f"Error: {e}")


#  python .\arg_parse.py Four_pillars.txt