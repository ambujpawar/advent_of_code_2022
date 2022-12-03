"""
Utilities for parsing input files from Advent of Code.
"""
from __future__ import annotations

from typing import Any, List


def read_input(path: str) -> List[Any]:
    """
    Read the input file at the given path and return a list of the lines.
    """
    input_strings = open(path).readlines()
    return [line.strip() for line in input_strings]
