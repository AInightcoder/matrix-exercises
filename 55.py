import numpy as np

matrix = np.array([[20, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [10, 18, 12]])

h=len(matrix)//2

head_half_matrix =np.copy(matrix[:h])

matrix[:h]=np.copy(matrix[h:])
matrix[h:]=head_half_matrix


print(matrix)