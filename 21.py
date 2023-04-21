import  numpy as np

matrix = np.arange(10, 50).reshape(10,4)
print(matrix)   
data = [sum(matrix[i])/len(matrix[i]) for i in range(1, len(matrix), 2)]

print(data)