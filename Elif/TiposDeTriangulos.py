angulo1 = int (input ("Digite o primeiro angulo interno: "))
angulo2 = int (input ("Digite o segundo angulo interno: "))
angulo3 = int (input ("Digite o terceiro angulo interno: "))

if angulo1 + angulo2 + angulo3 == 180:
    if (angulo1 == 90) or (angulo2 == 90) or (angulo3 == 90):
        print ("Triangulo Retangulo")
    elif (angulo1 > 90) or (angulo2 > 90) or (angulo3 > 90):
        print ("Triangulo Obtusangulo")
    else:
        print ("Triangulo Acutangulo")
else:
    print ("Triangulo Inexistente")