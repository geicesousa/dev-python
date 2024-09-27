# aumentar os preços em 10%
# gerar novos_produtos por deep copy (copy.copy)
# ordenar os produtos por ordem descrescente
# gerar produtos_ordenados_por_nome por deep copy 
# ordenar produros por preço crescente
# gerar produtos ordenados por preço por deep copy  

import copy

produtos = [
    {'nome': 'Produto 9', 'preco': 10.00},
    {'nome': 'Produto 5', 'preco': 22.32},
    {'nome': 'Produto 2', 'preco': 10.11},
    {'nome': 'Produto 7', 'preco': 105.48},
    {'nome': 'Produto 1', 'preco': 87.50},
    {'nome': 'Produto 8', 'preco': 512.00},
] 

copia_produtos =  [{**p, 'preco': round(p['preco']*1.1, 2)} for p in copy.deepcopy(produtos)]
# deepcopy cria uma cópia real e garante que não alteremos os produtos originais
print(*copia_produtos, sep ='\n')
   
produtos_ordenados_por_nome = sorted(copia_produtos, key = lambda p: p['nome'])
print()
print(*produtos_ordenados_por_nome, sep = '\n')
print()

produtos_ordenados_por_preco = sorted(copia_produtos, key = lambda p: p['preco'])
print(*produtos_ordenados_por_preco, sep= '\n')