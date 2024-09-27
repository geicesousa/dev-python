# syntax sugar
# no instante que decoramos uma função o python já inicia a execução dela 
# @decoradora 
# def decorada(): 
#   pass
# pode haver mais de um decorador e eles são lidos de baixo para cima, a mais próxima da def é a primeira

def decorador(func):
    def interna(*args, **kwargs):
        return func(*args, **kwargs)
    return interna

@decorador
def soma(x, y):
    return x + y

somar = soma(5,5)
print(somar)
