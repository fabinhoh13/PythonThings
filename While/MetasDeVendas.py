meta_nacional = float (input ("Meta Nacional: R$ "))

contagem_nacional = 0
contador_estado = 1
while contagem_nacional < meta_nacional:
    nome_estado = input (f"Nome do estado {contador_estado}: ")
    meta_estadual = float (input ("Meta Estadual: R$ "))
    
    contagem_estadual = 0
    contador_cidade = 1
    while contagem_estadual < meta_estadual:
        venda_cidade = float (input (f"Venda na cidade {contador_cidade}: R$ "))
        contagem_estadual += venda_cidade
        contador_cidade += 1
    print (f"Meta no estado de {nome_estado} cumprida!")
    print (f"Total do estado: R$ {contagem_estadual:.2f}")
    contagem_nacional += contagem_estadual
    contador_estado += 1
print (f"Meta nacional cumprida!")
print (f"Total nacional: R$ {contagem_nacional:.2f}")
    