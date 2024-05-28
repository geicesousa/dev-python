from flask import  Flask, jsonify, request
from cardapio import cardapio
from markupsafe import escape # proteje de ataques de injeção de códigos, colocar códigos maliciosos com a intenção de interromper o funcionamento ou roubar dados 

app = Flask(__name__)

#------- CARDÁPIO ------#
@app.route('/cardapio')
def get_cardapio():
    return jsonify(cardapio)

@app.route('/cardapio/pizza')
def get_pizza():
    return jsonify(cardapio.get('pizzas'))

@app.route('/cardapio/pizza/<sabor>')
def get_sabor(sabor):
    return jsonify(cardapio.get('pizzas').get(escape(sabor)))

@app.route('/cardapio/bebidas')
def get_bebidas():
    return jsonify(cardapio.get('bebidas'))

@app.route('/cardapio/sobremesas')
def get_sobremesas():
    return jsonify(cardapio.get('sobremesas'))

# POST, PUT E DELETE
# usar o preço como um filtro 
# as alterações e criações serão feitas sempre usando uma API Client, como o postman ou insomnia 
# criar o put e o delete usando id e/ou nome, basta passar por paramentro o metodos que desejamos


#------- PEDIDOS ------#
@app.route('/pedidos')
def get_pedidos():
    pass
    # return jsonify(pedidos)

@app.route('/pedidos/<int:id>')
def get_pedidos_id(id):
    pass
    # return jsonify(pedidos.get(escape(id)))

@app.route('/pedidos/<int:id>', methods = ['DELETE','PUT']) 
# deleta ou modifica o pedido pelo id
def pedidos_por_id(id):
   pass


#------- CLIENTES ------#
@app.route('/clientes')
def get_clientes():
    pass
    # return jsonify(clientes)

@app.route('/clientes/<int:id>', methods=['GET', 'PUT'])
# na função eu vou criar uma condição para cada metodo usando o request.method == PUT or GET
def clientes_id(id):
    pass
    # return jsonify(clientes.get(escape(id)))

@app.route('/clientes/<int:id>', methods = ['DELETE']) 
# deleta o cliente pelo id
def delete_clientes_por_id(id):
   pass

app.run(port=5000, debug=True, use_reloader=True) 

