# uma classe é um molde para criar novos objetos, que são instâncias e que possuem seus próprios atributos e métodos
# todas as classes em python herdam de builtins.objects, podemos ver usando: help(Classe)

class Pessoa:
    ano_atual = 2024 # atributo de classe
    
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def get_ano_nascimento(self): 
        return Pessoa.ano_atual - self.idade
        
        
p1 = Pessoa('Geice', 'cris', 27)

print(Pessoa.ano_atual)
print(p1.get_ano_nascimento())


# mantendo estado da classe
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando=filmando
        pass
    
    def filmar(self): # assinatura do método
        if self.filmando:
            print(f'{self.nome} já está filmando')
            return
        print(f'{self.nome} começou a filmar')
        self.filmando = True
    
    
cam1 = Camera('canon')
cam2 = Camera('sony')

cam1.filmar()
print(cam1.filmando)
cam1.filmar()
print()

print(cam2.nome)
print(cam2.filmando)
print()


# __dict__ e vars atributos de instância

print(vars(cam1))
print(vars(cam1))
print(vars(p1)) # transforma em dicionário
print(p1.idade, p1.nome)
del p1.idade
p1.__dict__['idade'] = 25 # cria novamente o atributo idade, pode tbm modificar um atributo já existente
print(p1.idade, p1.nome)

