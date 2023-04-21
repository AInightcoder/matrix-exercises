import numpy as np

m=5
n=4
d=2

matrix = np.zeros((m, n))

for i in range(m):
    for j in range(n):
        data = matrix[i, :]=i+d
        print(data, end="\t")
    print()    