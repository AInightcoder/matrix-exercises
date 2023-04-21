import  numpy as np

matrix = np.arange(10, 26).reshape(4,4)
print(matrix)
result = [sum(i) for i in matrix]
print(f"Yig'indisi: {result}")

