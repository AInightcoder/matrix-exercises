import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [10, 11, 12],
                   [13, 14, 15]])

row22 = np.copy(matrix[:, 0])

row2 = matrix[:, 0]
row5 = matrix[:, -1]
print(matrix, "\n=========================")

matrix[:, 0] = row5 
matrix[:, -1] = row22

print(matrix)
