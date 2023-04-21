import numpy as np
from random import randrange

arr = [randrange(40) for _ in range(40)]
matrix = np.array(arr).reshape(10, 4)
print(matrix)
satr_show=[]
satr_counter = 0
for row in matrix:
    couter=0
    for i in range(len(row)-1):
        if row[i]<row[i+1] and row[-1]>row[-2]:
              couter+=1
              if couter==3:
                  satr_show.append(row)
                  satr_counter+=1   
print(f"Tartibli satrlar soni: {satr_counter}")   
print(f"Tartibli satrlar: {satr_show}")  