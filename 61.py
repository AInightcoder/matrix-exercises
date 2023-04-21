import numpy as np
from random import randrange

arr = [randrange(-20, 20) for _ in range(40)]
matrix = np.array(arr).reshape(10, 
4)
print(matrix, "\n======================")
k = int(input("K >>> "))
matrix=np.delete(matrix,k,0)
print(matrix)