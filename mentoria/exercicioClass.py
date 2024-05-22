from random import randint

class Cachorro:
    def __init__(self, doguinho):
        self.nome = doguinho
        self.idade = randint(1, 25)
        
    def __str__(self):
        return f'Nome: {self.nome} | Idade: {self.idade}'

    def nome_cachorro(self):
        return self.nome
    
    def idade_cachorro(self):
        return self.idade

    def setter_nome(self, novo):
        self.nome = novo
        return self.nome 
    
    def setter_idade(self, nova):
        self.idade = nova
        return self.idade
    

class Matilha(Cachorro):
    def __init__(self, nome, tamanho):
        super().__init__(nome)
        self.tamanho = tamanho
        self.matilha = []
    
    
    def cria_matilha(self):
        contador = 0
        while contador < self.tamanho:
            contador += 1
            # criei um dicionário pq garante pegar nome e idade separados
            cachorro_idade = { "nome": self.nome, "idade": randint(1, 25)}
            self.matilha.append(cachorro_idade)

            # passando um array como parametro de matilha 
            # for nome in self.nome:           
            #     cachorro_idade = { "nome": nome, "idade": randint(1, 25)}
            #     matilha.append(cachorro_idade)

        
        return self.matilha

   
racas = ['pitbull', 'cão', 'viralata', 'caramelo']
instanciacao = Matilha('racas', 8)
instanciacao.cria_matilha()
instanciacao.nome_cachorro()
print(instanciacao.cria_matilha())