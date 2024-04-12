print('Olá, mundo Python!')

name = 'Geice'
age = 31

print(f'Meu nome é {name} e tenho {age} anos.')
print()     


num1 = 10
num2 = 3.5

print(num1/num2)
print()     

# name = input('Digite seu nome ')
# age = input('Digite sua idade ')

print(f'Meu nome é {name} e tenho {int(age)} anos.')
print()     

num3 = 1
num4 = 3
# num3 = int(input('nº '))
# num4 = int(input('outro nº '))

print(f'''Nº digitado: {num3}, {num4} 
soma = {num3 + num4}
subtração = {num3 - num4}
multiplicação = {num3 * num4}
divisão = {num3 / num4}
exponenciação = {num3 ** num4}

''')

frutas = ['maçã', 'banana', 'manga', 'uva', 'morango', 'abacaxi']
print(frutas)

print('1ª:', frutas[0], 'e última', frutas[-1])
print()     


frutas.remove('manga')
print(frutas)
del frutas[-1]
print(frutas)

print()

for fruta in frutas:
    print(f'Eu gosto de {fruta}.')

print()     

for n in range(1, 11):
    print(n)

print()

print('Ímpares:')
for n in range(1, 11, 2):
    print(n)

# nested for loop
vegetais = ['cenoura', 'abóbora', 'quiabo', 'vagem', 'chuchu', 'batata']

for fruta in frutas:
    for vegetal in vegetais:
        print(f'{fruta} e {vegetal}')
print()

n = 0
while n <= 10:
    print(n)
    n+=1

print('break:')
n = 0
while n <= 10:
    print(n)
    n+=1

    if n == 6:
        break

print()

print('continue:')
n = 0
while n <= 10:
    n+=1
    
    if n == 5:
        continue
    print(n)

print()
    
frutas = ['maçã', 'banana', 'manga', 'ameixa', 'maçã', 'uva', 'caju', 'morango', 'umbu', 'abacaxi', 'maçã', 'abacate']
contador = 0
for i in frutas:
    if i == 'maçã':
        contador += 1

print(f'A palavra maçã aparece {contador}x.')

print()

numero = float(input('digite um número: '))
if numero > 10:
    print('O nº é maior que 10.')

elif numero <= 10: # else
    print('O nº é menor ou igual a 10.')