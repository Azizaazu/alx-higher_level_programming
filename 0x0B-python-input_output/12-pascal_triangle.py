#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""

def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
    returns a list of lists of integers representing the triangle.
    """

    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = []
        if i == 0:
            row = [1]
        else:
            prev_row = triangle[i - 1]
            row.append(1)
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)
        triangle.append(row)

    return triangle
