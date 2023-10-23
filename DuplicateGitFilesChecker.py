import os
import sys
import subprocess
from pathlib import Path


def execute(command):
    output = subprocess.check_output(command)
    return output


if len(sys.argv) != 2:
    print('Usage: python "DuplicateGitFilesChecker.py" "<git_repo_path>"')
    sys.exit(1)

git_repo_path = Path(sys.argv[1])
os.chdir(git_repo_path)
output = execute("git ls-files")
lines = output.decode().splitlines(keepends=False)
lines_lowercase = [line.lower() for line in lines]

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
    sys.exit(1)

sys.exit(0)
