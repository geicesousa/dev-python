# os Dados são os Atributos e o comportamento são os Métodos
# Classes agrupam dados e funções de um conjunto mais geral (carros, funcionários, bolos, casas)
# Objetos são os resultados, os elementos criados a partir de uma classe, chamados instâncias (um carro específico, um funcionário, bolo de laranja, uma casa)

# para criar uma classe em python precisamos iniciar os atributos com self, esse parâmetro não é declarado pelo usuário, é intríseco da classe

class Funcionarios: 
    def __init__(self, nome_completo, idade, email, cargo):
    # __init__ é o construtor, inicia a classe, se não iniciar o valor é None
        self.nome_completo = nome_completo
        self.idade = idade
        self.email = email
        self.cargo = cargo

    def nome_e_cargo(self):
        return f' Nome: {self.nome_completo} | Cargo: {self.cargo}'


funcionaria = Funcionarios('Geice Sousa Pinho', 27, 'geice@jusbrasil.com', 'software engenieer')
funcionario = Funcionarios('Carlos Almeida', 31, 'carlos@jusbrasil.com', 'design')

print(Funcionarios.nome_e_cargo(funcionaria))
print(funcionario.nome_e_cargo())
