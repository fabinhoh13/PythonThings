n = int (input ("Qual a dimensão do vetor: "))

vetor = []

print ("Leitura dos elementos do vetor...")

for i in range (n):
    elemento = float (input (f"Elemento [{i}]: "))
    vetor.append(elemento)
    
if (n == len(vetor)):
    print ("Tem o mesmo tamanho do que o tamanho passado")

media_aritmetica = 0
media_geometrica = 1

for i in range (len(vetor)):
    media_aritmetica += vetor[i]
    media_geometrica *= vetor[i]
media_aritmetica /= n
media_geometrica = media_geometrica ** (1/n)

print (vetor)

print (f"Media Aritmética: {media_aritmetica:.4f}")
print (f"Media Geométrica: {media_geometrica:.4f}")