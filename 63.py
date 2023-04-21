import numpy as np
from random import randrange

arr = [randrange(-20, 20) for _ in range(40)]
matrix = np.array(arr).reshape(10, 
4)
print(matrix)
print("==========================")

min_index = np.unravel_index(np.argmin(matrix, axis=None),matrix.shape)
print(min_index[0])
matrix=np.delete(matrix, min_index[0], 0)
print(matrix)