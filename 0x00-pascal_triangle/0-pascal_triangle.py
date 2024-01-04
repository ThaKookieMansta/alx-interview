#!/usr/bin/python3
"""
This module contains the Pascal Triangle method
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the pascal traingle
    of n
    Args:
        n:

    Returns: A list of integers

    """
    if n <= 0:
        return []

    pascal_tri = [0] * n

    for i in range(n):
        new_row = [0] * (i + 1)
        new_row[0] = 1
        new_row[len(new_row) - 1] = 1

        for j in range(1, i):
            if 0 < j < len(new_row):
                x = pascal_tri[i - 1][j]
                y = pascal_tri[i - 1][j - 1]
                new_row[j] = x + y

        pascal_tri[i] = new_row

    return pascal_tri
