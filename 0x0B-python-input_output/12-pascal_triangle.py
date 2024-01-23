#!/usr/bin/python3
"""
The module containing code for:
    pascal_triangle
"""


def pascal_triangle(n):
    """Draws a pascal triangle.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        list: The triangle
    """

    row_counter = 0
    rows = []

    while row_counter < n:
        new_row = []
        front_ptr, back_ptr = 1, 0

        row_counter += 1

        if row_counter == 1:
            rows.append([1])
            continue
        elif row_counter == 2:
            rows.append([1, 1])
            continue

        new_row.clear()
        new_row.append(1)
        prev_row = rows[row_counter - 2]

        while front_ptr < len(prev_row):
            new_row.append(prev_row[front_ptr] + prev_row[back_ptr])
            front_ptr += 1
            back_ptr += 1

        new_row.append(1)
        rows.append(new_row)

    return rows
