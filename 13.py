import numpy as np

matrix = np.arange(10, 26).reshape(4, 4)
print(matrix)
# print(matrix[0])
# print(matrix[:, -1][1:])

for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i, -1], end="\t")