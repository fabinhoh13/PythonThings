from biblioteca import *

matriz = inputMatriz ("Martriz: ", int)

print (matriz)

lin, col = dimMatriz (matriz)

for i in range (lin):
    for j in range (col):
        print (f"{matriz[i][j]} ", end = "")
    print ()