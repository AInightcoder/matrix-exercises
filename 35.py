import numpy as np
from random import randrange

arr = [randrange(-20, 20) for _ in range(40)]
matrix = np.array(arr).reshape(4, 10)
print(matrix)

print("=========================")

couter=0
for i in range(10):
    lambda_odd = list(filter(lambda x: x%2!=0, matrix[:, i]))
    couter+=1
    if len(lambda_odd)==4:
        print(f"Odd_column:{matrix[:, i]}, Number: {couter}")
        break
else:
    print("there is no page")    