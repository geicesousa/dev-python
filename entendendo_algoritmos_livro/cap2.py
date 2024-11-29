def busca_menor(array):
    menor = array[0]
    menor_index = 0
    
    for i in range(1, len(array)):
        if array[i] < menor:
            menor = array[i]
            menor_index = i
    return menor_index



def ordenacao_por_selecao(arr):
    novo_array = []
    for i in range(len(arr)):
        menor = busca_menor(arr)
        novo_array.append(arr.pop(menor))
    return novo_array


print(ordenacao_por_selecao([24, 99, 98, 8, 36, 105,104, 6]))
print(ordenacao_por_selecao([2, 4, 1, 15, 48, 36, 10504, 3 , 98, 61]))