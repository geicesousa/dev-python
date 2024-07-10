# arquivos csv - comma separated values - armazenam dados tabulares

import csv
from pathlib import Path

root = Path(__file__).parent

try:
    with open(root / 'tabela.txt', 'w', newline='', encoding='utf-8') as arquivo:
        arq_csv = csv.writer(arquivo)
        arq_csv.writerow(['id', 'nome']) # writerow é próprio do csv e recebe um iterável
        arq_csv.writerow(['1', 'francisca'])
        arq_csv.writerow(['2', 'maria'])

except IOError as exc:
    print(exc)

try:
    with open(root / 'tabela.txt', 'r') as arquivo:
        ler_csv = csv.reader(arquivo)
        for row in ler_csv:
            print(row)
except IOError as exc:
    print(exc)