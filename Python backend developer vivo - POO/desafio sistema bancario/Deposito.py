from Transacao import Transacao

class Deposito(Transacao):

    def __init__(self, valor):
        self._valor = valor
  
    
    @property
    def valor(self):
        return self.valor

    def registrar(self, conta):
        conta.depositar(self.valor)

        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)