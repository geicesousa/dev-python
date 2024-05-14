# Crie uma matilha de 100 cachorros, de modo que todos tenham um nome formado da seguinte maneira: "Doguinho N" sendo N um numero entre 1 e 100. Para cada um nesses doguinhos uma idade aleatoria deve ser gerada.

from random import randint 

matilha = []
contador = 0

print('USANDO WHILE')
while len(matilha) < 100:    
    idade = randint(0,99)
    contador += 1
    matilha.append(f"Doguinho {contador}, idade {idade}")
    
print('\n'.join(matilha))
print()

print('USANDO LAÇO FOR')
for i in range(1,101):
    idade = randint(0,99)
    print(f'Doguinho {i}, idade {idade}')

