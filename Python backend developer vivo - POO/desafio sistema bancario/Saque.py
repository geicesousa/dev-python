from Transacao import Transacao

class Saque(Transacao):

    def __init__(self, valor):
        self._valor = valor
        #self.conta = conta
    
    @property
    def valor(self):
        return self.valor

    def registrar(self, conta):
        conta.sacar(self.valor)

        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)
