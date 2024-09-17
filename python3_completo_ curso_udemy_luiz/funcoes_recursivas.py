# são funções que se chamam dentro de si, cria um loop da função
# uma função recursiva tem sempre que ter um caso base, que seria o break, um limitador
# em puython a recursão tem um limite de 1000, por causa da limitação da call stack (lista de chamada), uma forma de burlar o limite de segurança do python é usar sys.strecursionlimit(limite), NÃO É UMA BOA PRÁTICA E NÃO É RECOMENDADO!!! 

def recursiva(inicio, fim):
    if inicio > fim:
        return fim
    
    print(inicio)
    
    inicio+=1
    
    return recursiva(inicio, fim)

recursiva(1,10)

