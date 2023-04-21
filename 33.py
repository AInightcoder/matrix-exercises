import numpy as np
from random import randrange

arr = [randrange(-20, 20) for _ in range(40)]

matrix = np.array(arr).reshape(10, 4)

print(matrix)
print("===============")
print(matrix[::-1])
print("===============")

for i in matrix[::-1]:
   negative = np.count_nonzero(i<0)
   positive = np.count_nonzero(i>0)

   if negative==positive:
        print(i)
        break
   else:
       print("there is no page")
 
    

