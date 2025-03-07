#!/usr/bin/env python3
"""
Write a type-annotated function make_multiplier\
    that takes a float multiplier as argument\
    and returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function make_multiplier that returns\
        a function that multiplies a float by multiplier
    :param multiplier: a float value
    :return: a function that multiplies a float by multiplier
    """
    return lambda x: x * multiplier
