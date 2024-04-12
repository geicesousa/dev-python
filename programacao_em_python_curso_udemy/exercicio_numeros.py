nota_1 = float(input('digite a primeira nota: '))
nota_2 = float(input('digite a segunda nota: '))
peso_1 = float(input('peso da primeira prova: '))
peso_2 = float(input('peso da segunda prova: '))

media_poderada = ((nota_1*peso_1) + (nota_2 * peso_2)) / (peso_1 + peso_2)

print(f'A média ponderada é: {media_poderada}')
