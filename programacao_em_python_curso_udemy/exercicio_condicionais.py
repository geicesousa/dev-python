nome = str(input('Nome: ')).lower()
nota_1 = float(input('Nota 1: '))
nota_2 = float(input('Nota 2: '))
faltas = int(input('Quantidade de faltas: '))

media = (nota_1 + nota_2) / 2
assiduidade = (20-faltas) / 20

print(f'''Estudante: {nome}
       Obteve média de {media} e {assiduidade * 100} % de presença.''')

if media > 6 and assiduidade >= 0.7:
    print(f'''Estudante: {nome} | Situação: Aprovad@''')

else: 
    print(f'''Estudante: {nome} | Situação: Reprovad@''')

