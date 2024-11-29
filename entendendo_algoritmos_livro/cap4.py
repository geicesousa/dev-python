# como usar recursão para somar todos os número dentro de um array
numeros = [1,2,3,4]

soma = 0
for n in numeros:
    soma += n
print(soma)    

def soma_recursiva(array):
    tamanho = len(array)
    if tamanho == 0:
        return 0
    else:
        return array[0] + soma_recursiva(array[1:])
    
print(soma_recursiva(numeros))

# função recursiva que conta os itens de uma lista
for n in enumerate(numeros):
    print(n[0]+1)
print('fim')
 
def conta_itens(lista):
    if lista == []:
        return 0
    else:
        return 1 + conta_itens(lista[1:])

lista = [5,6,3,21,55,6,4]
print(conta_itens(lista))

# valor mais alto em uma lista
def maior_valor(lista):
    maior = 0
    for n in lista:
        if n > maior:
            maior = n
    return maior

def outro_maior_valor(lista):
    maior = lista[0]
    
    for n in range(len(lista)-1):
        if lista[n] > maior:
            maior = lista[n]
    return maior  
    
maior_n = maior_valor(lista)
print(maior_n)

def quicksort(array): 
    if len(array) < 2: # se o array tiver 1 ou 0 itens, então ele já está ordenado
        return array 
    else:
        pivo = array[0] # número usado como referência
        menores = [i for i in array[1:] if i <= pivo]
0         maiores = [i for i in array[1:] if i > pivo]
        
        return quicksort(menores) + [pivo] + quicksort(maiores)
    

print(quicksort([8,39,9,1,4,5,2,0,63,7,85,67,14,10,27,32,3,2]))