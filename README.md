# DuplicateGitFilesChecker

This script returns a list of files that are duplicated within your Git repository.

## Usage

Usage: `python "DuplicateGitFilesChecker.py" "<git_repo_path>"`

## Known Issue

If you need this script to work with folders as well, please create an issue in the repository.<br>
I have a working method for handling folders by iterating recursively through the directory structure using the following Git command:
```
git ls-tree --name-only -d HEAD
```
I didn't code this because I personally don't need it, but it effectively lists directories in a Git repository, which would be a starting point to implement the script to works with folders as well.

## Extra

Something else useful is the git command:

`git config core.ignorecase true` (can be set to `true`, `false` or `unset`)

see more at:
https://git-scm.com/docs/git-config
