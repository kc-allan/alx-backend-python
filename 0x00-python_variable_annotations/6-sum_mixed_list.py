#!/usr/bin/env python3
"""
Write a type-annotated function sum_mixed_list\
    which takes a list mxd_lst of integers and floats\
    and returns their sum as a float.
"""


def sum_mixed_list(mxd_lst: list[int | float]) -> float:
    """
    Function sum_mixed_list that returns the sum of a list's contents
    :param mxd_lst: a list of float and int values
    :return: some of all n values in mxd_lst
    """
    sum: float = 0.0
    for i in mxd_lst:
        sum += i
    return sum
