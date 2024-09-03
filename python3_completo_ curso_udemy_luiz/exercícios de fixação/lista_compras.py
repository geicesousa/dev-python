# TODO: fazer uma lista de comprar
# usuário deve poder inserir, apaga e listar os itens
# o programa não deve apontar erros por index inexistentes
import os

lista_atualizada = ['feijao', 'carne', 'sal'] 
print('Bem-vinde! O que deseja fazer?')
sair = 'n'
while sair == 'n':
    opcao = input('''
        [a]pagar
        [i]nserir
        [l]istar
        ''').lower()
    
    try:
        if opcao == 'a':
            os.system('clear') #vai limpar o terminal
            item = input('Digite o nome do item que deseja apagar: ').lower()
            lista_atualizada.remove(item)

        elif opcao == 'i':
            os.system('clear')
            item = input('Digite o nome do item que deseja inserir: ').lower()
            lista_atualizada.append(item)

        elif opcao == 'l':
            os.system('clear')
            if len(lista_atualizada) == 0:
                print('Lista vazia')
                
            else:
                for index, item in enumerate(lista_atualizada):
                    print(index, item)
            
        else:
            print('Você precisa digitar uma opção válida [a, i ou l]')   
            continue 
        
    except ValueError: # o indicado é tratar cada exceção específica e não except puro
        print('Valor não encontrado.')
        continue
    
    except Exception:
        print('Ocorreu um erro desconhecido')
        
    sair = input('Deseja sair? [s/n]').lower()
    if sair == 's':
        break