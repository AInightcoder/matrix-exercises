# import numpy as np

# matrix = np.arange(10, 50).reshape(10 ,4)
# print(matrix, "\n================")
# matrix2 = matrix
# data=""
# for i in range(len(matrix)):
#     if i%2==0:
#         data+=str(matrix[i+1])+'\n'
#     else:
#         data +=str(matrix2[i-1])+"\n"   

import numpy as np

# create the matrix
matrix = np.arange(10, 50).reshape(4, 10)
print(matrix, "\n====================")

new_matrix = np.empty_like(matrix)

new_matrix[:, ::2]=matrix[:, 1::2]
new_matrix[:, 1::2]=matrix[:, ::2]

print(new_matrix)
print(type(new_matrix), type(matrix))
print(new_matrix.shape, matrix.shape)
