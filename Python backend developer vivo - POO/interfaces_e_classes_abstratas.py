# interfaces: definem o que uma classe deve fazer, mas não define como é feito, 
# interface não é uma palavra reservada em python, mas é em outras linguagens como java
# a interface define o que deve ser feito como um contrato, isso significa dizer onde os métodos serão declarados que 
# classes abstratas não podem ser instanciadas e em pyhton as usamos para criar um contrato
# um contrato obriga o uso do 
# python não tem classes abstratas por default, temos que importar um módulo (abc - abstract basic class)
# para tornar um método abstrato usamos o @abstractmetod

from abc import ABC, abstractmethod

class Controle(ABC):  # dizer que é uma extensão de ABC torna a classe abstrata, essa é a "classe interface", todas as filhas serão obrigadas a implementar todos os métodos que ela possuir

    @abstractmethod
    def ligar(self):
        print('Ligada')

    @abstractmethod
    def desligar(self):
        print('Desligada')


class ControleTV(Controle):

    def ligar(self):
        print('Ligando a televisão')
        super().ligar()

    def desligar(self):
        print('Desligando a televisão')
        super().desligar()

class Ver_error(Controle):
    pass


tv = ControleTV()
tv.ligar()
print()
tv.desligar()

print()
print('ERRO:')
print()
erro = Ver_error()