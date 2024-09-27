#contando de 2 em 2

for number in range(0, 15, 2):
    print(number)

for number in range( 10 ):
    print(number)

print()
print('floats, round e decimal')   
# floats, round e decimal
import decimal
numero_1 = 0.1
numero_3 = decimal.Decimal('0.1')
numero_2 = 0.7
soma = numero_1 + numero_2

print(soma)
print(f'{soma:.2f}')
print(type(f'{soma:.2f}')) # str
print(round(soma, 2)) # se não passamos o segundo parametro p/ casas decimais fical como float, o zero não aparece
print(round(soma)) # arredonda e é um int
print(type(round(soma, 2))) #float
print(type(numero_3)) #float