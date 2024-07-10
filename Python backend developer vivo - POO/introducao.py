# classe sempre começa com letra maiúsculas e o self tem que ser chamado em cada comportamento, que são os métodos que a classe tem
# em python temos construtores e destrutores


class Bicicleta:
    def __init__(self, color, type, name, value):
        self.color = color
        self.type = type
        self.name = name
        self.value = value

    def horn(self):
        return "bibifonfon"
    
    def run(self):
        return "running"
  
    def stop(self):
        return "stopp"
 
    def __str__(self):
        return f'''
        Nome: {self.name}
        Cor: {self.color}
        Modelo: {self.type}
        Valor: R${self.value}
        '''


new_bici = Bicicleta('Caloi', 'preta', 'Vicenzo', '1.300,00')
print(new_bici)
