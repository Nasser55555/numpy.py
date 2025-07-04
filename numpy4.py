import numpy as np

A = np.array([[2, 1], [7, 4]])
B = np.array([[3, 5], [1, 2]])

result = np.dot(A, B)
transpose = np.transpose(result)
inverse = np.linalg.inv(result)

print("Multiplication matricielle :\n", result)
print("Transposée :\n", transpose)
print("Inverse :\n", inverse)
