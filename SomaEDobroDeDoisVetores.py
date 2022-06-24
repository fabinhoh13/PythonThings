n = int (input ("Qual a dimensão dos vetores: "))

vetor1 = []

print ("Leitura do primeiro vetor...")

for i in range (n):
    elemento = float (input (f"Elemento [{i}]: "))
    vetor1.append(elemento)

vetor2 = []

print ("Leitura do segundo vetor...")

for i in range (n):
    elemento = float (input (f"Elemento [{i}]: "))
    vetor2.append(elemento)
    
vetor3 = []

for i in range (n):
    elemento = (vetor1[i] + vetor2[i]) * 2
    vetor3.append(elemento)
    
print ("Vetor 1")
print (vetor1)
print ("Vetor 2")
print (vetor2)
print ("Vetor 3")
print (vetor3)