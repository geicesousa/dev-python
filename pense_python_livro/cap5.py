# x % 10 produz o dígito mais à direita de x (na base 10). Da mesma forma x % 100 produz os dois últimos dígitos.
print(120%10)
print(120%100)
print(1200%10)
print(1110%100)
print(1290%10)
print(1290%100)

# // divisão exata, arreonda o resultado para o valor menor 
print( 5//3)
# pass palavra reservada funciona como "deixe passar", não faz nada

# forma simpliciface de usar condicional dupla em python
x = 0
if x < 20 and x < 50:
    print()
    #condição

if 20 < x < 50:
    print()
    #condição 

# return só pode ser usado dentro de uma função
# função recursiva ou recursividade: uma função que chama a si mesma

def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

countdown(10)

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

print_n('Hello', 4)

def do_n(func, n):
    for i in range(n):
        print(n)
        do_n(func, n-1)

do_n(do_n, 2)
do_n(do_n, 3)

