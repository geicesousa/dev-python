from flask import  Flask, jsonify, request
from cardapio import cardapio

app = Flask(__name__)

@app.route('/')
def get_cardapio():
    return jsonify(cardapio)

@app.route('/pizza')
def get_pizza():
    return jsonify(cardapio.get('pizzas'))

@app.route('/pizza/<sabor>')
def get_sabor(sabor):
    return jsonify(cardapio.get('pizzas').get(sabor))

@app.route('/bebidas')
def get_bebidas():
    return jsonify(cardapio.get('bebidas'))

@app.route('/sobremesas')
def get_sobremesas():
    return jsonify(cardapio.get('sobremesas'))

app.run(port=5000, debug=True)

