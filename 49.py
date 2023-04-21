import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [10, 11, 1],
                   [13, 14, 15]])

sorted_matrix = np.sort(matrix)
new_arr=[]
for row in sorted_matrix:
    copy_element = np.copy(row[-1])
    min_element = row[0]
    max_element = row[-1]

    row[-1]=min_element
    row[0]=copy_element
    new_arr.append(row)

new_matrix=np.array(new_arr)
print(new_matrix)   