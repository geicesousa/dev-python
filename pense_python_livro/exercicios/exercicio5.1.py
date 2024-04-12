import time

resultado = time.time()
print(resultado)

minutos = resultado / 60
print(minutos)

horas = minutos / 60
print(horas/60)

def check_fermat(a, b, c, n):
    if n >= 2:
        verify = a**n + b**n
        if verify == c**n:
            print('fermat estava certo')
        else:
            print(f'''Fermat estava errado, {verify} e {c** n}
                  Holy smokes, Fermat was wrong!
            ''')
    else:
        print('''n é menor que 2 
No, that doesn’t work.
''')

#check_fermat(6,2,4,1)

def check_fermat2(a, b, c, n):
    if n >= 2 and a**n + b**n == c**n:
        print(f'''Holy smokes, Fermat was wrong!''')
    else:
        print('''No, that doesn’t work.''')

#check_fermat2(6,2,4,1)

def testa_check_fermat():
    valor_a = input('Digite o valor de a: ')
    valor_b = input('Digite o valor de b: ')
    valor_c = input('Digite o valor de c: ')
    valor_n = input('Digite o valor de n: ')

    a = int(valor_a)
    b = int(valor_b)
    c = int(valor_c)
    n = int(valor_n)

    check_fermat2(a, b, c, n)

# testa_check_fermat()

#Se algum dos três comprimentos for maior que a soma dos outros dois, então você não pode formar um triângulo. Senão, você pode. (Se a soma de dois comprimentos igualar o terceiro, eles formam um triângulo chamado “degenerado”.)
def is_triangle(x, y, z):
    xy = x + y
    yz = y + z
    xz = x + z
    if z > xy or x > yz or y > xz:
        print('No')
    else:
        print('Yes')

is_triangle(8,2,6)
is_triangle(12,1,1)
is_triangle(3,4,5)
is_triangle(1,1,10)

def testa_is_triangle():
    valor_a = input('Digite o valor de a: ')
    valor_b = input('Digite o valor de b: ')
    valor_c = input('Digite o valor de c: ')

    a = int(valor_a)
    b = int(valor_b)
    c = int(valor_c)
  
    is_triangle(a,b,c)

#testa_is_triangle()   


def recurse(n, s):
    ''' função recebe n e s como parametros
    n e s: deve ser um nº
    sempre que n for um valor negativo entra em loop infinito
    '''
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s),

