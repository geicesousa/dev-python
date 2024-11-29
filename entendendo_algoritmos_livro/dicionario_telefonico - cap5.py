class Lista_telefonica:
    def __init__(self):
        self.lista_contatos = {}
    
    def adc_contato(self, nome, numero):
        contato = {'nome': nome, 'numero': numero}    
        if nome in self.lista_contatos:
            return f'Já existe um contato com esse nome: "{nome}"'
        else:
            self.lista_contatos[nome] = numero
        return f'Contato "{nome}" adicionado com sucesso' 
    
    def get_contato(self, nome):
        if nome in self.lista_contatos:
            return f'Dados do Contato: {nome , self.lista_contatos[nome]}'
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

print('lista')
print(contato1.exibe_lista())

print(contato1.get_contato('carla'))
print(contato1.get_contato('geice'))