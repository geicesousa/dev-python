# o objeto é o outro

class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        
    def classe_usada(self):
        print(f'Nome: {self.nome}, Sobrenome: {self.sobrenome}, Idade: {self.idade}, Classe: {self.__class__.__name__}')

class Cliente(Pessoa):
    pass

class Estudante(Pessoa):
    pass

# mro - method resolution order, ordem de busca dos métodos nas classes herdeiras, é como uma verificação do escopo da classe; conseguimos ver usando o help(Classe) ou classe.mro()
pessoa1 = Pessoa('Geice', 'Sousa', 27)
pessoa1.classe_usada()
estudante1 = Estudante('Akin', 'Sousa', 3)
estudante1.classe_usada()
cliente1 = Cliente('Amanda', 'Reis', 37)
cliente1.classe_usada()

# herança multipla e mixins
# geralmente quando usamos herança é pq os objetos estão relacionados, generalizando ou especializando, mas sempre dentro de uma mesma família, são objetos analógos.  (animal, ave, cardeal -  mamífero, pessoa, aluno)
# ao usar mixins alguns princípios do solid podem ser quebrados
# mixins é uma herança, mas que não pertence a mesma família (Cliente (Pessoa, SalvaArquivo))
# problema do diamante: uma serie de heranças que acabam se confundindo na hora de buscar o escopo dos métodos
# A, B, C D
# D(B,C) - C(A) - B(A) - A
#      A
#   /    \
#  B     C
#  \     /
#     D
# o python3 tem o c3 superclass linearization para gerar o mro
# podemos usar o Classe.mro() ou como atributo __mro__
#
