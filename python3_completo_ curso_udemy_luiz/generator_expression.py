# iterator é uma classe, ela entrega apenas o próximo elemento
# generator é uma função que sabe pausar, todo generator é um iterator, mas nem todo iterator é um generator
# generator não esta na memória do pc
import sys

lista = [n for n in range(100)]
generator = (n for n in range(100))
print(generator)
print(sys.getsizeof(lista)) # retorna o valor ocupado em bytes na memória
print(sys.getsizeof(generator))
print()

# generator functions, yield indica onde o generator deve parar
# há yield from que direciona para função geradora
def generator(n, max):
    while True:
        yield n 
        
        n+=1
        
        if n>max:
            break

gen = generator(1,10)

print(list(gen))
print(list(gen)) #aqui está vazio, quando chega ao fim mostra limpa pq não armazena
