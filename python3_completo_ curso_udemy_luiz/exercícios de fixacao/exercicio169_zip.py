lista_1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_2 = ['BA', 'SP', 'MG', 'RJ']

def zipper(list1, list2):
    i = 0 
    for n in list1: # poderia usaro enumerate, mas o for teria n, m (que não seria usado), pois o enumerate tras o index e o valor
        try:
            print(list1[i] + ', ' + list2[i])
            i += 1
            
        except IndexError:
            
            return
            
zipper(lista_1, lista_2)


# resolução curso
def zipper(lista1, lista2):
    menor = min(len(lista1), len(lista2))
    return [ (lista1[i], lista2[i]) for i in range(menor)
    ] 
    
print(zipper(lista_1, lista_2))

# o zip retorna um objeto python
print(list(zip(lista_1, lista_2))) 

from itertools import zip_longest
print(list(zip_longest(lista_1, lista_2, fillvalue='Sem município')))