# gunc
Get git repositories in a directory tree with uncommitted changes

## Installation

```sh
$ pip install .
$ gunc -h
usage: gunc [-h] [-v] [path]

Get git repositories with uncommitted changes

positional arguments:
  path        path to search below [working directory by default]

optional arguments:
  -h, --help  show this help message and exit
  -v          print uncommitted files
```

## Usage examples

```sh
$ gunc  # print paths to repos below working directory with uncommitted changes
/code/repo1
/code/repo2
[ds] ~/code
$ gunc -v # print paths and uncommitted files (output of `git status --porcelain`)
/code/repo1
A  filea

/code/repo2
?? fileb
```
