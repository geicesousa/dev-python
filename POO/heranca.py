# class.mro() mostra a ordem dos args da class - metod resolutions order
# o super pode ser chamado antes ou depois
# mixin adciona um comportamento a classe, é uma class que implementa um método

# herança simples
class Veiculo:
    def __init__(self, cor, placa, chassi, tipo_combustivel, qtd_rodas):
        self.cor = cor
        self.placa = placa
        self.chassi = chassi
        self.combustivel = tipo_combustivel
        self.qtd_rodas = qtd_rodas


class Moto(Veiculo):  # dentro do parenteses fica a classe mãe/super
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, chassi, tipo_combustivel, qtd_rodas,
                 carregado):
        super().__init__(cor, placa, chassi, tipo_combustivel, qtd_rodas)
        self.carregado = carregado

    def esta_carregado(self, value):  # o self sempre tem que ser declarado
        if value == 'true':
            print('está carregado')
        if value == 'false':
            print('não está carregado')


carreta = Caminhao('azul', 'juh-9874', '7896541230', 'diesel', 6, 'true')
print(carreta)
print('chassi:', carreta.chassi)
print('combustível:', carreta.combustivel)
print('cor:', carreta.cor)
carreta.esta_carregado('true')


# herança múltipla, é um aninhamento de classes, é para usar com cuidado pois 
# deixa o código confuso

class Animal:
    def __init__(self, qtd_olhos, qtd_patas):
        self.qtd_olhos = qtd_olhos
        self.qtd_patas = qtd_patas


class Mamifero(Animal):
    def __init__(self, qtd_olhos, qtd_patas, cor):
        super().__init__(qtd_olhos, qtd_patas)
        self.cor = cor


class Ave(Animal):
    def __init__(self, voar, nadar, **kargs):  # os argumentos terão que ser
        # passados nomeados por estar usando kargs
        self.voar = voar
        self.nadar = nadar
        super().__init__(**kargs)


class Gato(Mamifero):
    pass


class Onitorrinco(Mamifero, Ave):
    pass


print(Onitorrinco.mro())  # mostra a ordem de aninhamento p/ classes c/ herança
