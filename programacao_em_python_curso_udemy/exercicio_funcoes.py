def calcula_imc(peso, altura):
    imc = peso / (altura * altura)
    return (imc)

# IMPORTANTE: em funções nas quais vamos usar o valor devemos semore usar o return, quando colocamos print e tentamos usar o resultado em outro lugar, aparece o seguinte erro: TypeError: '<' not supported between instances of 'NoneType' and 'float'

def mensagem_imc(sexo, peso, altura):
    resultado = calcula_imc(peso, altura)

    if sexo == 'f':
        if resultado < 19.1:
            return 'abaixo do peso'
        elif resultado > 19.1 or resultado <= 25.8:
            return ('no peso normal')
        elif resultado > 25.8 or resultado <= 27.8:
            return ('marginalmente acima do peso')
        elif resultado > 27.8 or resultado <= 32.3:
            return ('acima do peso ideal')
        elif resultado > 32.3:
            return ('obeso')
        else:
            return 'Houve um erro na execução do programa, tente novamente mais tarde.'


    if sexo == 'm':
        if resultado < 20.7:
            return('abaixo do peso')
        if resultado >20.7 or resultado <= 26.4:
            return('no peso normal')
        if resultado > 26.4 or resultado <= 27.8:
            return('marginalmente acima do peso')
        if resultado > 27.8 or resultado <= 31.1:
            return('acima do peso ideal')
        if resultado > 31.1:
            return('obeso')
        else:
            return 'Houve um erro na execução do programa, tente novamente mais tarde.'

print('Agora iremos calcular seu IMC!')

valida_sexo = False
while valida_sexo == False:
    informa_sexo = input('digite seu sexo: [F ou M] ').lower()

    if informa_sexo == 'f' or informa_sexo == 'm':
        valida_sexo = True
    else:
        print('Sexo inválido, digite F, para feminino ou M para masculino.')
        valida_sexo = False

valida_peso = False
while valida_peso == False:
    informa_peso = input('digite seu peso (use ponto para separar): ')
    
    try:
        informa_peso = float(informa_peso)
        if informa_peso <= 0 or informa_peso > 300:
            print('O peso deve ser um valor positivo e até 300kg')
        else:
            valida_peso = True

    except:
        print ('O peso deve ser numeral e kilos e gramas devem ser separados por "."')

valida_altura = False
while valida_altura == False:
    informa_altura = input('digite sua altura (use ponto para separar): ')

    try:
        informa_altura = float(informa_altura)
        if informa_altura <= 0 or informa_altura > 3.00:
            print('A altura deve ser um valor positivo e até 3.00')
        else:
            valida_altura = True
    
    except:
        print('A altura deve ser numeral e separar m e cm com ponto (".")')

# execução
resultado_imc = calcula_imc(informa_peso, informa_altura)
classificacao_imc = mensagem_imc(informa_sexo, informa_peso, informa_altura)

print (f'Seu IMC é: {resultado_imc:.2f}. Você está: {classificacao_imc}.')