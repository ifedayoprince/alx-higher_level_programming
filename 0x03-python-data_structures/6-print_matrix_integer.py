#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for idx in matrix:
        print(*idx)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
