import numpy as np

matrix = np.ones((4, 5))

for i in range(4):
   for j in range(5):
      data = matrix[i][j]=5*j
      print(data, end="\t")
   print()