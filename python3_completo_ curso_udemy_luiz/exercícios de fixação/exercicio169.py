lista_1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_2 = ['BA', 'SP', 'MG', 'RJ']

def zipper(list1, list2):
    i = 0 
    for n in lista1:
        try:
            return list1[i] + ', ' + list2[i]
            i += 1
        except IndexError as e:
            print(e)
            return
            
zipper(lista_1, lista_2)

# resolução curso

def zipper(lista1, lista2):
    menor = min(len(lista1), len(lista2))