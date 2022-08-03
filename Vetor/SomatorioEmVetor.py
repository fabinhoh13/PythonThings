v = []
elemento = int (input ("Digite um valor -->  "))
while elemento >= 0:
    v.append (elemento)
    elemento = int (input ("Digite um valor -->  "))

sa = []
for i in range (len(v)):
    somatorio = 0
    for j in range (i + 1):
        somatorio += v[j]
    sa.append(somatorio)

print (v)
print (sa)