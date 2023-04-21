import numpy as np
from random import randrange

arr = [randrange(-20, 20) for _ in range(40)]
matrix = np.array(arr).reshape(10, 
4)
print(matrix)
print("==========================")

max_index = np.unravel_index(np.argmax(matrix, axis=None),matrix.shape)
matrix=np.delete(matrix, max_index[1], 1)
print(matrix)