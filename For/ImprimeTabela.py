import math

print ("X/Y|", end="")
for y in range (3, 25, 3):
    print (f"{y:11.0f}", end="")
print ("\n---------------------------------------------------------------------------------------------")

for x in range (2, 31, 2):
    print (f"{x:2.0f} |", end="")
    for y in range (3, 25, 3):
        if ((x + y) % 2 == 0):
            resultado = (1/(x*y)) + math.sin(x+y)
        elif ((x*y) % 2 != 0):
            resultado = ((y**2)-(4*x))**(1/2)
        else:
            resultado = (x+y)**(1/3)
        print (f"{resultado:10.2f} ", end ="")
    print ()



