frase = 'meu amor, essa é a última oração, pra salvar meu coração, coração não é tão simples quanto pensa'
frase_split = frase.split()
frase_split2 = frase.split(',')
print(frase_split)
print()
print(frase_split2)
    
print()
usando_join = '*'.join(frase_split2)
print(usando_join)

#desempacotamento em chamadas de funções

lista = [1, 6, 0, 'caracol', 'borboleta', 'abelha']
print(1, 6, 0, 'caracol', 'borboleta', 'abelha')
print(*lista)