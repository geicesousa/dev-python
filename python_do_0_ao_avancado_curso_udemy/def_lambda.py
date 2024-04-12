# lambda é uma função sem nome
# para usar devemos chamar a palavra reservada, um argumento e uma expressão, geralmente atribuimos a uma variálvel e usamos dentro de outra função

soma = lambda x, y: x + y
print(soma(1,3))

def somando_e_multiplicando(x,y):
    adc = lambda x, y: x + y
    return adc(x,y) * 2

print(somando_e_multiplicando(3,6))