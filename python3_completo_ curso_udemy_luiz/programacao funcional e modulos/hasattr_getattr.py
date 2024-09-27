# conseguimos saber quais os metódos disponíveis para determinados iteráveis usando hasattr e getattr
string = 'Geice'
string2 = 'Akin'
lista = [10,20,30]
upper = 'upper'

print(hasattr(string, 'upper'))
print(hasattr(string, 'append'))
print(hasattr(lista, 'lower'))
print(hasattr(lista, 'append'))

print()
print(getattr(string, upper)())# o parentese executa o metodo chamado/retornado pelo getattr
print(getattr(string, upper))# o objeto