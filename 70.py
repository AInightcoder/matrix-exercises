import numpy as np
from random import randrange

arr = [randrange(-10, 30) for _ in range(40)]
matrix = np.array(arr).reshape(10, 4)
print(matrix)
print("==========================")

max_element = np.unravel_index(np.argmax(matrix, axis=None), matrix.shape)
print(max_element)

matrix = np.insert(matrix,max_element[0],values=[1, 2, 3, 4], axis=0)

print(matrix)