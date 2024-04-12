nome = 'Geice'
i = 0
asterisco = '*'
new_name = ''
while i < len(nome):
    
    print(asterisco + nome[i] + asterisco)
    i += 1

#for
for letter in nome:
    all_letters = f'*{letter}'
    new_name += all_letters

print(new_name)

# calculadora 
while True:
    numero1 = input('digite um número:')
    numero2 = input('digite outro número:')
    operacao = input('digite a operação: ')

    try:
        numero1 = float(numero1)
        numero2 = float(numero2)

        if operacao == '-':
            print(numero1 - numero2)
        elif operacao == '+':
            print(numero1 + numero2)
        elif operacao == '*':
            print(numero1 * numero2)
        elif operacao == '/':
            print(numero1 / numero2)
    
        sair = input('deseja sair? ').lower().startswith('s')

        if sair:
            break

    except:
        print('você deve digitar números')


