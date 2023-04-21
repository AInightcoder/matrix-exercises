import  numpy as np

matrix = np.arange(10, 50).reshape(10,4)
print(matrix)
data = []
for i in range(len(matrix[0])):
    data.append(sum(matrix[:, i]))
print(data)    

index_el= data.index(max(data))
print(min(matrix[:, index_el]))