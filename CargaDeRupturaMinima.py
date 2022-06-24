crp = float (input ("Valor padrão de carga de compressão: "))
n = int (input ("Número de amostras: "))

menor = 9999999999999999999999

i = 1
while (i <= n):
    area = float (input (f"Área da amortra {i} (cm2): "))
    peso = float (input (f"Peso da amostra {i} (cm2):"))

    crpAmostras = peso/area
    print (f"Antes do if {menor}")
    if crpAmostras < menor:
        print ("Achei um menor valor")
        menor = crpAmostras
    print (f"Depois do if {menor}")
    
    
    i+=1

print (f"CARGA DE RUPTURA MÍNIMA = {menor:.2f}")
if (crpAmostras >= crp):
    print ("Cimento aprovado.")
else:
    print ("Cimento reprovado.")