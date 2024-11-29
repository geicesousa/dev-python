# UML -> Linguagem de Modelagem Unificada, facilita a compreensão 
# associação, agregação e composição 

#associação, temos 2 objetos separados e um objeto conhece o outro, é uma relação fraca
class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None
    
    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, instrumento):
        self._ferramenta = instrumento
        
class Ferramenta:
    def __init__(self, nome_ferramenta):
        self.nome = nome_ferramenta
        
    def usar(self):
        return f'{self.nome} está em uso'
        

escritor1 = Escritor('Akin')
print(escritor1.nome)
pincel = Ferramenta('pincel')
metodo_usar = pincel.usar()
print(metodo_usar)
escritor1.ferramenta = pincel 
print(escritor1.ferramenta.usar())
print()

# agregação, são objetos separados, que existem separados, mas juntos realizam uma tarefa maior e melhor; 
# é uma relação de um para muitos
# relação rodas e carros, um é parte do outro

class CarrinhoDeCompras:
    def __init__(self):
        self._produtos = []

    def listar_produtos(self):
        for p in self._produtos:
            print(p.nome, p.preco)
            
    def total(self):
        return sum([p.preco for p in self._produtos])
    
    def inserir_produtos(self, *produtos): 
        self._produtos += produtos 
        # poderia ser um for + append ou um self._produtos.extend(produtos)



class Mercadorias:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
carrinho = CarrinhoDeCompras()
m1, m2, m3 = Mercadorias('sandália', 35), Mercadorias('vestido', 70), Mercadorias('travesseiro', 70)
carrinho.inserir_produtos(m1, m2, m3)
carrinho.listar_produtos()
print(carrinho.total())
print()


# composição, um objeto gerencia o ciclo de vida do outro,é dono do outro, no caso do exemplo, endereço só existe se cliente existir (caso não seja instaciado separadamente)
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
        pass
 
    def inserir_endereco(self, rua, numero, bairro): # quando deletarmos cliente, apagamos tbm os endereços associados 
        self.enderecos.append(Endereco(rua, numero, bairro))
        
    def lista_endereco(self):
        for n in self.enderecos:
            print(n.rua, n.numero, n.bairro)
        
class Endereco:
    def __init__(self, rua, numero, bairro):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro

cliente = Cliente('Akin')
cliente.inserir_endereco('Criança', 32, 'Travesso')
cliente.inserir_endereco('Criança', 40, 'Travesso')

cliente.lista_endereco()