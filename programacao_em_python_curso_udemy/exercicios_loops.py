# loop while [break e continue] e loop for
# invoice (fatura) nome de user, product and price, só para qndo o usuario digita 'n' 

repeat = 's'
invoice = []
total = 0

while repeat == 's':
    product = input('Nome do produto: ')
    price = float(input('Preço do produto: '))
    invoice.append([product, price])
    total += price

    repeat = input('deseja continuar?').lower()

for i in invoice:
    print(f'{i[0]} - R${i[1]}')

print(f'O valor total da compra é {total}')


