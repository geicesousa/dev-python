def soma(x,y):
    return x + y

def multiplica(x,y):
    return x * y

def executa(funcao, *args):
    def pausa_def(x):
        return funcao(x,*args)
    
    return pausa_def

soma_5 = executa(soma, 5)
print(soma_5(5))

multiplica_15 = executa(multiplica, 15)
print(multiplica_15(4))