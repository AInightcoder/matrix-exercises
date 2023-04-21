import  numpy as np

matrix = np.arange(10, 26).reshape(4,4)
print(matrix)
result = 1
[result:=result*i for i in matrix[:, :]]

print(result)
print(f"MIN: {min(list(result))}, Index: {list(result).index(min(result))}")


