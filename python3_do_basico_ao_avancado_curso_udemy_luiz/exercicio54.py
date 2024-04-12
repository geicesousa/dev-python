#1 
number = input('digite um número inteiro: ') or 10
print(number.isdigit()) # retorna true ou false para numeros inteiros
try:
    number_int = int(number)
    if number_int % 2 == 0:
        print('este número é par')
    else:
        print('este número é ímpar')
except:
    print('vc tem que digitar um número inteiro')
#2 
horario = input('digite um horário: ')

try:
    horario = float(horario)
    if horario > 0 and horario < 12:
        print('bom dia')
    elif horario > 11 and horario < 18:
        print('boa tarde')
    elif horario > 17 and horario < 23:
        print('boa noite')
except:
    print('horário inválido')

#3
nome = input('seu nome')

if len(nome) >= 1 and len(nome) <= 4:
    print('seu nome é curto')
elif len(nome) > 4 and len(nome) <= 7:
    print('seu nome é normal')
else:
    print('seu nome é muito grande')
