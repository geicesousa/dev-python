# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
# TODO: Crie uma Estrutura Condicional para verificar o consumo médio mensal 
# TODO: Retorne o plano de internet adequado:
def recomendar_plano(consumo):
    if consumo <= 10:
        return f'Você consome até {consumo} por mês, seu plano ideal é o "Essencial Fibra - 50Mbps".'  
    elif consumo > 10 and consumo <= 20:
        return f'Você consome até {consumo} por mês, seu plano ideal é o "Prata Fibra - 100Mbps".'
    else:
        return f'Você consome até {consumo} por mês, seu plano ideal é o "Premium Fibra - 300Mbps".'

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = 19
# float(input('Qual seu consumo de dados mensal? '))
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))

#------------------##------------------##------------------##------------------##------------------#
# solução 1
print('solução 1')
# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
# TODO: Crie um loop para solicitar os itens ao usuário:
# TODO: Solicite o item e armazena na variável "item":
# TODO: Adicione o item à lista "itens":

itens = []
continuar = 0
while continuar < 3:

  item = input('Qual item deseja adicionar? ')
  itens.append(item)
  continuar += 1

# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")

#------------------##------------------##------------------##------------------##------------------#
print()
print('solução 2')
#solução 2
itens = []

adc_item = input('Digite os itens que deseja adicionar separado por vígula (,) ')

itens = adc_item.rsplit(',')

print("Lista de Equipamentos:")  
for item in itens:
    print(f"- {item}")

#------------------##------------------##------------------##------------------##------------------#
print()
print('solução 3')
#solução 3 (aceita)
itens = []

item1 = input('item: ')
item2 = input('item: ')
item3 = input('item: ')
itens.append(item1)
itens.append(item2)
itens.append(item3)

print("Lista de Equipamentos:")  
for item in itens:
    print(f"- {item}")