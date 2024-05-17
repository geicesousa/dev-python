from flask import  Flask, jsonify, request

cardapio = {
    "pizzas": [ 
        {"sabor": "marguerita", "preco": 50.89, "id":1},
        {"sabor": "mussarela", "preco": 40.49, "id":2},
        {"sabor": "portuguesa", "preco": 50.99, "id":3},
        {"sabor": "napolitana", "preco": 40.89, "id":4},
        {"sabor": "brie com geléia de pimenta", "preco": 70.89, "id":5},
        {"sabor": "camarão e cream cheese", "preco": 80.89, "id":6},
        {"sabor": "quatro queijos", "preco": 60.89, "id":7},
        {"sabor": "baiana", "preco": 50.89, "id":8},
        {"sabor": "lombinho", "preco": 50.89, "id":9},
        {"sabor": "canadense", "preco": 50.89, "id":0},
    ], 
    "bebidas":[
        {"refrigerante": "lata - 350ml", "preco": 7.99},
        {"cerveja": "lata - 350ml", "preco": 6.99},
        {"cerveja": "long neck - 355ml", "preco": 10.99},
        {"suco": "jarra - 500ml", "preco": 10.99},
        {"suco": "copo - 350ml", "preco": 7.99},
    ], 
    "sobremesas": [
        {},
        {},
        {},
    ]
}

app = Flask(__name__)

@app.route('/cardapio')
def get_cardapio():
    return jsonify(cardapio)

@app.route('/cardapio/pizza/{value}')
def get_cardapio_value(value):
    pass



app.run(port=5000, host='localhost', debug=True)