import numpy as np

data = np.array([10, 20, 15, 25, 30])

mean = np.mean(data)
std = np.std(data)

normalized_data = (data - mean) / std

print("Données normalisées :", normalized_data)










