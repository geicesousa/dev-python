# Iterador é um objeto que contém um número contável de itens, uma lista (array, tuple, list) iterável; para uma classe ser iterável temos que ter os iteradores declarados, lembrando de estabelecer sempre a condição de parada, pode ser usado o StopInteration
# métodos iteradores: __iter__() __next__()

class Iterador:

    def __init__(self, argumento):
        self.lista = argumento
        self.contador = 0

    def __iter__(self):
        return self    

    def __next__(self):
        try:
            nomes = self.lista[self.contador]
            self.contador += 1
            print(f'{nomes} contando: {self.contador}')

        except IndexError:
            raise StopIteration
            # raise invoca uma exceção dada qualquer condição estabelecida
            # assert invoca uma exeção dada uma condição false, para acontecer a exceção tem que haver uma condição falsa

lista = 'mãe', 'filho', 'familia', 'escola', 'comunidade'

for i in Iterador(lista):
    i # não precisa do print pq na class tem print e não return

# Geradores são tipos especiais de iteradores, eles não armazena todos os valores na memória e isso otimiza o funcionamento do programa; são definidos usando funções e usamos o yield no lugar do return
# geradores armazenam o estado atual e traz um valor, após isso a execução é pausada e quando chamada de novo traz o próximo valor/item da sequência 
# depois que um item for consumido não pode ser mais acessado, 

# exemplo abstrato (aplicável a um crawler)
# import requests

# def fetch_products(url, max_pages = 100):
#     page = 1
#     while page <= max_pages:
#         response = requests.get(f'{url}?page={page}')
#         data = response.json()

#         for product in data['products']:
#             yield product
#         if 'next_page' not in data:
#             break
#         page += 1

    # enquanto page for menor que o máximo de páginas, ele vai buscar a url com a página + 1 e a cada produto encontrado na resposta da requisição ele vai gerar o produto quando não tiver mais 'next_page' na resposta da requisição ele para, se houver +101 páginas, ele tbm para
     

def gerador(lista):
    for item in lista:
        yield item

print()
print('Gerador')
for i in gerador(lista):
    print(i)

# O uso do gerador é mais simples e seu caso de uso é para casos simples (apenas um controle de fluxo, quando a otimização de memória for o pré-requisito); casos mais complexos é mais indicado que usemos o iterador, usando a classe como um modelo 