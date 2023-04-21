import  numpy as np

k=3
matrix = np.arange(10, 26).reshape(4,4)
print(matrix)
yg = sum(matrix[:, k])
result = 1
[result:=result*i for i in matrix[:,k]]
print(f"Yig'indisi: {yg}, Ko'paytmasi: {result}")

