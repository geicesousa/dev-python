# modificações para validação de dados: não aceita valores não numéricos em price, só aceita números positivos
repeat = 's'
invoice = []
total = 0
valid_price = False

while repeat == 's':
    product = input('Nome do produto: ')

    while valid_price == False:
        price = input('Preço do produto: ')

        try: # tenta 
            price = float(price)
            if price <= 0:
                print('o preço deve ser maior que 0.')
            else:
                valid_price = True
        
        except: # caso a tentativa falhe
            print('O preço deve ser um número e os centavos devem estar separados por "."')

    invoice.append([product, price])
    total += price
    valid_price = False
    repeat = input('deseja continuar?').lower()

for i in invoice:
    print(f'{i[0]} - R${i[1]}')

print(f'O valor total da compra é {total}')
