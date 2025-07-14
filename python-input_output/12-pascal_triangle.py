#!/usr/bin/python3
"""
Module that generates Pascal's triangle of size n.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal's triangle of size n.

    Args:
        n (int): Number of rows in the triangle.

    Returns:
        list: Pascal's triangle as a list of lists.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row always [1]

    for i in range(1, n):
        row = [1]  # Every row starts with 1
        prev_row = triangle[i - 1]
        for j in range(1, i):
            # Sum of the two numbers above
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # Every row ends with 1
        triangle.append(row)

    return triangle
