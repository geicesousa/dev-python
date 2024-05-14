name = input('Digite seu nome: ')
age = input('Digite sua idade: ')

if name and age:
    print(f'Seu nome é {name} e você tem {age} anos.')
    print(f'Seu nome invertido é {name[::-1]}.')
    print(f'A primeira letra de seu nome é {name[0]}.')
    print(f'A última letra de nome é {name[len(name)-1]}.')
    print(f'Seu nome tem {len(name)} letras.')
    if " " in name:
        print('Seu nome tem espaços')
    else:
        print('Seu nome não tem espaços')
            
else:
    print('Você deixou algum campo em branco...')