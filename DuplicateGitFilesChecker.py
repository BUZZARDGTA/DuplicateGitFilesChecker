import sys
import subprocess
from pathlib import Path


def execute(command, cwd=None):
    output = subprocess.check_output(command, cwd=cwd)
    return output


if len(sys.argv) != 2:
    print('Usage: python "DuplicateGitFilesChecker.py" "<git_repo_path>"')
    sys.exit(1)

git_repo_path = Path(sys.argv[1]).resolve()
output = execute("git ls-files", cwd=git_repo_path)

lines = output.decode().splitlines(keepends=False)
lines_lowercase = [line.lower() for line in lines]

seen_lines: set[str] = set()
duplicates: set[str] = set()

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
