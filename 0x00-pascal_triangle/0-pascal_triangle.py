#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """Pascal's Triangle
    Create a function def pascal_triangle(n):
    that returns a list of lists of integers
    representing the Pascals triangle of n"""

    if n <= 0:
        return []

    pascal = [[1]]

    for i in range(n - 1):
        Row = [0] + pascal[-1] + [0]
        lenght = len(pascal[-1]) + 1
        pascal.append([Row[j] + Row[j + 1] for j in range(lenght)])

    return pascal
