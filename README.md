# MMMMMMAAAAAAARRRRRRRRRRSSSSSSSSSS
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Instructions
https://code.google.com/archive/p/marsrovertechchallenge/


## Assumptions Made
The most massive assumption I'm making is that all input will always be perfect!
(If I've added some error-handling, it was because it was bothering me and not because I meant to)

**TL;DR**
- All input is without error

## Recommended Usage
Let [pipenv](https://pipenv-fork.readthedocs.io/en/latest/) do the heavy lifting, by letting it create a [virtualenv](https://realpython.com/python-virtual-environments-a-primer/) and install packages as specified in `Pipfile.lock` using:

`pipenv install`

## Bare Metal Usage
It's a simple script! No installations, just a requirement of python 3.5 and you can run it using the example command below.

_Requirements_
- python 3.5+

_Example_\
`python rover.py`

## Tests
Tests are defined using pytest and require the pytest package to run. There are extra packages in there to make the output look good. Assuming you followed the recommended usage and have the virtualenv active, the commands you need would be:

```pytest```
