# atributo de classe é um atributo ou variável que será utilizada dentro da class, aqui modificações só podem ser realizadas dentro da class ou por meio dela
# atributo de instância é alocado durante a instanciação e só vale para o objeto instanciado

class Aluno:
    turno = 'matutino'  # atributo de classe

    def __init__(self, nome, escola):
        self.nome = nome  # atributos de instância, pois só serão alocados durante a instanciação da class
        self.escola = escola

    def __str__(self) -> str:
        return f'Nomes: {self.nome} | Escola: {self.escola} | Turno: {self.turno}'
    

cristiano = Aluno('Cristiano', 'Pingo de Gente')
akin = Aluno('Akin', 'CMEI')
print(cristiano)
print(akin)

Aluno.turno = 'integral'
print(akin)
print(cristiano)

cristiano.turno = 'vespertino'
print(akin)
print(cristiano)


# método de classe, gera uma nova instanciação; precisa de acesso ao contexto da classe
# método de estático, usado dentro da classe, não precisa de contexto nem de classe nem de instanciação

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self) -> str:
        return f'Nome: {self.nome} | Idade {self.idade}'
        
    def gera_ano_de_nascimento(self, idade):
        ano = 2024 - idade
        return f'{self.nome} nasceu em {ano}'
   
    @classmethod
    def criar_data_nascimento(cls, ano, mes, dia, nome):  # cls aponta para class Pessoa, é como uma instanciação, é uma referência
        idade = 2024 - ano 
        return cls(nome, idade)
    
    @staticmethod
    def maior_de_idade(idade):
        return idade >= 18


pessoa1 = Pessoa('Geice', 31)
pessoa1.gera_ano_de_nascimento(31)
print(pessoa1.nome)
print(pessoa1.idade)
print(pessoa1.gera_ano_de_nascimento(31))
print(pessoa1)
print(pessoa1.criar_data_nascimento(1992, 12, 8, 'Geice'))
print(pessoa1.maior_de_idade(31))

