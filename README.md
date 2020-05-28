# PiXL Maths App Farm
[![Tests](https://github.com/nihaals/pixl-maths-app-farm/workflows/Tests/badge.svg)](https://github.com/nihaals/pixl-maths-app-farm/actions?query=workflow%3ATests)
[![codecov](https://codecov.io/gh/nihaals/pixl-maths-app-farm/branch/master/graph/badge.svg)](https://codecov.io/gh/nihaals/pixl-maths-app-farm)
[![PyPI](https://img.shields.io/pypi/v/PMA)](https://pypi.org/project/PMA/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/PMA)](https://pypi.org/project/PMA/)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/PMA)](https://pypi.org/project/PMA/)

This project requires at least Python 3.8.
The tool is designed to work with [PiXL's Maths App](https://mathsapp.pixl.org.uk/PMA2.html).
It was created by reverse engineering the flash file and took a huge amount of time so any
support is appreciated.

## Setup
1. Install [Python](https://www.python.org/downloads/)
2. Run `pip install -U pma` in your terminal/command prompt. This is the same command to update

There are also docker images on [GitHub](https://github.com/nihaals/pixl-maths-app-farm/packages) and [Docker Hub](https://hub.docker.com/r/orangutan/pma).

## CLI Usage
* `pma farm --help`
* `python -m pma farm --help`
* `python -m pma farm --goal 100 SCHOOL_ID USERNAME PASSWORD`
* `python -m pma farm --yes SCHOOL_ID USERNAME PASSWORD`
* `python -m pma farm --goal 100 --yes SCHOOL_ID USERNAME PASSWORD`
* `python -m pma farm SCHOOL_ID USERNAME PASSWORD`

Note: You can use either `pma` or `python -m pma`
