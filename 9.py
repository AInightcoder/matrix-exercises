import numpy as np

k = 1
matrix = np.arange(10, 50).reshape(10, 4)
print(matrix, "\n================")

# data = ""
# for l in range(0, len(matrix), 2):
#     data +=str(matrix[l])+"\n"
# print(type(data))    

data = [matrix[item] for item in range(len(matrix)) if item%2==0 ]

print(data)