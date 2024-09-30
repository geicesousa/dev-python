# python não tem modificadores de acesso, mas por convenção para informar o acesso dos atributos usamos:
# public = (sem underline) 
# _protect = (com um underline), usado apenas dentro da classe e das subclasses/classes-filhas
# __private = (com dois underlines), usado apenas dentro da classe-mãe
# como não há modificadores de acesso reais, que realmente impedem/barram o acesso, conseguimos chamar no código de qualquer jeito; 

class Exemplo:
    def __init__(self):
        self.public = 'atributo publico'
        self._protect = 'atributo protegido'
        self.__privado = 'atributo privado'
        
    def metodo_public(self):
        print('método público')
        return self.public
    
    def _metodo_protect(self):
        print('método protegido')
        return self._protect

    def __metodo_private(self):
        print('método privado')
        return self.__privado

exemplo = Exemplo()
print(exemplo.public)
print(exemplo.metodo_public())
print()
print(exemplo._protect)
print(exemplo._metodo_protect())
print()
# print(exemplo.__private) # dá erro AttributeError: 'Exemplo' object has no attribute '__private'
# print(exemplo.__metodo_private()) 
print(exemplo._Exemplo__metodo_private()) # apenas assim conseguimos acessar