#funções hash
#"Tabela hash é um nome sofisticado para um array cuja indexação é feita através de uma função. 
#Tabela hash é uma estrutura de dados eficiente no que diz respeito à inserção, remoção e busca de elementos.
# Não há elementos com a mesma chave em uma tabela. Chave identifica unicamente um objeto. Tipicamente é um atributo dele. Por exemplo, matrícula para aluno, CPF para pessoa, CNPJ para empresa, número do cartão de crédito para cliente etc."

# criando uma lista telefônica
def cria_lista_telefonica(nome, numero):
    dici = dict()
    
    dici['nome'] = nome
    dici['numero'] = numero
    
    # dici = {'nome': nome, 'numero': numero}
    
    return dici

print(cria_lista_telefonica('Geice', '0102030405'))
print(cria_lista_telefonica('Akin', '071717017'))

lista_telefonica = dict() # {}
print()

print()

lista_telefonica['Mateus'] = 789654123
lista_telefonica['Dandaro'] = 1234566987
lista_telefonica['Jane'] = 236541780
lista_telefonica['Tarzan'] = 98710254

print(lista_telefonica['Jane'])

print('Solução orientada a objeto')


class Lista_telefonica:
    def __init__(self):
        self.lista_contatos = []
    
    def adc_contato(self, nome, numero):
        # contato = {nome, numero} #assim cria um set
        contato = {'nome': nome, 'numero': numero} # {nome: numero}
        print(type({nome: numero}))
        for contato_nome in self.lista_contatos:
            if contato_nome['nome'] == nome:
                return f'Já existe um contato com esse nome: "{nome}"'
        else:
            self.lista_contatos.append(contato)
            return f'Contato "{nome}" adicionado com sucesso' 
    
    def get_contato(self, nome):
        for contato in self.lista_contatos:
            if contato['nome'] == nome:
                return f'Dados do Contato: {contato}'
            else:
                return 'Contato não encontrado'
    
    def exibe_lista(self):
        return self.lista_contatos

contato1 = Lista_telefonica()

contato1.adc_contato('geice', '123456')
contato1.adc_contato('paulo', '123456')
contato1.adc_contato('felipe', '123456')
contato1.adc_contato('cristina', '123456')
contato1.adc_contato('manuela', '123456')
print(contato1.adc_contato('geice', '987654'))
print(contato1.adc_contato('amanda', '123456'))

print(contato1.exibe_lista())
print(contato1.get_contato('carla'))
print(contato1.get_contato('geice'))

# funções hash que operam com strings
# a - sempre retorna 1 
def always_one(string):
    if string:
        return 1
    
# b - usa a string como indice
def string_index(string):
    index = len(string)
    return {index: string}