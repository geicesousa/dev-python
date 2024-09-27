def print_iter(iterator):
    print(*list(iterator), sep='\n')
    
produtos = [
    {'nome': 'Produto 9', 'preco': 10.00},
    {'nome': 'Produto 5', 'preco': 22.32},
    {'nome': 'Produto 2', 'preco': 10.11},
    {'nome': 'Produto 7', 'preco': 105.48},
    {'nome': 'Produto 1', 'preco': 87.50},
    {'nome': 'Produto 8', 'preco': 512.00},
] 

novos_produtos = [ {**p, 'preco': p['preco'] *1.5} for p in produtos ]

novos_produtos_map = map(lambda a: (a['nome'], a['preco']), produtos)

print_iter(novos_produtos_map)

filtro_produtos = [ p for p in produtos if p['preco'] > 30] # para filtrar a condição vem depois

novos_produtos_filter = filter(lambda a: a['preco'] >= 50, produtos)

print_iter(filtro_produtos)

# reduce não é builtin, temos que importar, é uma boa prática usar o valor inicial para termos um valor inicial no acumulador e delimitar o tipo que iremos usar 
from functools import reduce

total = 0 
for p in produtos:
    total += p['preco']
print(total)

produtos_reduce = reduce(lambda ac, prod: ac + prod['preco'], produtos, 0)

print(produtos_reduce)