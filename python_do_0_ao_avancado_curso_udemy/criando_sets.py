# sets são similares a listas, mas não permite que os itens se repitam e ordenam os números, não usa index, possui operadores para mostrar a diferença entre as listas, para unir, para mostrar o que tem igual

cores = ['verde', 'roxo', 'azul', 'vermelho']
cores2 = ['verde', 'preto', 'roxo', 'azul', 'branco']
numeros = [1, 6, 12, 18, 24, 30]
numeros2 = [10, 6, 120, 108, 24, 30]

lista1 = set(numeros)
lista2 = set(numeros2)
cor = set(cores)
cor1 = set(cores2)

print(lista1 , 'type:', type(lista1))
print(lista2)

print()
print(lista1 | lista2) #union
print(lista1 - lista2) #diference
print(lista1 ^ lista2) #symetric diference
print(lista1 & lista2) #and

print()
print(cor1 | cor) 
print(cor1 - cor) 
print(cor1 ^ cor) 
print(cor1 & cor)

# dá pra criar um set manualmente, mas não dá pra criar um set vazio {}, pois isso informa ao python que é um dicionário
set_1 = {7,5,8,9,6,6,3,4,3,2,1}
# set.discard - se o item não existir ignora
# set.remove - se o item não existir apresenta um erro
print(set_1)
print()
print(set_1.union(lista1))
print(set_1.union(lista1, lista2))