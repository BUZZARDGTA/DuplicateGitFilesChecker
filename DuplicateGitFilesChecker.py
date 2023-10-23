import os
import subprocess
from pathlib import Path


GIT_REPO = Path("D:/Git/Illegal_Services/GitHub")


def run_git_command(command):
    try:
        output = subprocess.check_output(command)
        output = output.decode().splitlines(keepends=False)
        return output
    except subprocess.CalledProcessError as e:
        raise("Error running the command:", e)


os.chdir(GIT_REPO)
lines = run_git_command("git ls-files")
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
