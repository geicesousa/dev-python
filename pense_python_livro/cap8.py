fruit = "amora"
index = 0

# while index < len(fruit):
#     index = index - 1
#     letter = fruit[index]
#     print(letter, index) #apresenta erro de range no final
    
prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        print(letter + 'u' + suffix)
        continue
    print(letter + suffix)

print()
print(fruit[:]) # [n:m] n primeiro caracter e m o último que queremos, mas não incluído; se não houver n, então conta a partir do início

def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    
    return -1

print(find('maoço', 'a', 0))
print()

def count(string, letter):
    contador = 0
    
    for i in string:
        if i == letter:
            contador += 1
    
    print(contador)

def count_3(string, letter):
    print(find(string, letter, 0))

count('javascript', 'a')
print()
count_3('javascript', 'a')
 
print()

fruta = 'banana'
print(fruta.count('a'))

def is_palindrome(string):
    if string[::-1] == string:
        print('é um palíndromo')
    else:
        print(f'a palavra {string} não é um palíndromo')

is_palindrome('ovo')
is_palindrome('socorram marrocos')


def transform_word(string):
    # ord e char para converter em caracteres e numeros
    # cada letra ord(l)
    new = []
    for l in string:
        letter = ord(l)
        new.append(letter)
    
    print(new)

 
    for item in new:
        translate = chr(item)
    

transform_word('geice codificado')

