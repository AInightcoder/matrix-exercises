import  numpy as np

matrix = np.arange(10, 50).reshape(10,4)
print(matrix)
result = 1   
data = [sum(i) for i in matrix]

print(max(data), data.index(max(data)))
