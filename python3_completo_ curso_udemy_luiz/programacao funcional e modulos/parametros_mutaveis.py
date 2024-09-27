# quando passamos como parâmetro um valor mutável, o python armazena o primeiro valor e este primeiro valor será usado em todas as chamadas daquela função
# 
def adiciona_clientes(nome, lista=[]):
    lista.append(nome)
    return lista


cliente = adiciona_clientes('Geice')
adiciona_clientes('Akin')
print(cliente)
cliente1 = adiciona_clientes('Carlos')
adiciona_clientes('Akin')
print(cliente1)
print()
# criando uma lista vazia e passando como argumento, funciona, mas o ideal é não criar função com um valor default mutável
lista1 = []
cliente_lista = adiciona_clientes('Geice', lista1)
print(cliente_lista)
print()
def adiciona_clientes2(nome, lista=None):
    if lista is None:
        lista = []
        
    lista.append(nome)
    return lista


cliente2 = adiciona_clientes2('Geice')
adiciona_clientes2('Akin', cliente2)
cliente2.append('Arthur')
# print(cliente2)

cliente3 = adiciona_clientes2('Carlos')
adiciona_clientes2('Maíra', cliente3)
adiciona_clientes2('Jane', cliente3)
# print(cliente3)