#!/usr/bin/env python3
"""Function to_kv, take a string 'k' and an int or a float'v'
and return a tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, v**2)
