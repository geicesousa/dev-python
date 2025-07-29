# Filas funcionam enqueue (insere um item no final da lista) dequeue (retira um item no início da lista). A estrutura de dados de uma fila é FIFO (first in, first out - primeiro a entrar, primeiro a sair) 
# Pilha é uma estrutura de dados LIFO (last in, first out - último a entrar, primeiro a sair)
# 

from collections import deque # fila com duas extremidades ou dois finais (double-ended); basicamente significa que podemos adicionar elementos no início e final da fila usando insert, pop, appendleft, popleft

grafo = {}
grafo['voce'] = ['alice','bob','claire']
grafo['bob'] = ['anuj','peggy']
grafo['alice'] = ['peggy']
grafo['claire'] = ['thom','jonny']
grafo['anuj'] = []
grafo['peggy'] = ['silas', 'beth']
grafo['thom'] = []
grafo['jonny'] = []

def vende_manga(nome):
    return nome == 'silas'

def pesquisa(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    verificadas = []
    
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        
        if not pessoa in verificadas:
            if vende_manga(pessoa):
                print(f'{pessoa} é um vendedor de mangas!')
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa)
                
    print(f'Não encontramos vendedor de manga')     
    return False


pesquisa('voce')
pesquisa('thom')
pesquisa('anuj')
pesquisa('bob')
print()