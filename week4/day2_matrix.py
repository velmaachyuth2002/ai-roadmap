import random
import time
import numpy as np


def dot(a, b):
    if len(a) != len(b):
        raise ValueError("Vectors must have the same length.")

    total = 0
    for i in range(len(a)):
        total += a[i] * b[i]

    return total


def matmul(A, B):
    rows_a = len(A)
    cols_a = len(A[0])

    rows_b = len(B)
    cols_b = len(B[0])

    if cols_a != rows_b:
        raise ValueError(
            f"Cannot multiply matrices of shape ({rows_a}, {cols_a}) and ({rows_b}, {cols_b})"
        )

    result = []

    for i in range(rows_a):
        row = []

        for j in range(cols_b):
            column = []

            for k in range(rows_b):
                column.append(B[k][j])

            row.append(dot(A[i], column))

        result.append(row)

    return result


# Test
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

print(matmul(A, B))
# [[19, 22], [43, 50]]


# Shape mismatch
try:
    C = [[1, 2, 3]]
    D = [[1, 2],
         [3, 4]]

    print(matmul(C, D))
except ValueError as e:
    print(e)


# NumPy verification
A_np = np.array(A)
B_np = np.array(B)

print(A_np @ B)
# or
print(np.matmul(A_np, B_np))


# Timing comparison
SIZE = 200

A = [[random.random() for _ in range(SIZE)] for _ in range(SIZE)]
B = [[random.random() for _ in range(SIZE)] for _ in range(SIZE)]

start = time.perf_counter()
matmul(A, B)
end = time.perf_counter()
print("Python matmul:", end - start)

A_np = np.array(A)
B_np = np.array(B)

start = time.perf_counter()
A_np @ B_np
end = time.perf_counter()
print("NumPy matmul:", end - start)