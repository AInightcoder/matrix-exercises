import numpy as np
from random import randrange

arr = [randrange(-10, 30) for _ in range(40)]
matrix = np.array(arr).reshape(10, 4)
print(matrix)
print("==========================")

# find rows that contain all positive elements
positive_rows = np.where((matrix > 0).all(axis=1))[0]
print(positive_rows)
matrix = np.delete(matrix, positive_rows, axis=0)

print(matrix)
 