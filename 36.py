import numpy as np

arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [5, 6, 7, 8],
]

matrix = np.array(arr)

def find_similar_row(matrix):
    global counter  # Declare counter as global
    counter = 0
    for row in matrix[1:]:
        for i in range(len(matrix[0])):
            if matrix[0, i]==row[i]:
                counter+=1   
    print(counter/4)

find_similar_row(matrix)
