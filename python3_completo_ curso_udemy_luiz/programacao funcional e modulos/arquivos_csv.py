# CSV - comma separated value (valores separados por vírgula), pode ser lido num editor de texto ou em planilha, 
# armazena dados em forma de tabela, cada linha é uma linha da tabela e as colunas são separadas por vírgula, não deve haver espaços entre as vírgulas e palavras
# extensão .csv

# nome,idade,endereço
# Geice,27,"Rua Brasil, Municipio-Estado, 38"
# Cleber,35,"Rio Vermelho, Salvador-Ba, nº 42"
# Gilberto,59,"Rua Barra, ""Centenário"", Salvador-Ba" # irá trazer centenário entre aspas

import csv
from pathlib import Path

CAMINHO = Path(__file__).parent

with open(CAMINHO/'exemplo.csv', 'r') as arquivo:
    leitor_csv = csv.reader(arquivo)
    for n in leitor_csv:
        print(n)

print()
    
with open(CAMINHO/'exemplo.csv', 'r') as arquivo:
    dict_csv = csv.DictReader(arquivo)
    for dic in dict_csv:
        print(dic)
        
               
# escrevendo num csv
#
lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]

chaves_colunas = lista_clientes[0].keys() #
valores_linhas = lista_clientes[0].values() #

with open(CAMINHO/'exemplo_csv.csv', 'w') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(chaves_colunas) #para dicionários usamos dictwhiter
    
    for linha in lista_clientes:
        escritor.writerow(linha.values())