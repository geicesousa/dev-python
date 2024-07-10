from datetime import datetime

class Historico:
    def __init__(self):
        self._transacoes = []
        self.limite_transacoes = 10

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self.transacoes.append({
           "tipo": transacao.__class__.__name__,
           "valor": transacao.valor,
           "data": datetime.now().strftime("%d/%m/%Y %H:%M:%s")
        }) 

    # gerador
    def gerar_relatorio(self, tipo_transacao = None): 
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao['tipo'].lower() == tipo_transacao.lower():
                yield transacao
    
    # mostrar data e hora das transações
    def transacoes_diarias(self):
        pass