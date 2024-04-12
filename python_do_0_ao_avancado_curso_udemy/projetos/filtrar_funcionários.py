# usar sets
# criar 3 listas: 1- quem tem carro e trabalha a noite, 2 - tem carro e trabalha durante o dia, 3 - não tem carro

funcionarios = ['ana', 'marcos', 'alice', 'pedro', 'sofia', 'bruno', 'melissa']
trabalha_de_dia = ['ana', 'marcos', 'alice', 'melissa']
trabalha_de_noite = ['pedro', 'sofia', 'bruno']
possui_carro = ['marcos', 'alice', 'bruno', 'melissa']

funcionarios = set(funcionarios)
trabalha_de_dia = set(trabalha_de_dia)
trabalha_de_noite = set(trabalha_de_noite)
possui_carro = set(possui_carro)

lista1 = possui_carro & trabalha_de_noite
lista2 = possui_carro & trabalha_de_dia
lista3 = funcionarios ^ possui_carro
lista4 = funcionarios - possui_carro

print(lista1)
print(lista2)
print(lista3)
print(lista4)

# resolução curso
lista1 = set(possui_carro).intersection(trabalha_de_noite)
lista2 = set(possui_carro).intersection(trabalha_de_dia)
lista3 = set(funcionarios).difference(possui_carro)
lista4 = set(funcionarios).symmetric_difference(possui_carro)

print(lista1)
print(lista2)
print(lista3)
print(lista4)