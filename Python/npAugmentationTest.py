import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([5, 6])
C = np.array([[7], [8]])

tmp = np.empty((3, 3))

tmp[:2, :2] = A
tmp[2:, :2] = B
tmp[:2, 2:] = C

print(tmp)
