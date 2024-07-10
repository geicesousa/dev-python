# INNER FUNCCTIONS: colocar uma função dentro da outra, cascata de funções

def function_dad(parametro):
    print('função pai')
    print(parametro)
    # também é possível passar uma função como paramentro e executar aqui:  parametro() 
    def function_soon(parametro):
        print('chamada interna da função filha')
        print(parametro)
        # função escopada, só existe no escopo da dad

    function_soon('o que vem?')

function_dad('executando função pai')

print()

def calculo(operacao):
    def soma(a,b):
        return a + b
    def subtrai(a,b):
        return a - b
    
    # if operacao == '+':
    #     return soma
    # else:
    #     return subtrai
    
    # mach case é uma estrutura condicional para python
    match operacao:
        case '+':
            return soma
        case '-':
            return subtrai

conta = calculo('+')
print(conta) # aqui mostra o objeto

# aqui mostra os resultados
print(calculo('+')(60,8))
print(conta(8,5))
print()

''' nesses casos, quando uma função é retornada, 
ela só é executada dependendo do parâmetro que foi 
passado como argumento na função pai, é uma fábrica 
de funções (factory)

uma função que não tem retorno atribuído retorna None
só conseguimos usar return dentro de uma função
'''

# DECORADOR é uma função
# um decorador adiciona uma nova funcionalidade sem modificar a estrutura da função decorada
# atribuimos a uma variável e passamos a função que queremos decorar como argumento assim:
# funcao_decorada = funcao(funcao_que_quero_decorar), 
# é útil para fazer checagens, de saldo, se aquele usuário pode acessar aquele dado da conta, realizar alguma outra tarefa após a verificação
# @nome_da_função_decoradora => açúcar sintático: um facilitador da sintaxe, deixa o uso menos verboso
def imprime_mensagem(funcao):
    def guarda_mensagem():
        print('abaixo uma função será executada')
        funcao()
        print('a função foi executada')

    return guarda_mensagem
    

def ola_mundo():
    print('Olá mundo!')

decorada = imprime_mensagem(ola_mundo)
decorada()

print()
print('**exemplo usando açúcar sintático**')

@imprime_mensagem
def ola_mundo():
    print('Olá mundo!')

ola_mundo()
print()

# decorador usando funções com parâmetros
print('decorador usando argumentos')
print()

def imprime_mensagem_com_parametro(funcao):
    def guarda_mensagem(*args, **kwargs): 
        # usando args e kwargs fica mais genérico e podemos usar quantos parâmetros quisermos
        print('abaixo uma função recebida por paramentro será executada')
        return funcao(*args, **kwargs) 
        # o ideal é retornar a função recebida por parâmetro, não só executar, pois o resultado fica guardado na memória

    return guarda_mensagem

@imprime_mensagem_com_parametro
def hello_world(parametro, o):
    print(f'Olá mundo de {parametro}')

hello_world('Geice', 'Sousa') # o segundo parâmetro não vai aparacer pq na finção original ele não está sendo usado
print('introspecão comprometida', hello_world.__name__)
print()

''' INTROSPECÇÃO: é a capacidade de um objeto saber os seus atributos em tempo de execução, 
quando usamos decoradores essa capaciadade fica comprometida e para resolver isso usamos o
módulo functools, método wraps() e passamos como argumento a função que será executada no
decorador
'''



import functools

def imprime_mensagem_com_parametro(funcao):
    @functools.wraps(funcao)
    def guarda_mensagem(*args, **kwargs): 
        return funcao(*args, **kwargs) 
    return guarda_mensagem

@imprime_mensagem_com_parametro
def hello_world(parametro, o):
    print(f'Olá mundo de {parametro}')
print('instrospecção salvaguardada', hello_world.__name__)

