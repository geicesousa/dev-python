# isolar erros é uma excelente alternativa para verificar se o restante do código está funcionando bem

nomes= ['geice', 'margarida', 'amanda', 'samanta']

try:
    print(nomes[4])
except IndexError: 
    # é o erro que aparece no console quando tentamos acessar um indez inexistente, há tbm o KeyError que é para chaves inexistentes em dicts outros: ValueError NameError TypeError ImportError
    print('não existe')

print()
# quando o try funciona e queremos dar continuidade ao código podemos usar o else ou finally (mais adequado)

try:
    print(nomes[2])
except:
    print('não existe essa posição')
else:
    print('passou pelo try e não executou o except')

print()

try:
    print(nomes[1])
except:
    print('não existe essa posição')
finally:
    print('passou pelo try e não executou o except')