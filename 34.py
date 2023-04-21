import numpy as np
from random import randrange

arr = [randrange(-20, 20) for i in range(40)]
matrix = np.array(arr).reshape(10, 4)

print(matrix)
print("============================")

for i in matrix:
    even_elements = list(filter(lambda x: x % 2 == 0, i))
    if len(even_elements) == 4:
        print(i)
        break
else:
    print("There is no page")


