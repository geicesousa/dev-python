from Cliente import Cliente
from Historico import Historico

class Conta:
    def __init__(self, numbero, cliente):
        self._saldo = 0
        self._numbero = numbero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    @property
    def numero(self):
        return self._numbero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def saldo(self):
        return f'Seu saldo é {self._saldo}'
    
    @property
    def historico(self):
        return self._historico
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)

    def sacar(self, valor):
        if self.saldo >= valor and valor > 0:
            self.saldo -= valor
            print(f'Saque realizado com sucesso. Seu saldo atual é R${self.saldo}')
            return True
        elif valor < 0:
            print('O valor sacado precisa sem mais de R$0,00')
        else:
            print(f'Saldo insuficiente para saque. Seu saldo atual é {self.saldo}')
    
        
    def depositar(self, valor):
         if valor > 0:
            self.saldo += valor
            print(f'Deposito no valor de R${valor} realizado com sucesso.')