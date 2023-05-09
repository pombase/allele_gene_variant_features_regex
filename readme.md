# Regular expressions for PomBase variant nomenclature

This repository contains a single test script that can be ran on python 3.9 (tested on `3.9.7`), without installing any extra dependencies.

The test script defines a dictionary that contains all possible cases outlined in the paper. There might be a combination of existing patterns that is not defined in the current cases, but it should be easy to capture with the provided examples.

To run the tests simply run:

```bash
python test_regex.py
```