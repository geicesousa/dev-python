class Pessoa:
    ano_atual = 2024 
    
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        
    def exibe_nome_completo(self): # métodos de classe
        return f'{self.nome} {self.sobrenome}'

# métodos de classe são diferentes de método de instância 
# método de classe são decorators, ele a cria um novo objeto, nele conseguimos acessar a própria classe; ele não possui self, o parâmetro é cls; também não conseguimos acessar o self. dentro dele
# em um @classmetod a classe referência a si mesma

    @classmethod
    def cria_anonimo(cls, idade):
        return cls('Anônima', 'Sem sobrenome', idade) # esse tipo de estrutura que usa uma função para criar um classe é uma factorie, uma fábrica
    
    @staticmethod
    def metodo_estatico(*args, **kwargs): # tem pouca utilidade, mas pode servir para organização , ele não tem acesso a cls nem ao self
        print('qualquer coisa', args, kwargs)

print('pessoa1')
pessoa1 = Pessoa('Akin', 'Sousa', 3)
nome_completo = pessoa1.exibe_nome_completo()
print(nome_completo)
print()

print('pessoa2')
pessoa2 = Pessoa.cria_anonimo(32)
print(pessoa2.nome, pessoa2.sobrenome, pessoa2.idade)
print(pessoa2.exibe_nome_completo())
print()

print('pessoa3')
pessoa3 = Pessoa.metodo_estatico(argumento_nomeado='kwargs')
print(pessoa3)
print(pessoa3)
Pessoa.metodo_estatico(1,2,3)