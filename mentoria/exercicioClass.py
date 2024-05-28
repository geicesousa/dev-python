from random import randint

class Cachorro:
    def __init__(self, doguinho):
        self.nome = doguinho
        self.idade = randint(1, 25)
        
    def __str__(self):
        return f'Nome: {self.nome} | Idade: {self.idade}'

    def get_nome(self):
        return self.nome
    
    def get_idade(self):
        return self.idade

    def set_nome(self, nome):
        self.nome = nome
        return self.nome 
    
    def set_idade(self, idade):
        self.idade = idade
        return self.idade
    
class Matilha(Cachorro):
    def __init__(self, nome, tamanho):
        super().__init__(nome) # usar composição ao invés de herança
        self.tamanho = tamanho
        self.matilha = []
    
    
    def cria_matilha(self):
        contador = 0
        while contador < self.tamanho:
            contador += 1
            # criei um dicionário pq garante pegar nome e idade separados
            # cachorro = { f'"nome": {self.nome} {contador} , "idade": {randint(1, 25)}'} assim cria um set, um set é uma chave e string
            cachorro = {"nome": f'{self.nome} {contador}'  , "idade": randint(1, 25)}
            self.matilha.append(cachorro)

            

        return self.matilha


instanciacao = Matilha('racas', 8)
instanciacao.cria_matilha()
instanciacao.get_nome()
print(instanciacao.cria_matilha())