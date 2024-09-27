import random 

def gerador_cpf():
    numeros_gerados = ''
    for n in range(9):
        numeros_gerados += str(random.randint(0,9))

    len_cpf = len(numeros_gerados)
    
    dez_digitos = numeros_gerados[:10] 
    cont = 0
    cont2 = 0
    multiplicador = 10
    multiplicador2 = len_cpf
    digitos_somados = 0
    digitos_somados2 = 0
    
    while cont < len(numeros_gerados):
        digitos_somados += int(numeros_gerados[cont])*multiplicador
        cont += 1
        multiplicador -= 1
   
    digito_um = (digitos_somados * 10) % len_cpf
    digito_um = digito_um if digito_um <= 9 else 0  
    
    dez_digitos = numeros_gerados + str(digito_um)

    while cont2 < len(dez_digitos):
            digitos_somados2 += int(dez_digitos[cont2])*multiplicador2
            cont2 += 1
            multiplicador2 -=1
    digito_dois = (digitos_somados2 * 10) % len_cpf
    digito_dois = digito_dois if digito_dois <= 9 else 0
    
    cpf_gerado = f'{numeros_gerados}{digito_um}{digito_dois}'
    
    return cpf_gerado
