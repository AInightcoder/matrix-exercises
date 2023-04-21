import numpy as np

while True:

    n = int(input("N >>> "))
    m = int(input("M >>> "))

    # a = [[5*j for j in range(n)] for i in range(m)]

    matrix = np.zeros((m, n))
    data= ""
    for i in range(m):
        for j in range(n):
            data =matrix[i][j]=j*10
            print(data, end="\t")
        print()  