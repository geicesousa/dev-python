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
