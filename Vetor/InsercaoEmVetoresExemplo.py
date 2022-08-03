v = []
aux = int (input ("Digite o valor a ser inserido: "))
while aux >= 0:
    v.append(aux)
    aux = int (input ("Digite o valor a ser inserido: "))
v2 = []
for i in range (len (v)):
    aux1 = 0
    for j in range (i + 1):
        aux1 += v[j]
        
    v2.append(aux1)
print (v2)