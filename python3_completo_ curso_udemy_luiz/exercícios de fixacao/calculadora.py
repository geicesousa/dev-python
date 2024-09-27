print('Bem-vinda! Nessa calculadora você pode apenas fazer contas simples. Vamos começar?!')

while True:
    numero1 = input('digite um número: ')
    numero2 = input('digite outro número: ')
    operacao = input('digite a operação: ')
    numeros_validos = None

    try:
        num_float1 = float(numero1)
        num_float2 = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None
        print('Você deve digitar números.')

    if numeros_validos is None:
        continue

    operadores_validos = '+-*/'

    if operacao not in operadores_validos:
        print('Operador inválido. Digite um sinal entre +, -, *, /')
        continue
  
    print('O resultado de sua conta é:')
    if operacao == '-':
        print(num_float1 - num_float2)
    elif operacao == '+':
        print(num_float1 + num_float2)
    elif operacao == '*':
        print(num_float1 * num_float2)
    elif operacao == '/':
        print(num_float1 / num_float2)
    
    sair = input('deseja sair? ').lower().startswith('s')

    if sair:
        break