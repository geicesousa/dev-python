# variável livre é a variável que está entre a função mãe e a filha numa função decoradora, ela está fora do escopo da clousure

def exemplo(a):
    x = a # variável livre
    
    def retorna_parametro(valor=''):
        nonlocal x
        x += valor # sem o nonlocal lança o erro UnboundLocalError pq o python não encontra x neste escopo; o nonlocal informa ao python que a variável é para ser buscada em outro escopo
        return x
    
    return retorna_parametro
    
teste = exemplo('geice')
teste2 = exemplo('geice')
print(teste())
print(teste2(' e akin'))