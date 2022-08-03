import math

s1 = float (input ("Digite o lado 1 do triangulo (m): "))
s2 = float (input ("Digite o lado 2 do triangulo (m): "))
s3 = float (input ("Digite o lado 3 do triangulo (m): "))

perimetro = s1 + s2 + s3

s = perimetro / 2.0

area = s * (s - s1) * (s - s2) * (s - s3)

area = math.sqrt(area)

print (f"Perimetro do triangulo = {perimetro} m")
print (f"Área do triangulo = {area} m^2")

