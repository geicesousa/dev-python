from itertools import count, combinations, permutations, product, groupby

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    
# count é um iterador infinito, o contador eterno
grupo = ['silas', 'thiago', 'ricardo', 'mario', 'pedro', 'luiz']
combinacao = combinations(grupo, 3) #ordem não importa
print_iter(combinacao)

permutacao = permutations(grupo) #ordem importa
print_iter(permutacao)

print()

camisetas = [['preta', 'branca'], ['algodão', 'poliéster'], ['p','m','g']]
produtos = product(*camisetas)
print_iter(produtos)

# para agrupar usando o groupby, a lista deve estar ordenada
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

def ordem(aluno):
    return aluno['nota']

alunos_ordenados = sorted(alunos, key= ordem)
grupos = groupby(alunos_ordenados, key= ordem)

print()
for chave, grupo in grupos:
    print(chave + ')', list(grupo))