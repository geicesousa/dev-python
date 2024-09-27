# uma forma de criar listas a partir de iteráveis, pode haver condicional (com if/else) a esquerda do for; 
# a direita do for vai funcionar como um mapeamento
nova_lista = [numero for numero in range(5,55,5)]
print(nova_lista)
lista = [numero + 5 for numero in range(0,10)]
print(lista)

for_duplo = [(x,y) for x in range(4) for y in range(5)]
print(for_duplo)

print()

dici = {"geice": "nome", "sousa": "sobrenome", "27": "idade"}

new_dici = { chave: valor for chave, valor in dici.items()}
print(new_dici)
print()
new_dici = { chave: valor if valor == "nome" else "não é nome" for chave, valor in dici.items() }
print(new_dici)
print()
new_dici = { chave: valor if valor == "nome" else "não é nome" for chave, valor in dici.items() if chave == "27"}
print(new_dici)