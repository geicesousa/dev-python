from array import array
# arrays em python são módulos separados, elas servem para listas muito grandes pois melhoram a performace

letras = ['a', 'b', 'c']
numeros_inteiros = [2, 6, 9, 7]
numeros_float = [1.3, 2.9, 3.5, 9.4]

# para criar uma array temos que informar o tipo de valor que ela terá, esses type code são especificos, como uma palavra reservada

letras_arr = array('u',letras)
nome_arr = array('u',['g', 'e', 'i', 'c', 'e'])

numeros_float_arr = array('f',[1.3, 2.9, 3.5, 9.4])

numeros_inteiros_arr = array('i',[2, 6, 9, 7])

print(f'''
{letras_arr} 
{nome_arr} 
{type(letras_arr)} 
{type(numeros_float)} 
{type(numeros_float_arr)} 
{numeros_inteiros_arr} 
{numeros_inteiros} 
''')