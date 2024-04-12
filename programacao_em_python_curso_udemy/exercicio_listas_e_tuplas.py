# mês de nascimento
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro') # tupla, uma lista imutável

data_nascimento = input('digite sua data de nascimento: ')

mes_nascimento = data_nascimento[3] + data_nascimento[4]
print(f'Você nasceu no mês de {meses[int(mes_nascimento)-1]}')

# resolução dada no curso
indice = int(data_nascimento[3:5]) - 1 # slicing
mes = meses[indice]

print(f'Você nasceu no mês de {mes}')
