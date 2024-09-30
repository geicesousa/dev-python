class Connection:
    def __init__(self, host='localhost') -> None:
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user): #setter, atribui valor ao user
        self.user = user
    
    def set_password(self, password):
        self.password = password

    @classmethod
    def cria_user_password(cls, user, password):
        return cls(user, password)
    
    @staticmethod
    def log(msg):
        print('Log:', msg)
        

# @property é um getter em python, ele vai obter/retornar o valor de determinado atributo; é um método que se comporta com atributo
# @property é uma propriedade do objeto, não precisa ser chamada com (), geralmente tem o mesmo nome de um atributo
# atributos que começam com _ não devem ser usados fora da classe, pois são atributos que se referem a property (conveção)

class Caneta:
    def __init__(self, cor):
        self._cor = cor
        
    @property
    def cor(self):
        print('property cor')
        return self._cor
    
    @cor.setter
    def cor(self, coloracao): 
        #geralmente usado para restringir algum acesso, aí aqui teria uma lógica para restringir ou liberar ou qlqr outra ação
        self._cor = coloracao
        print('Atribuindo cor pelo setter:', self._cor)


caneta1 = Caneta('azul')
caneta2 = Caneta('preta')
caneta3 = Caneta('verde')

print(caneta1.cor)
caneta1.cor = 'vermelha'
print(caneta2.cor)
print(caneta3.cor)
        