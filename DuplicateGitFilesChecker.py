import os
import subprocess
from pathlib import Path


GIT_REPO = Path("D:/Git/Illegal_Services/GitHub")


def run_git_command(command):
    try:
        return subprocess.check_output(command, shell=True, text=True)
    except subprocess.CalledProcessError as e:
        raise("Error running the command:", e)


os.chdir(GIT_REPO)
output = run_git_command("git ls-files")

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
