# um dict é um conjunto de valores não ordenados, agrupados sempre como chave:valor
# um dicionario não tem index, usamos o nome da chave para acessar a chave que desejamos
# um dicionário não itera, como iteraria se não tem index?!

geice = { 'nome': 'geice', 'sobrenome': 'sousa pinho', 'profissão': 'software engineer', 'idade': 31, 'filhos': ['akin']}

print(type(geice))
print(geice['idade'])
print(geice['profissão'])
print(geice['filhos'])
geice['filhos'].append('zuri') #adiciona na lista de filhos
# geice['filhos'] = 'zuri' #substitui para 'zuri'
print(geice['filhos'])
print('sobrenome' in geice)
print('formação' in geice)
print()

# imprimindo chave e valor usando for-loop
for chave in geice:
    print(f'{chave}: {geice[chave]}') 

print()

print(geice.get('sobrenome', 'chave inexistente'))
print(geice.get('nacionalidade', 'chave inexistente'))

# exercicio
print()

cores = { 'vermelho': 'red', 'verde': 'green', 'verde-escuro': 'dark-green', 'laranja': 'orange', 'rosa': 'pink', 'roxo': 'purple'}

vermelho = cores.get('vermelho', 'cor não encontrada')
amarelo = cores.get('amarelo', 'cor não encontrada')

print(vermelho)
print(amarelo)
print()

