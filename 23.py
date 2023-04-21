import  numpy as np

matrix = np.arange(10, 50).reshape(10,4)
print(matrix)   
data = [min(i) for i in matrix]
print(data)