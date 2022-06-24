def realizaCalculos (num_termos, raio):
    pi = 0
    for i in range (0, num_termos):
        pi += ((-1)**i) * (4/(2 * i + 1))
    volume = (4/3) * pi * (raio ** 3)
    
    return round (pi, 5), round (volume, 5)


n = int (input ("Número de termos: "))
r = int (input ("Raio da esfera: "))

pi, volume = realizaCalculos (n, r)

print (f"pi = {pi}")
print (f"Volume da esfera = {volume}")