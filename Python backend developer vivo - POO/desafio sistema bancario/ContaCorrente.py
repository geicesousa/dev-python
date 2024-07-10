from Conta import Conta
from Saque import Saque

class ContaCorrente(Conta):
    def __init__(self, number, client, limite = 500, limite_saques = 5):
        super().__init__(number, client)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor): 
        qtd_saques = len( transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__ )
        
        limite_excedido = valor > self.limite

        qtd_saques_excedida = qtd_saques >= self.limite_saques

        if limite_excedido:
            return f'O valor do saque é maior que o limite \n Limite: R${self.limite}'
        
        elif qtd_saques_excedida:
            return f'Você já fez os {self.limite_saques} saques esse mês.'
        
        else:
            super().sacar(valor)

    def __str__(self):
        return f'\n Agência: {self.agencia} \n Conta: {self.conta} \n Nome: {self.cliente.nome}'