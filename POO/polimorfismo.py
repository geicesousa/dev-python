# a função len() é um exemplo de polimorfismo, se adequa a cada tipo que recebe
# polimorfismo geralmente é trabalhado junto com herança em poo
class Ave:
    def __init__(self, cor_penas, cor_bico):
        self.cor_penas = cor_penas
        self.cor_bico = cor_bico

    def voar(self):
        return print('Voando')


class Arara(Ave):
    def voar(self):
        super().voar()


class Avestruz(Ave):
    def voar(self):
        return print('Apesar de ser uma ave, avestruzes não voam.')


avestruz = Avestruz('preta e branca', 'laranja')
avestruz.voar()
arara = Arara('azul', 'laranja')
arara.voar()
