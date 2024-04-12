lista = ['produtos', 2, 'variaveis', 8, 'aleatorios', 90]

item1, item2, item3, *outros = lista
print(item1)
print(item2)
print(item3)

print(outros)

item1, item2, *outros, item3 = lista

print(item1)
print(item2)
print(item3)

print(outros)

# armazena index com index
cores = ['verde', 'preto', 'roxo', 'azul', 'branco']

numeros = [1, 6, 12, 18, 24, 30]

print(zip(cores, numeros)) # coloca os itens agrupagos de acordo com os index

# metodo list transforma cada letra em um item
nome = 'Geice'

print(list(nome))

print(list(zip(cores, numeros)))

nova_lista = 'feijão, arroz, quiabo, macarrão, tomate, alho'

print(nova_lista.split(','))


