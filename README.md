# password-creator ![banner](https://raw.githubusercontent.com/patrickleweryharris/password_creator/master/img/logo.png)


![python](https://img.shields.io/badge/python-3-blue.svg?style=flat-square)
[![pypi](https://img.shields.io/badge/pypi-v1.0.0-blue.svg?style=flat-square)](https://pypi.python.org/pypi/anagram-solver) [![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/patrickleweryharris/anagram-solver/blob/master/LICENSE) [![standard-readme compliant](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)


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

- password_creator is entirely hosted on the client machine, no internet connection is ever used after installation.

- All words used in passwords are randomly sampled from a set of 99172 common english words, which can be found in [password_creator/stuff.py](https://github.com/patrickleweryharris/password_creator/blob/master/password_creator/stuff.py).

- If default settings are used, there are > 1.62 * 10^14 different possibilities for the output.

- Randomness is provided by the python random.sample function.

- **Note**: This project has not been security audited. Use passwords from here at your own risk.

## Background

Project inspired by the [1password](https://github.com/AgileBits) random password generator.

## Install

```shell
$ pip install password-creator
```

## Usage

```shell
$ password_creator
razors-snip-horsehairs # Just an example, your passwords will be different
```

## API
- By default, passwords are three random words long, delimited with dashes.

- The number of characters in a password can also be set.

Both, one, or none of these can be changed at will:

```shell
$ password_creator --set_length 6 --set_delimiter /
stumbles/almanacs/weevils/exemplified/spiffy/mortises # An example
```

```shell
$ password_creator --set_chars 4
flou # An example
```

- Any valid integer can be used as a length or number of characters.
- Delimiters can be any string. Not that the last character in the string is always shaved off to provide better readability for simple input.  
**Note**: any invalid inputs will result in the default values being used.  

## Contribute

PRs accepted.

Small note: If editing the Readme, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

MIT © Patrick Harris
