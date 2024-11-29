pilha_caixas = 10
caixas_abertas = []

def encontra_chave(caixas):
    while 0 < caixas:
        abriu_caixa = caixas
        caixas_abertas.append(abriu_caixa)
        caixas -= 1
    
def recursiva(i):
    print(i)
    if i > 0:
        recursiva(i-1) # caso recursivo
    else:
        print('i = 0') # caso base

recursiva(3)

def fat(n):
    if n == 1:
        return 1
    else:
        return n * fat(n-1)
        
print(fat(5),)