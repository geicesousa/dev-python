
'''
o for só funciona em iteráveis (str, range) 
para fazer o for o python chama um iterador __iter__ 
após chama o __next__ e faz um while
'''
# __ se chama tander
# iter(value) - função que usa o objeto
# next(iter(value)) - next entrega o próximo valor 

nome = 'geice'
texto = iter(nome)

while True:
    try:
        print(next(texto))

    except StopIteration:
        break
