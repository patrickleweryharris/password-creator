# password-creator ![banner](/img/logo.png)


![python](https://img.shields.io/badge/python-3-blue.svg?style=flat-square)
[![pypi](https://img.shields.io/badge/pypi-v1.1.0-blue.svg?style=flat-square)](https://pypi.python.org/pypi/anagram-solver) [![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/patrickleweryharris/anagram-solver/blob/master/LICENSE) [![standard-readme compliant](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)


> Random password generation from the command line

Create random passwords using a dictionary of close to one hundred thousand English words

## Table of Contents

- [Security](#security)
- [Background](#background)
- [Installation](#installation)
- [Usage](#usage)
- [API](#api)
- [Contribute](#contribute)
- [License](#license)

## Security

password_creator is entirely hosted on the client machine, no internet connections is ever used after installation

All words used in passwords are randomly sampled from a set of 99172 common english words, which can be found [password_creator/stuff.py](https://github.com/patrickleweryharris/password_creator/blob/master/password_creator/stuff.py)

## Background

Project inspired by the [1password](https://github.com/AgileBits) random password generator

## Install

```shell
$ pip install password-creator
```

## Usage

```shell
$ password_creator
yuletide-southwests-wheal # Just an example, your passwords will be different
```

## API
By default, passwords are three random words long, delimited with dashes

Both, one, or none of these can be changed at will:

```shell
$ password_creator --set_length 6 --set_delimiter /
stumbles/almanacs/weevils/exemplified/spiffy/mortises # An example
```
**Note**: any invalid inputs will result in the default values being used
## Contribute

PRs accepted.

Small note: If editing the Readme, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

MIT © Patrick Harris
