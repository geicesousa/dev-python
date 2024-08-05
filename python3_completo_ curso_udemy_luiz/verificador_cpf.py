# pegar os 9 primeiros números e multiplicar de a partir de 10 e em ordem descrescente, soma tudo
# multiplica o resultado (de cima) por 10 
# obtem o resto da divisão (de cima) por 11
# se o resultado for > 9, resultado vai ser 0, se o resultado for <= 9, resultado vai ser o valor encontrado na divisão

from numbers import Number
# import re

CPF = '336.780.630-71' 
CPF2 = '74473çp188507'
CPF3 = '00000000000' 
CPF4 = '089524925748'

def valida_cpf(cpf):
    # cpf_cru = re.sub(r'[^0-9]', '', cpf)
    cpf_cru = cpf.replace('.', '').replace('-','')
    len_cpf = len(cpf_cru)
    verifica_digitos = cpf_cru.isdigit()
    
    verifica_igualdade = cpf_cru[0] * len_cpf == cpf_cru   

    primeiros_9_digitos = cpf_cru[:9] #pega do início até o 9º item
    primeiros_10_digitos = cpf_cru[:10] 
    cont = 0
    cont2 = 0
    multiplicador = 10
    multiplicador2 = len_cpf
    digitos_somados = 0
    digitos_somados2 = 0
    
    if verifica_igualdade:
        return 'Os números não podem ser repetidos'
    
    elif verifica_digitos:
        #---confirma 1º dígito---#
        while cont < len(primeiros_9_digitos):
            digitos_somados += int(primeiros_9_digitos[cont])*multiplicador
            cont += 1
            multiplicador -= 1
        #---confirma 2º digito---#
        while cont2 < len(primeiros_10_digitos):
            digitos_somados2 += int(primeiros_10_digitos[cont2])*multiplicador2
            cont2 += 1
            multiplicador2 -=1

        digito_um = (digitos_somados * 10) % len_cpf
        digito_um = digito_um if digito_um <= 9 else 0  

        digito_dois = (digitos_somados2 * 10) % len_cpf
        digito_dois = digito_dois if digito_dois <= 9 else 0
        
        cpf_validado = f'{primeiros_9_digitos}{digito_um}{digito_dois}'
        
        
        return f'O CPF é válido' if cpf_validado == cpf_cru else 'O CPF não é válido'

    else:
        return 'Você precisa digitar apenas números e eles não podem ser repetidos'


#cpf_digitado = input('Digite um CPF: ')
cpf1 = valida_cpf(CPF)
cpf2 = valida_cpf(CPF2)
cpf3 = valida_cpf(CPF3)
cpf4 = valida_cpf(CPF4)

print(cpf1)
print(cpf2)
print(cpf3)
print(cpf4)
#print(valida_cpf(cpf_digitado))
