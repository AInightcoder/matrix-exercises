import numpy as np

matrix = np.array([[20, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [10, 18, 12],
                   [13, 14, 15]])


max_index = np.unravel_index(np.argmax(matrix, axis=None), matrix.shape)
min_index = np.unravel_index(np.argmin(matrix, axis=None), matrix.shape)

min_column = np.copy(matrix[:, min_index[1]])
max_column = matrix[:, max_index[0]]

print(f"Max_column:{max_column}, Min_column:{min_column}")

matrix[:, min_index[1]]=max_column
matrix[:, max_index[0]]=min_column

print(matrix)