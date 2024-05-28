# o valor da pizza de 2 sabores será sempre o mais caro - será inserido na regra de negócio
# dividir os sabores em classicos e premium (?)
cardapio = {
    "pizzas": {
        "marguerita_teste": {
            "id":1,
            "ingredientes": [],
            "tamanho": [
                {"P": 30.99},     
                {"G": 50.89}
            ]
        },
        "mussarela":{"preco": 40.49, "id":2},
        "portuguesa": {"preco": 50.99, "id":3},
        "napolitana": {"preco": 40.89, "id":4},
        "brie com geléia de pimenta": {"preco": 70.89, "id":5},
        "camarão e cream cheese": { "preco": 80.89, "id":6},
        "quatro queijos": { "preco": 60.89, "id":7},
        "baiana": { "preco": 50.89, "id":8},
        "lombinho": { "preco": 50.89, "id":9},
        "canadense": { "preco": 50.89, "id":0}
    },
    "bebidas": {
        "refrigerante": [
            { "tipo": "lata - 350ml", "preco": 11.99}, 
            { "tipo": "litro", "preco": 7.99}
        ], 
        "suco": [
            { "tipo": "garrafa - 500ml", "preco": 11.99}, 
            { "tipo": "copo - 300ml", "preco": 5.99}
        ], 
        "cerveja": [
            { "tipo": "garrafa - 600ml", "preco": 12.99}, 
            { "tipo": "long neck - 330ml", "preco": 9.99}, 
            { "tipo": "lata- 350ml", "preco": 5.99}
        ]
    },
    "sobremesas": { 
        "fatia de torta": 20, 
        "docinho": 3.50,
        "uma bola de sorvete": 5,
        "duas bolas de sorvete": 8
    }
}
