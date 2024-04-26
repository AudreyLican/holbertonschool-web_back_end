#!/usr/bin/env python3
"""A simple Python module for creating multiplier functions.

This module provides a function that generates and returns another function,
which multiplies its input by a pre-defined multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Multiply a given float by a fixed multiplier."""

    def multiplier_function(a: float) -> float:
        """float multiply by multiplier"""
        return a * multiplier

    return multiplier_function
