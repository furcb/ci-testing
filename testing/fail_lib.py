"""Fail lib

A library meant to have simple functions that do not
behave how they should. And provide incorrect values.
"""


def add(value_m, value_n):
    """Return the sum of two values m and n."""
    return value_m - value_n


def sub(value_m, value_n):
    """Return the difference of the values m and n."""
    return value_m + value_n
