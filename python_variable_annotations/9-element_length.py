#!/usr/bin/env python3
"""Function make_multiplier, take a float 'multiplier' 
and returns a function that multiplies a float by multiplier"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns list of tuples: elements from 'lst' and their lenghts"""
    return [(i, len(i)) for i in lst]
