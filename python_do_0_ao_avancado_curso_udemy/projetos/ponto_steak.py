# usar if else 
# retornar o ponto de cozimento de acordo com a temperatura que usuário vai fornecer
# < 48 assar mais um pouco 48c - selada
# 54 mal passada
# 60 ao ponto
# 65 entre ao ponto e bem passada
# 71 bem passada > 71 bem passada

temperatura = int(input('Qual a temperatura da carne? '))

if temperatura < 48:
    print('A carne precisa assar mais um pouco.')

elif temperatura >= 48 and temperatura < 54:
    print('Selada.') 

elif temperatura >= 54 and temperatura < 60:
    print('Mal passada.') 

elif temperatura >= 60 and temperatura < 65:
    print('Ao ponto.')

elif temperatura >= 65 and temperatura < 71:
    print('Entre ao ponto e bem passada.')

else:
    print('Bem passada.')


#---- resolução do curso ----#

if temperatura < 48:
    print('A carne precisa assar mais um pouco.')

elif temperatura in range(48, 54):
    print('Selada.') 

elif temperatura in range(54, 60):
    print('Mal passada.') 

elif temperatura in range(60, 65):
    print('Ao ponto.')

elif temperatura in range(65, 71):
    print('Entre ao ponto e bem passada.')

else:
    print('Bem passada.')

