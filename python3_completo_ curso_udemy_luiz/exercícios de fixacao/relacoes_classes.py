# criar 3 classes e relacioná-las

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
    pass

    @property
    def motor(self):       
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor
       
    @property
    def fabricante(self):        
        return self._fabricante

    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante


class Motor:
    def __init__(self, nome):
        self.nome = nome

    

class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self._lista_de_carros = []
         
    def inserir_carro(self, carro):
        self._lista_de_carros.append(Carro(carro))
        
    def listar_carros(self):
        for n in self._lista_de_carros:
            print(n.nome) # se não acessarmos o atributo, aparece apenas a referência ao objeto no terminal
 
        
   
 
carro1 = Carro('pegout')
turbo3 = Motor('turbo3')
pegout = Fabricante('PEGOUT')
carro1.motor = turbo3
carro1.fabricante = pegout
print('Carro1:', carro1.nome, '\nMotor:', carro1.motor.nome, '\nFabricante:', carro1.fabricante.nome)
print()


carro2 = Carro('argo')
fiat = Fabricante('fiat')
carro2.fabricante = fiat
carro2.motor = turbo3
print('carro 2:', carro2.nome, '\nMotor:', carro2.motor.nome, '\nFabricante:', carro2.fabricante.nome)
print()

print('Lista de carros do fabricante:')
fiat.inserir_carro('cronos')
fiat.inserir_carro('argo')
fiat.inserir_carro('uno')
fiat.inserir_carro('toro')
fiat.listar_carros()

print()
general_motors = Motor('General Motors')
print('Lista de motores:', general_motors.nome, 'e', turbo3.nome)

