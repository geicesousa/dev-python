# force o erro e ver ele no console para tratá-lo adequadamente 
zero = 0 
trinta = 30
letras = ['a', 'b', 'c']

try:
    pass 
    letras[9] # IndexError: list index out of range
    letras + trinta # TypeError: can only concatenate list (not "int") to list
    30/0 # ZeroDivisionError: division by zero
    numero = int(input('')) # ValueError: invalid literal for int() with base 10: 'l'
    letras.find('z') # AttributeError: 'list' object has no attribute 'find'
    #c # NameError
    #while True print('Hello world') # SyntaxError: invalid syntax

except IndexError as error:
    print('IndexError: list index out of range')
    print(error.__class__.__name__)
    print(error.__class__.__cause__)
    print(error)

except TypeError:
    print('TypeError: can only concatenate list (not "int") to list')

except ZeroDivisionError:
    print('ZeroDivisionError: division by zero')

except ValueError:
    print('ValueError: invalid literal for int() with base 10: "l"')

except AttributeError as error:
    print('AttributeError: "list" object has no attribute "find"')

except NameError:
    print('NameError')

except SyntaxError:
    print('SyntaxError: invalid syntax')
    
# o finally sempre será executado
finally:
    print('acabou')

# é possível lançar erros 'personalizados' usando raise <NomeDoErro>(mensagem)
# o raise tbm relança a exceção

