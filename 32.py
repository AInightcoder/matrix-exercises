import numpy as np
from random import randrange

arr = [randrange(-20, 20) for _ in range(40)]

matrix = np.array(arr).reshape(10, 4)

print(matrix)

for i in matrix:
   negative = np.count_nonzero(i<0)
   positive = np.count_nonzero(i>0)

   if negative==positive:
        print(i)
        break
   else:
       print("there is no page")
 
    

