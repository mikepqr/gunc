# gunc
Get git repositories in a directory tree with uncommitted changes

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
$ gunc  # print paths to repos below working directory with uncommitted changes
/Users/mike/code/repo1
/Users/mike/code/repo2
[ds] ~/code
$ gunc -v # print paths and uncommitted files (output of `git status --porcelain`)
/Users/mike/code/repo1
A  filea

/Users/mike/code/repo2
?? fileb
```
