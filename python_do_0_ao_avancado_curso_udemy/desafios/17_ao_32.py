age = 78 #int(input('Digite su age: '))

if age < 13:
    print('você é criança')
elif age >= 13 and age <= 19:
    print('você é adolescente')
else:
    print('você é adulto')


cars = ['fordka', 'palio', 'rylux', 'picasso', 'fusca', 'virtus', 'fiat uno']

car =  'PALIO' # input('digite o nome do carro desejado: ').lower()

if car in cars:
    print('temos este carro disponível')
else: 
    print('não temos este carro na loja')


fruta_correta = False

while fruta_correta == False: # True
    fruta = 'abacate' # input('digite o nome de uma fruta: ').lower()

    if fruta == 'abacate':
        print('você acertou a fruta correta!')
        fruta_correta = True
       # break
    else:
        print('tente novamente...')
        continue

# numeros = [1,2,3,4,5,6,7,8,9,10]
numeros = list(range(1,11))
pares = []
impares = []

for i in numeros:
    if i % 2 == 0:
        pares.append(i)
    
    else:
        impares.append(i)

print(f'pares: {pares} | ímpares: {impares}')

cidades = ('Recife', 'Salvador', 'Maceió')
cidade = 'salvador' # input('digite o nome de uma cidade: ').lower()

if cidade in cidade:
    print(f'a cidade de {cidade} é um destino possível')
else:
    print(f'a cidade de {cidade} não é um destino possível')

paises = {'frança': 'paris', 'portugal': 'lisboa', 'holanda': 'amsterdã', 'espanha': 'madri', 'brasil': 'brasília', 'grécia': 'atenas'}

pais = input('digite o país: ').lower()

if pais in paises:
    print(f'Pais: {pais}, Capital: {paises[pais]}')

else:
    print(' capital não encontrada')