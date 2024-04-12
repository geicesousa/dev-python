lista = [1,2,3,4,5,6]


def multiplicar(x):
    return x * 2

multiplicados = map(multiplicar, lista) # recebe uma função e um iterável (lista, array, tupla)

print(list(multiplicados)) #resultado das multiplicações

print(multiplicados) # aqui retorna o objeto

print()

print(list(map(lambda x: x *2, lista)))

print(list(map(lambda x: x *2, [9,8,7])))

numeros = [20,35,98,67,61,58,81,72,10,18,13]

def menores_50(x):
    return x < 50

print()
print(list(filter(menores_50, numeros)))
print(list(filter(lambda x: x > 50, numeros)))

print()

# list comprehension com string

aleatorios = ['nome', 'banana', 'pessego', 'vatapa', 'banana da terra', 'cama', 'geladeira']
teste = [item for item in aleatorios if 'r' in item] # retorna o item para cada item em aleatorios se r estiver em item
print(teste)

print()
valores = [ num+2 for num in numeros]
print(valores)

from sys import getsizeof #verifica o tamanho de memória ocupada
#generator expressions melhora a performace pois ocupa menos estaço na memória, basta usar () no lugar de []

dez_em_dez = [x * 10 for x in range(100)]
print(type (dez_em_dez))
print(getsizeof(dez_em_dez))


print()

dez_em_dez = (x * 10 for x in range(100))
print(type (dez_em_dez))
print(getsizeof(dez_em_dez))
