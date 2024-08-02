# CRUD = create, read, update, delete
# métodos de lista: append, insert, pop, del, clear, extend, split, strip

lista = [1, 9, 'geice', 'curso udemy', 1.50, 'akin', True, 'vazio']
teste = [63, 'números', 1.87, 'bloco']
outra = lista.copy()
print(lista)
lista.append('cristóvão')
print(lista)
lista.pop() #remove ultimo item
print(lista)
del lista[-1] #remove ultimo item
print(lista)
lista.insert(1, 1.1) #insere um item no index
print(lista)
lista.extend(teste);lista.extend('teste') #insere cada item da str separadamente
print(lista)
lista.clear() #limpa toda a lista
print(lista);print(outra);print()

cont = 0
for item in outra:
    print(f'index: {cont}, item: {item}')
    cont += 1

#DESEMPACOTAMENTO
numero, palavra, *resto = teste
print(numero, palavra);print(resto)

teste = [63, 'números', 1.87, 'bloco']
_, _, altura, *resto = teste # usar _ (antes) ou *_ (depois) é uma convenção em python e é uma forma de acessar apenas o valor que queremos numa lista
print(altura)

# enumerate consome todos os dados então, a lista deixa de existir, é como se limpasse, retorna uma tupla
lista_enumerada = enumerate(outra)
print();print('enumerate')
for item in enumerate(outra):
    print(item)
     
print(lista_enumerada) # aponta pro objeto