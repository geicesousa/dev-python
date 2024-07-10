# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

# TODO: Crie um método fazer_chamada para permitir que um usuário faça uma chamada telefônica:
# TODO: Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano':
# TODO: Verifique se o saldo do plano é suficiente para a chamada.
# TODO: Se o saldo for suficiente, deduz o custo da chamada do saldo do plano.
# TODO: E retorne uma mensagem de sucesso com o destinatário e o saldo restante após a chamada:
    def fazer_chamada(self, destinatario, duracao):
      custo_chamada = self.plano.custo_chamada(duracao)
      if saldo_plano > custo_chamada:
        novo_saldo = custo_chamada - saldo_plano
        return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${novo_saldo}"

# Classe Pano, ela representa o plano de um usuário de telefone:
class Plano:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

# TODO: Crie um método para verificar_saldo e retorne o saldo atual:
    def verificar_saldo(self):
      return self.saldo
# TODO: Crie um método custo_chamada para calcular o custo de uma chamada supondo o custo de $0.10 por minuto:
    def custo_chamada(self, minutos):
      tempo = number(minutos)
      custo = 0.10 * tempo
      return custo

# TODO: Crie um método deduzir_saldo para deduz o valor do saldo do plano:
    def deduzir_saldo(self, valor):
      deducao = self.saldo - valor
      return deducao
# Classe UsuarioPrePago, aqui vemos a herança onde UsuarioPrePago herda os atributos e métodos da classe UsuarioTelefone:
class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


# Recebendo as informações do usuário:
nome = "rod"
numero = 90000000000
saldo_inicial = 10.00

# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = 33933333333
duracao = 60

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))