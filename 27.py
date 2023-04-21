import  numpy as np

matrix = np.arange(10, 50).reshape(10,4)
print(matrix)

data = [sum(i) for i in matrix]
print(data)

min_el = min(data)
index_el = data.index(min(data))
print(max(matrix[index_el]))