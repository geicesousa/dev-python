from random import randint

class Cachorro:
    def __init__(self, doguinho):
        self.nome = doguinho
        self.idade = randint(1, 25)
        
    def __str__(self):
        return f'Nome: {self.nome} | Idade: {randint(1, 25)}'

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
    
class Matilha():
    def __init__(self, nome, tamanho):
        self.nome = Cachorro(nome)
        self.tamanho = tamanho
        self.matilha = []
    
    def cria_matilha(self):
        contador = 0
        while contador < self.tamanho:
            contador += 1
            # criei um dicionário pq garante pegar nome e idade separados
            # cachorro = { f'"nome": {self.nome} {contador} , "idade": {randint(1, 25)}'} assim cria um set, um set é criado assim: {"a", "b", "a"} log={"a", "b"}; mantem apenas valores únicos
            cachorro = {"nome": f'{self.nome.get_nome()} {contador}'  , "idade": randint(1, 25)}
            self.matilha.append(cachorro)

        return self.matilha
    
    def get_matilha(self):
        return self.matilha
    
    def set_matilha(self, attr, index, value):
        self.matilha[index][attr] = value

    # armazenar no banco de dados, vulgo txt, para que o dado seja armazenado/persistido
    # open() close()

print('instanciação cachorro')
cao = Cachorro('matias')
print(cao)
print(cao.get_nome())
print(cao.get_idade())
print('matilha criada')
primeira_matilha = Matilha('BúDog', 100)
print(primeira_matilha.cria_matilha())
print(primeira_matilha.matilha[2])
print(primeira_matilha.matilha[2].get('idade'))
print(primeira_matilha.matilha[2].get('nome'))
print(primeira_matilha.get_matilha())
primeira_matilha.set_matilha('nome', 0, 'doguinho')
primeira_matilha.set_matilha('idade', 0, '19')
primeira_matilha.set_matilha('idade', 1, 32)

print(primeira_matilha.get_matilha())

