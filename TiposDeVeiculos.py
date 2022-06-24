#1 carro  3volks 4 fiat 
#2 moto 5 honda 6 yamaha

tipoAutomovel = int (input ("Digite o tipo de automovel"))
if (tipoAutomovel == 1):
    marcaAutomovel = int (input ("Digite a marca do carro"))
    if (marcaAutomovel == 3):
        print ("Volks")
    else:
        print ("Fiat")
if (tipoAutomovel == 2):
    marcaAutomovel = int (input ("Digite a marca da Moto"))
    if (marcaAutomovel == 5):
        print ("Honda")
    else:
        print ("Yamaha")