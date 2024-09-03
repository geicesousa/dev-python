def soma(x,y):
    return x + y

def multiplica(x,y):
    return x * y

def executa(funcao, x):
    def pausa_def(y):
        return funcao(x,y)
    
    return pausa_def

soma_5 = executa(soma, 5)
print(soma_5)