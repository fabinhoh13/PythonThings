from math import sqrt

def calculaComprimento (reta):
    p = (reta["B"]["X"] - reta["A"]["X"]) ** 2
    s = (reta["B"]["Y"] - reta["A"]["Y"]) ** 2
    comprimento = sqrt(p + s)
    
    return round (comprimento, 2)

qntRetas = int (input ("Informe a quantidade de retas: "))
retas = []
for i in range (1, qntRetas + 1):
    print (f"Reta {i}:")
    Xa = float (input (" - Coordenada X de A: "))
    Ya = float (input (" - Coordenada Y de A: "))
    Xb = float (input (" - Coordenada X de B: "))
    Yb = float (input (" - Coordenada Y de B: "))
    reta = {"A": {"X": Xa, "Y": Ya},
            "B": {"X": Xb, "Y": Yb}
        }
    print ()
    retas.append(reta)

print ("Medidas das retas:")
for i in range (qntRetas):
    comprimento = calculaComprimento (retas[i])
    print (f" - Reta {i + 1}: {comprimento:.2f}")