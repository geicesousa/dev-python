import json


print('''
    [L] listar 
    [D] desfazer 
    [R] refazer 
    [A] adicionar
    [S] sair
''')

lista_de_tarefas = ['comprar pão', 'buscar remédio']
lista_tarefas_refazer = []


# def listar(lista):
    # if lista is None:
    #     return 'Não há itens na lista'
    # print('Tarefas: ')
    # for index, item in enumerate(lista):
    #     return index, item
    # print()

def adicionar(tarefa):
    return lista_de_tarefas.append(tarefa)
    
while True:
    opcao = input('selecione a opção desejada: ').lower()
    if opcao == 'l' or opcao == 'listar':
        if not lista_de_tarefas:
            print('Não há itens na lista')
            break
        
        print('Tarefas: ')
        for index, item in enumerate(lista_de_tarefas):
            print(index, '-', item)
        
        print()
        continue

        
    elif opcao == 'd' or opcao == 'desfazer':
        remove_tarefa = lista_de_tarefas.pop()
        lista_tarefas_refazer.append(remove_tarefa)
        print(lista_de_tarefas)
        continue

    elif opcao == 'r' or opcao == 'remover':
        if not lista_de_tarefas:
            print('A lista está vazia')
            break
        if not lista_tarefas_refazer:
            print('Não há o que refazer')
            continue
        tarefa_refeita = lista_tarefas_refazer.pop()
        lista_de_tarefas.append(tarefa_refeita)
        print(lista_de_tarefas)
        continue
    
    elif opcao == 'a' or opcao == 'adicionar':
        tarefa = input('digite a tarefa que deseja inserir: ')
        
        lista_de_tarefas.append(tarefa)
        
        with open('lista_tarefas.json', 'w') as arquivo:
            json.dump(lista_de_tarefas, arquivo, indent=2, ensure_ascii=False)
        
    
        continue
    else:
        print('ocorreu um erro inesperado')
        break


    