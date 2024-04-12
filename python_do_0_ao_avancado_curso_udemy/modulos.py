# criamos as funções em arquivos separados e importamos, para fins de organização e separação de responsabilidades do programa
import funcoes

# usando import importa todas as funções, usando o from
# from funcoes import multiplicar
# from funcoes import * (importa tudo)
from funcoes import multiplicar, somando_e_multiplicando

print(funcoes.multiplicar(2))

print(funcoes.somando_e_multiplicando(8,6))
