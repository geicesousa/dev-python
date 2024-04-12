# a função eval recebe uma string como parametro, tudo o que tiver escrito é interpretado como código python, como se tivesse escrito no código [print('Olá, mundo!')" retorna -> Olá, mundo!]

def eval_loop():
    new_data = ''

    while True:
        data = input('digite algo ')
        if data == 'done':
            print('fim')
            break    
                
        new_data = eval(data)
        print(new_data)
        print(eval('type(data)'))

    if new_data != '': # aqui usei gpt
        print(new_data)

eval_loop()
