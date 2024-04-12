# usar id e elif
# < 18,5  magreza | 18,5 - 24,9 normal | 25,0 - 29,9 sobrepeso | 30,0 - 39,9 obesidade | > 40,0 obesidade grave
# 
# 

info1 = input('Qual a sua altura? ')
info2 = input('Qual a seu peso? ')

def calcula_imc(altura, peso):
    return peso / altura ** 2

try:
    altura = float(info1)
    peso = float(info2)
except:
    print('Peso e altura devem ser valores numéricos e separados por ponto (ex.: 1.64)')

else:

    resultado_imc = calcula_imc(altura, peso)
    print(resultado_imc)


    if resultado_imc < 18.5:
        print('Magreza')

    elif resultado_imc >= 18.5 and resultado_imc <= 24.9:
        print('Normal')

    elif resultado_imc >= 25.0 and resultado_imc <= 29.9:
        print('Sobrepeso')

    elif resultado_imc >= 30.0 and resultado_imc <= 39.9:
        print('Obesidade')

    else:
        print('Obesidade grave')
