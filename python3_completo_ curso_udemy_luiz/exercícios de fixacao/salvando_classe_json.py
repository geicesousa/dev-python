import json

class Carro:
    def __init__(self, nome, marca, rodas, portas, modelo, novo=False):
        self.nome = nome
        self.marca = marca
        self.qtd_rodas = rodas
        self.qtd_portas = portas
        self.modelo = modelo
        self.condicao = novo
     
    def __str__(self):
        print('nome:', self.nome, '\nmarca:', self.marca, '\nnº de rodas:', self.qtd_rodas, '\nnº de portas:', self.qtd_portas, '\nmodelo:', self.modelo)
        
fiat = Carro('fiat uno', 'fiat', 4, 2, 2020)
var = vars(fiat) 
with open('classe_json.json', 'w') as arquivo:
    json.dump(var, arquivo)
    
with open('classe_json.json', 'r') as arquivo:
    print(json.load(arquivo))


print()