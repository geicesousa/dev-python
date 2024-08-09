# argumentos nomeados, posicionais
# parâmetros com valores padrões 
# após chamar um argumento nomeado, os próximos obirgatoriamente devem ser nomeados tbm
# em python return só é possível dentro de uma função ou método de classe

# se usarmos global x dentro de uma função; é possível, mas não é uma boa prática
x = 1
def escopo():
    global x
    x = 10
    print(x, 'função escopo')

escopo()
print(x)

# *args, para argumentos não nomeados, empacota os valores numa tupla
def soma(*args):
    total = 0
    for n in args:
        total += n
    return total
    
numeros = 1,2,3,4,5,6
print('Soma = ', soma(1,2,3))
print('Soma desempacotando = ', soma(*numeros))

print('####Exercícios####')
#função multiplicadora
def multiplicadora(*args):
    multiplicacao = 1
    for n in args:
        multiplicacao *= n
    
    return multiplicacao

resultado = multiplicadora(*numeros)
print(resultado)

def par_impar(numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'ímpar'

par = par_impar(6)
impar = par_impar(9)

print(par, impar)

# Higher Order Functions -> funções que podem receber e/ou retornar outras funções
# First-Class Functions -> Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

def saudacao(msg):
    return f'{msg}'

def saudacao_nome(funcao, nome):
    return funcao(nome)

cumprimento = saudacao
cumprimento('Olá')

print(saudacao_nome(saudacao, 'Geice'))

# closure
def multiplicacao(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar



duplicar = multiplicacao(2)
triplicar = multiplicacao(3)
quaduplicar = multiplicacao(4)

print(duplicar(6))
print(triplicar(9))
print(quaduplicar(3))