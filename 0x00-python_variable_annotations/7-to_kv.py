#!/usr/bin/env python3
"""
Write a type-annotated function to_kv\
    that takes a string k and an int OR float v as arguments\
    and returns a tuple.
The first element of the tuple is the string k.
The second element is the square of the int/float v\
    and should be annotated as a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function to_kv that returns a tuple of a string and a float
    :param k: a string
    :param v: an int or float
    :return: a tuple containing k and the square of v
    """
    sq: float = v * v
    return (k, sq)
