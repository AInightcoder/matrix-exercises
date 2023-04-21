import  numpy as np

matrix = np.arange(10, 50).reshape(10, 4)
print(matrix)

avr=sum(sum(matrix))/40

print(avr)
closed_element = None
eng_kichigi = matrix[0][0]

for i in matrix:
    for j in i:
        distence= abs(j-avr)
        if distence<eng_kichigi:
            eng_kichigi=distence
            closed_element=j

print(closed_element)