import numpy as np
from random import randrange

# arr = [randrange(40) for _ in range(40)]
# matrix = np.array(arr).reshape(4, 10)

arr = [
    
    [1, 2, 3, 4, 5, 6, 7, 50, 9, 10],
    [11, 12, 13, 14, 15, 16, 17, 40, 19, 20],
    [21, 22, 23, 24, 25,26, 27, 30, 29, 30 ],
    [31, 32, 33, 34, 35, 36, 37, 20, 39, 40],
]

matrix = np.array(arr).reshape(4, 10)
print(matrix)
column_show=[]
column_counter = 0
for i in range(len(matrix[0])):
    counter = 0
    for j in range(len(matrix[:, i])-1):
        if matrix[:, i][j]>matrix[:, i][j+1] and matrix[:, i][-1]<matrix[:, i][-2]:
             counter+=1
        if counter==3:
            column_counter+=1    
            column_show.append(matrix[:, i])
print(f"Tartibli kamayish column soni: {column_counter}")            
print(f"Tartibli kamayish columnlar: {column_show}")            