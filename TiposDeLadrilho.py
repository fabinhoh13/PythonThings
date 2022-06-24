import math

tipo_ladrilho = int (input ("Qual o tipo de ladrilho (1/2/3)? "))

area_ladrilho = 0
area_total = 0
if (tipo_ladrilho == 1):
    area_ladrilho = 80
    area_total = float (input ("Qual a área (cm²) da sala? "))
    total_ladrilhos = area_total / area_ladrilho
    print (f"Quantidade de ladrilhos: {math.ceil(total_ladrilhos)}")

if (tipo_ladrilho == 2):
    area_ladrilho = 60
    area_total = float (input ("Qual a área (cm²) da sala? "))
    total_ladrilhos = area_total / area_ladrilho
    print (f"Quantidade de ladrilhos: {math.ceil(total_ladrilhos)}")


if (tipo_ladrilho == 3):
    area_ladrilho = 40
    area_total = float (input ("Qual a área (cm²) da sala? "))
    total_ladrilhos = area_total / area_ladrilho
    print (f"Quantidade de ladrilhos: {math.ceil(total_ladrilhos)}")

else: 
    print ("Tipo de ladrilho errado!")
