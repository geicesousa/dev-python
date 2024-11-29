def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = int((baixo+alto)/2)
        chute = lista[meio]
        
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None


lista = [1,3,5,7,9,11,89] 

print(pesquisa_binaria(lista, 7))
print(pesquisa_binaria(lista, 1))
print(pesquisa_binaria(lista, 11))
print(pesquisa_binaria(lista, 10))



