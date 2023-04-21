import numpy as np

m=4
n=5

matrix = np.zeros((m, n))

for i in range(m):
    for j in range(n):
        data = matrix[i][j]=m
        print(data, end="\t")
    print()