import  numpy as np

matrix = np.arange(10, 50).reshape(10,4)
print(matrix)   
data = []
for l in range(len(matrix[0])):
     data.append(max(matrix[:, l]))

print(f"Max elements:{data}")    
