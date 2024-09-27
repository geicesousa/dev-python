frase = 'Python é uma linguagem multiparadigma' \
'fortemente tipada e dinâmica.' \
'A linguagem de programação Python foi criada por Guido van Rossum' # \ dá continuidade a string

i = 0
qtd_letra_apareceu = 0
letra_mais_encontrada = ''
count = ''

while i < len(frase):

    letra_atual = frase[i]
    count_letra_apareceu = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if qtd_letra_apareceu < count_letra_apareceu:
        qtd_letra_apareceu = count_letra_apareceu
        letra_mais_encontrada = letra_atual

    i += 1
   

print(f'A letra que apareceu mais vezes foi {letra_mais_encontrada}. Ela apareceu {qtd_letra_apareceu} vezes.')

