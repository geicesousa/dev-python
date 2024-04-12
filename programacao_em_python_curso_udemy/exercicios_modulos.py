import time as t # renomeando o módulo
import matplotlib.pyplot as plt 

tempos = []
vezes = []
vez = 1 

print('Você verá quantos segundos você gasta para digitar a palavra CACHORRO.')
input('Aperte enter para começar. Você deve digitar 3x.')

while vez < 4:
    iniciar = t.perf_counter() # a função clock() não existe mais no python3, a perf_counter() substitui
    input('Digite a palavra CACHORRO: ')
    final = t.perf_counter()
    tempo = round(final-iniciar, 2)
    tempos.append(tempo)
    vezes.append(vez)
    vez += 1

legenda = ['1ª', '2ª', '3ª', '4ª', '5ª']
plt.xticks(vezes, legenda)
plt.plot(vezes, tempos)
plt.show()