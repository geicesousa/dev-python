lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]

def soma_itens( l1, l2):
    resultado = []
    for n in range(min(len(l1), len(l2))):
        resultado.append(l1[n] + l2[n])
    return resultado
         
    
print(soma_itens(lista_a, lista_b))

resultado = [ a + b for a, b in zip(lista_a, lista_b)]
print(resultado)
