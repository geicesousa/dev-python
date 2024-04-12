def nome_completo():
    print('Meu nome completo é Geice Sousa Pinho.')
    minha_idade()

def minha_idade():
    print('Minha idade é 31 anos.')

nome_completo()

# As funções nulas podem exibir algo na tela ou ter algum outro efeito, mas não têm um valor de retorno. , são funções que apenas executam uma ação, void 
# funções com retorno retornam um valor armazenado

def rigth_justify(s):
    print ('1 ' * (70 - len(s)) + s)

rigth_justify('geice')
rigth_justify('geice pinho')
rigth_justify('geice sousa pinho')


print(len('1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 '))
print(len('1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 '))

#__main__, que é um nome especial para o frame na posição mais proeminente. Quando você cria uma variável fora de qualquer função, ela pertence a __main__.