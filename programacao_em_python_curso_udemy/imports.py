import math

print(f'''{math.ceil(3.2)} #arredonda para mais
{math.floor(3.7)} #arredonda para menos
{math.fsum([1,2,3,4])} #soma todos os itens
''')
import time
print(f''' {time.localtime()} #mostra dia e horário local com minutos e segundos, semana do ano
{time.localtime().tm_hour}
{time.localtime().tm_min}
{time.localtime().tm_mday}

 ''')

import random # selecionar itens aleatórios

print(random.randint(0,12),
random.randrange(1,5))
# randint inclui o número de parada

def megasena():
    jogo = []
    while len(jogo) < 6:
        num = random.randint(1,99)
        if num in jogo:
            continue
        else:
            jogo.append(num)
    
    print(jogo)
    print(sorted(jogo))

megasena()
print()
megasena()
print()
megasena()

#se salvarmos um arq na pasta lib do python no pc, conseguimos usar o arquivo que criamos como módulo built-in