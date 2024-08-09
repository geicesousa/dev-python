from flask import  Flask, jsonify, request
from cardapio import cardapio
from restaurante import pedidos, clientes, relatorio_vendas
from markupsafe import escape # proteje de ataques de injeção de códigos, colocar códigos maliciosos com a intenção de interromper o funcionamento ou roubar dados | retorna uma string, as vezes com simbolos &#

app = Flask(__name__)

#------- CARDÁPIO ------#
@app.route('/cardapio') # exibe o cardápio
def get_cardapio():
    return jsonify((cardapio))

@app.route('/cardapio/pizzas') # exibe a sessão de pizzas
def get_pizza():
    return jsonify(cardapio.get('pizzas'))

@app.route('/cardapio/pizzas/<sabor>') # exibe um sabor específico de pizza
def get_sabor(sabor):
    return jsonify(cardapio.get('pizzas').get(escape(sabor)))

@app.route('/cardapio/bebidas') # exibe a sessão de bebidas
def get_bebidas():
    return jsonify(cardapio.get('bebidas'))

@app.route('/cardapio/sobremesas') # exibe a sessão de sobremesas
def get_sobremesas():
    return jsonify(cardapio.get('sobremesas'))

@app.route('/cardapio/<categoria>', methods = ['POST'])
#cria uma nova seção dentro de pizza/sobremesa/bebidas
def cria_nova_categoria(categoria):
    pega_rota = cardapio.get(categoria)
    novo_item = request.get_json()
    pega_rota.update(novo_item) # update pq cria um dicionário
    
    return jsonify(cardapio.get(categoria))

@app.route('/cardapio/<categoria>/<tipo>', methods = ['POST'])
# cria um novo item dentro de cada tipo de sob
def cria_novo_item_especifico(categoria, tipo):
    pega_rota = cardapio.get(categoria).get(tipo)
    novo_item = request.get_json()
#try:
    if categoria == 'bebidas' or categoria == 'sobremesas':
        pega_rota.append(novo_item) #append pq insere um item numa lista
    elif categoria == 'pizzas':
        pega_rota.update(novo_item)
    elif categoria and tipo:
        pega_rota.append(novo_item)
    else:
        return "Erro. Caminho não encontrado."
    
    return jsonify(cardapio.get(categoria).get(tipo))
#except AttributeError:

# AJUSTAR o PUT de cardapio - insere o body apenas no primeiro item

@app.route('/cardapio/<categoria>/<tipo>', methods=['PUT'])
def edita_item(categoria, tipo):
    item_modificado = request.get_json()
    for item in cardapio[categoria][tipo]:
        item.update(item_modificado)
        return jsonify(cardapio.get(categoria).get(tipo))


@app.route('/cardapio/<categoria>/<tipo>', methods = ['DELETE']) 
# deleta seção do cardapio pelo id
def deleta_item_do_cardapio(categoria, tipo):
    del cardapio[categoria][tipo]

    return jsonify(cardapio.get(categoria))

@app.route('/cardapio/bebidas/<tipo>/<int:index>', methods = ['DELETE']) 
# deleta item especifico de cada bebida
def deleta_item_especifico_do_cardapio( tipo, index):
    del cardapio['bebidas'][tipo][index]

    return jsonify(cardapio.get('bebidas'))

#------- PEDIDOS ------#
@app.route('/pedidos')
# exibe a lista com todos os pedidos
def get_pedidos():
    return jsonify(pedidos)

@app.route('/pedidos/<int:id>')
def get_pedidos_id(id):
    for pedido in pedidos:
        if pedido.get('id') == id:
            return jsonify(pedido)

@app.route('/pedidos', methods = ['POST'])
def cria_pedido():    
    novo_pedido = request.get_json()
    pedidos.append(novo_pedido)
    # como gerar um novo id - fazer um random e comparar com os ids já existentes, se já existir, multiplicar por 2  
    # e a hora?
    return jsonify(pedidos)

@app.route('/pedidos/<int:id>', methods = ['PUT']) 
#INSERIR STATUS NA ROTA para garantir que apenas o status possa ser modificado
# modifica o (status) pedido pelo id
def edita_pedido(id):
    pedido_modificado = request.get_json()
    for index, pedido in enumerate(pedidos):
        if pedido.get('id') == id:
            pedidos[index].update(pedido_modificado)
            return jsonify(pedidos[index])

@app.route('/pedidos/<int:id>', methods = ['DELETE']) 
# deleta  o pedido pelo id
def deleta_pedido(id):
    for index, pedido in enumerate(pedidos):
        if pedido.get('id') == id:
            del pedidos[index]

    return jsonify(pedidos)

#------- CLIENTES ------#
@app.route('/clientes')
def get_clientes():
    return jsonify(clientes)

@app.route('/clientes/<value>')
def get_clientes_id(value):
    for cliente in clientes:
        if cliente.get('id') == value:
            return jsonify(cliente)

@app.route('/clientes', methods=['POST'])
def cria_cliente():
    novo_cliente = request.get_json()
    clientes.append(novo_cliente)
    return jsonify(clientes)

@app.route('/clientes/<value>',  methods=['PUT'])
def modifica_cliente(value):
    atualizacao = request.get_json()
    for cliente in clientes:
        if cliente.get('id') == value:
            cliente.update(atualizacao)
            return jsonify(cliente)


#------- RELATÓRIO DE VENDAS ------#
@app.route('/relatorio')
def get_relatorio_vendas():
    return jsonify(escape(relatorio_vendas))


app.run(port=5000, debug=True, use_reloader=True) 

