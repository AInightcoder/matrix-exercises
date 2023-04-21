import  numpy as np

matrix = np.arange(10, 26).reshape(4,4)
yig = []
for i in range(len(matrix)):
    yig.append(sum(matrix[:, i]))
print(yig)    

