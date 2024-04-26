#!/usr/bin/env python3
"""
    Make_multiplier, takes a float 'multiplier' and 
    returns a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Multiply a given float by a fixed multiplier."""

    def multiplier_function(a: float) -> float:
        """float multiply by multiplier"""
        return a * multiplier

    return multiplier_function
