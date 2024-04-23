# é sobre um atributo ou método ser público ou provado
# python não tem uma protecção de dados real, mas por convenção usamos o _
# (underline) para dizer que o método é privado
#  
#  

class Conta:
    def __init__(self, saldo, agencia, tipo):
        self._saldo = saldo
        self.agencia = agencia
        self.tipo_de_conta = tipo

    def sacar(self, valor):
        self._saldo -= valor
        return 'saque realizado'

    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        self._saldo += valor
        return 'deposito concluído'

    def tranferencia(self, valor, conta_destinataria):
        self._saldo -= valor
        conta_destinataria._saldo += valor
        return 'transferência realizada com sucesso'


# @property (getter) é como um estático que só pode ser acessado na class,
# não é privado de vdd, tudo é público
# @x.setter (setter)
# @x.deleter
# @property, @classmetod, @staticmetod == depurador
