import numpy as np

dist = np.array([1, 3, 2, 4, 0, 6, 7])
sorted_indices = np.argsort(dist)
five_smallest_indices = sorted_indices[:5]

print(five_smallest_indices)
