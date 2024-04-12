# calcular a quantidade de tinta necessária para pintar uma parede
# precisamos saber do usuário: altura da parede, largura, rendimento
# devemos usar funções

def calcula_tinta(rendimento, altura, largura):
    quantidade = altura*largura/rendimento
    return f'Você precisa de {quantidade} latas de tinta para pintar uma parede de {altura}x{largura}.'

info1 = input('Qual o rendimento da lata? ')

info2 = input('Qual a altura da parede? ')

info3 = input('Qual a largura da parede? ')

try:
    rendimento = float(info1)
    altura = float(info2)
    largura = float(info3)
    print(calcula_tinta(rendimento, altura, largura))

except:
    print('Os valores digitados devem se numéricos e separados por vígula.')
   