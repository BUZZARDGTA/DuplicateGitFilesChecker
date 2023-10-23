import os
import subprocess
from pathlib import Path


git_repo_directory = Path("D:/Git/Illegal_Services/GitHub")
os.chdir(git_repo_directory)

command = "git ls-files"
try:
    output = subprocess.check_output(command, shell=True, text=True)
except subprocess.CalledProcessError as e:
    print("Error running the command:", e)
    exit(0)

# Split the output into lines and convert them to lowercase
lines = output.split("\n")
lines_lowercase = [line.lower() for line in lines]

# Create a set to keep track of seen lines (case-insensitive)
seen_lines = set()
duplicates = set()

# Check for duplicates (case-insensitive) and print them
for line, line_lower in zip(lines, lines_lowercase):
    if line_lower in seen_lines:
        duplicates.add(line)
    seen_lines.add(line_lower)

if duplicates:
    for duplicate in sorted(duplicates, key=str.lower):
        print(duplicate)
