#!/usr/bin/env python3
"""
Annotate function : 'def element_length(lst):
    return [(i, len(i)) for i in lst]'
with appropriate type"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns list of tuples: elements from 'lst' and their lenghts"""
    return [(i, len(i)) for i in lst]
