import numpy as np
from random import randrange

arr = [randrange(-20, 20) for _ in range(40)]
matrix = np.array(arr).reshape(4, 10)

print(matrix)

max_count = 0
max_column = None
for i in range(len(matrix[0])):
    freq_dict = {}
    for row in matrix[:, i]:
        if row in freq_dict:
            freq_dict[row] += 1
        else:
            freq_dict[row] = 1
    counter = 0
    for key in freq_dict:
        if freq_dict[key] > 1:
            counter += freq_dict[key]
    if counter > max_count:
        max_count = counter
        max_column = i

if max_column is not None:
    print(matrix[:, max_column])
else:
    print("No repeated elements found.")
