

import time
import random
import numpy as np



def dot(a, b):
    if len(a) != len(b):
        raise ValueError("Vectors must have the same length")

    total = 0

    for i in range(len(a)):
        total += a[i] * b[i]

    return total


print(dot([1, 2, 3], [4, 5, 6]))  # 32
print(dot([1, 0], [0, 1]))        # 0

try:
    print(dot([1, 2], [1, 2, 3]))
except ValueError as e:
    print(e)



def most_similar(query, docs):
    best_index = -1
    best_score = float("-inf")

    for i, doc in enumerate(docs):
        score = dot(query, doc)

        if score > best_score:
            best_score = score
            best_index = i

    return best_index


query = [1, 0, 1]

docs = [
    [1, 0, 1],
    [0, 1, 0],
    [2, 0, 1],
    [-1, 0, -1],
]

print(most_similar(query, docs))  # 2


# 3. Compare Python dot vs NumPy dot

size = 1_000_000

a = [random.random() for _ in range(size)]
b = [random.random() for _ in range(size)]



start = time.perf_counter()

result1 = dot(a, b)

end = time.perf_counter()

print("Python dot:", result1)
print("Python time:", end - start)



a_np = np.array(a)
b_np = np.array(b)

start = time.perf_counter()

result2 = np.dot(a_np, b_np)

end = time.perf_counter()

print("NumPy dot:", result2)
print("NumPy time:", end - start)