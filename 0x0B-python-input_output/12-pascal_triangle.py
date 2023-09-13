#!/usr/bin/python3
"""Calculates the time complexity"""


def pascal_triangle(n):
    """Represents Pascal's Triangle of size n
    """
    if n <= 0:
        return []

    row = [0] * (n+1)
    row[0] = 1
    for i in range(1, n+1):
        row[i] = (n-i+1) * row[i-1] // i

    return row[1:]
