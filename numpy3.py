import numpy as np

a = np.array([10, 20, 30, 40, 50])
b = np.array([10, 25, 30, 35, 50])

indices_diff = np.where(a != b)

print("Indices avec différence :", indices_diff[0])
print("Valeurs dans 'a' :", a[indices_diff])
print("Valeurs dans 'b' :", b[indices_diff])
