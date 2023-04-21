import numpy as np

matrix = np.arange(10, 50).reshape(4 ,10)
print(matrix, "\n================")

data=""
for l in range(1, len(matrix[0, :]), 2):
     data += str(matrix[:, l])+"\n"

print(data)