# SecretSharer

## Introduction
SecretSharer is a python script that uses [blockstacks secret-sharing library](https://github.com/blockstack/secret-sharing) to share or restore secrets

## Requirements
```
sudo -H pip install secretsharing ArgumentParser --upgrade
```

## Usage
```
usage: secretsharer.py [-h] [-i [IN]] [-o [OUT]] [-v] {share,restore} ...

Split a secret into some shares

optional arguments:
  -h, --help            show this help message and exit
  -i [IN], --in [IN]    input file (default: stdin)
  -o [OUT], --out [OUT]
                        output file (default: stdout)
  -v, --version         show program's version number and exit

subcommands:
  valid subcommands

  {share,restore}       command to execute
    share               share a secret
    restore             restore a secret
```

## License
`secretsharer.py` is licensed under the [GPLv3](https://www.gnu.org/licenses/gpl-3.0.html)
