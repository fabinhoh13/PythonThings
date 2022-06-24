pressao = float (input("Digite a pressão atmosférica: "))
mols = 3
temperatura = float (input("Digite a temperatura (em graus celsius): "))
constante = 0.082

tempKelvin = temperatura + 273.15

volumeMetade = mols * tempKelvin * constante

volume = volumeMetade / pressao

print (f"{mols} mols de um gás a {temperatura} celsius e a {pressao} atm, ocupam {volume} litros")