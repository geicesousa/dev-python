class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, nova_conta):
        self.contas += nova_conta
        self.contas.append(nova_conta)
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)