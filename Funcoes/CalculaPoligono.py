import math

def calculaArea (q, l):
    if q == 3:
        a = (l**2 * (math.sqrt(3))) / 4
        a = round (a, 2)
        poligono = "triângulo"
    elif q == 4:
        a = l ** 2
        a = round (a, 2)
        poligono = "quadrado"
    elif q == 5:
        a = (5 * l **2) /  (4 * math.tan(0.6283))
        a = round (a, 2)
        poligono = "pentágono"
    else:
        a = (3 * l ** 2 * math.sqrt(3)) / 2
        a = round (a, 2)
        poligono = "hexágono"
        
    return a, poligono

#---------------------------------------------------------

q = int (input ("Digite a quantidade de lados: "))

if q < 3:
    print ("Não é um poligono")
elif q > 6:
    print ("Poligono não identificado")
else:
    l = float (input ("Digite a medida do lado: "))
    a, poligono = calculaArea (q, l)
    print (f"O polígono é um {poligono} com área: {a}")
    