#!/usr/bin/env python3
"""
make_multiplier, takes a float 'multiplier' and 
returns a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""
    def multiplier_func(a: float) -> float:
        """float multiply by multiplier"""
        return a * multiplier
    return multiplier_func
