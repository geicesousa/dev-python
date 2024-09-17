import json
from typing import TypedDict

pessoa = {
    'nome': 'Geice',
    'idade': 37,
    'profissão': 'software engenieer',
    'contatos': [ 
        {'telefone': '(71)987568416'}, 
        { 'celular': '(71)987458769'}
    ] 
}

with open('dados.json', 'w') as arquivo:
    json.dump(pessoa, arquivo, indent=2)
    print(arquivo)
    
with open('dados2.json', 'w') as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=2)
    
    print(arquivo)
    
with open('dados2.json', 'r') as arquivo:
    exibe = json.load(arquivo)
    print(exibe)
    print(type(exibe))


class Pessoa(TypedDict): #tipagem
    nome: str
    idade: int 
    altura: float
    profissao: str
    contatos: list
    bilingue: True
    proprietaria: None | str