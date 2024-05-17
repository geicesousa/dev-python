print(open('words.txt').readline())
print(open('words.txt').readline().strip())
linha = open('words.txt')
print(linha.readline()) # usando assim, cada vez que chama aparece um linha do arquivo
print(linha.readline().strip())
print()


# Escreva um programa que leia words.txt e imprima apenas as palavras com mais de 20 caracteres

for line in linha:
    if len(line) > 20:
        pass #   print(line)

# Escreva uma função chamada has_no_e que retorne True se a palavra dada não tiver a letra “e” nela.

def has_no_e(word):
    if 'e' not in word:
        return True
    
    return False
print(f'''has_no_e
{has_no_e('geice')}
{has_no_e('amanda')}''')

print()

# resolução do livro - tem o mesmo resultado
def has_no_e2(word): 
    for letter in word:
        if letter == 'e':
            return False
    return True


# Altere seu programa na seção anterior para imprimir apenas as palavras que não têm “e” e calcule a porcentagem de palavras na lista que não têm “e”.

for word in linha:
    for letter in word:
        if letter != 'e':
            print(word)
        

# Escreva uma função chamada avoids que receba uma palavra e uma série de letras proibidas, e retorne True se a palavra não usar nenhuma das letras proibidas.
            
def avoids(word, array):
    for l in array:
        if l not in word:
            return True
        
        return False

# resolução do livro - tem o mesmo resultado
def avoids2(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

print('avoids', avoids('geice', ['a', 'b', 'd']))
print('avoids', avoids('geice', ['i', 'b', 'e']))

print('avoids2', avoids2('geice', ['a', 'b', 'd']))
print('avoids2', avoids2('geice', ['i', 'b', 'e']))

def uses_only(word, array):
    for item in array:
        if item in word:
            return True
        return False

print('pato', uses_only('pato', ['a','p','t', 'o']))
print('pato', uses_only('pato', ['l', 'o']))

# Escreva uma função chamada is_abecedarian que retorne True se as letras numa palavra aparecerem em ordem alfabética

def is_abecedarian(word):
    if sorted(word) == list(word) :
        print('nesta palavra as letras estão em ordem alfabética')
        return True
        
    else:
        print('nesta palavra as letras são aleatórias')
        return False
print()
is_abecedarian('gol')
is_abecedarian('ano')
