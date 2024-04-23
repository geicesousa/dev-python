from Conta import Conta
from abc import ABC, abstractmethod

class Transacao(ABC):

    @property
    @abstractmethod
    def value(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        if isinstance(conta, Conta):
           print('é instância')
        
        else:   
           print('conta inválida, não é instância')
