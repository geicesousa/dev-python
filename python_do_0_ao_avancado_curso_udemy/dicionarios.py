dicionario = {'nome': 'geice', 'idade': 31, 'nacionalidade': 'brasileira', 'genero': 'feminino'}

print(dicionario['nome'])
print()
dicionario.update({'escolaridade': 'superior completo'}) #update atualiza e adiciona
print(dicionario)
dicionario.update({'idade': 27})
print()
print(dicionario)

for keys in dicionario:
    print(keys)
print()

for item in dicionario.items(): # retorna uma tuple e não podemos manipular
    print(item)
print()

for keys, values in dicionario.items(): # retorna dois valores que permitem manipulação
    print(keys, values)

print()
print(dicionario.get('nome'))
print(dicionario.get('endereço'))
print(dicionario.items())
print(dicionario.keys())

print()
print()

# update (dict) e append (list)
# Lista inicial de dicionários
lista_de_dicionarios = [
    {'nome': 'João', 'idade': 30},
    {'nome': 'Maria', 'idade': 25}
]

# Adicionar um novo campo 'email' ao segundo dicionário na lista
# para modificar usamos a mesma lógica
lista_de_dicionarios[1]['email'] = 'maria@example.com'

# Exibir a lista atualizada
print(lista_de_dicionarios)

## Lista inicial de dicionários
lista_de_dicionarios = [
    {'nome': 'João', 'idade': 30},
    {'nome': 'Maria', 'idade': 25}
]

# Novo dicionário a ser adicionado
novo_dicionario = {'nome': 'Pedro', 'idade': 28}

# Adicionar o novo dicionário à lista
lista_de_dicionarios.append(novo_dicionario)

# Exibir a lista atualizada
print(lista_de_dicionarios)
