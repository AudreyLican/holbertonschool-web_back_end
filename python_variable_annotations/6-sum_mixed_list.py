#!/usr/bin/env python3
"""Function sum_mixed_list, take a list 'mxd_lst' of integer &
floats and return their sum as float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns the sums of integers and floats in 'mxd_lst'."""
    return sum(mxd_lst)
