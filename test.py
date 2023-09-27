import numpy as np
a = np.array((1, 2, 3, 5))
b = np.array((4, 5, 6, 51))

dist = np.linalg.norm(a-b)

print(dist)
