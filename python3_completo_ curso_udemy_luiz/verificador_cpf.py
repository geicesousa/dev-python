# pegar os 9 primeiros números e multiplicar de a partir de 10 e em ordem descrescente, soma tudo
# multiplica o resultado (de cima) por 10 
# obtem o resto da divisão (de cima) por 11
# se o resultado for > 9, resultado vai ser 0, se o resultado for <= 9, resultado vai ser o valor encontrado na divisão
#
# 

CPF = '336.780.630-71' 
CPF2 = '74473188507'
CPF3 = '009.628.875-28' 
CPF4 = '00962887528'

# refatoração: 
# insery try e except
# verificar se os numeros são repetidos

def valida_cpf(cpf):
    
    remove_ponto = cpf.replace('.', '').replace('-','')
    primeiros_9_digitos = remove_ponto[:9] #pega do início até o 9º item

    # confirma o primeiro dígito
    cont = 0
    multiplicador = 10
    digitos_somados = 0

    while cont < len(primeiros_9_digitos):
        digitos_somados += int(primeiros_9_digitos[cont])*multiplicador
        cont += 1
        multiplicador -= 1

    digito_um = (digitos_somados * 10) % 11
    #digito_um = digito_um if digito_um <= 9 else 0
    if digito_um > 9:
        digito_um = 0
    else:
        digito_um = digito_um


    # confirma o 2º digito
    primeiros_10_digitos = remove_ponto[:10] # primeiros_9_digitos + str(digito_um)
    multiplicador2 = 11
    digitos_somados2 = 0
    cont2 = 0

    while cont2 < len(primeiros_10_digitos):

        digitos_somados2 += int(primeiros_10_digitos[cont2])*multiplicador2
        cont2 += 1
        multiplicador2 -=1

    digito_dois = (digitos_somados2 * 10) % 11
    print(digito_dois)    
    digito_dois = digito_dois if digito_dois <= 9 else 0
    print(digito_um, digito_dois)    

