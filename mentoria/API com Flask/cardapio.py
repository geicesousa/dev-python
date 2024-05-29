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
        "mussarela":{
            "id":2, 
            "ingredientes": [],
            "tamanho": [
                {"P": 28.99},     
                {"G": 40.49}
            ]} ,
        "portuguesa": {
            "id":3, 
            "ingredientes": [],
            "tamanho": [
                {"P": 38.99},     
                {"G": 50.99}
            ]},
        "napolitana": {
            "id":4, 
            "ingredientes": [],
            "tamanho": [
                {"P": 29.99},     
                {"G": 40.89}
            ]},
        "brie com geléia de pimenta": {
            "id":5, 
            "ingredientes": [],
            "tamanho": [
                {"P": 48.99},     
                {"G": 70.89}
            ]},
        "camarão e cream cheese": { 
            "id":6, 
            "ingredientes": [],
            "tamanho": [
                {"P": 56.99},     
                {"G": 80.89}
            ]},
        "quatro queijos": {
            "id":7, 
            "ingredientes": [],
            "tamanho": [
                {"P": 42.99},     
                {"G": 60.89}
            ]},
        "baiana": { 
            "id":8, 
            "ingredientes": [],
            "tamanho": [
                {"P": 38.99},     
                {"G": 50.89}
            ]},
        "lombinho": { 
            "id":9, 
            "ingredientes": [],
            "tamanho": [
                {"P": 38.99},     
                {"G": 50.89}
            ]},
        "canadense": { 
            "id":0, 
            "ingredientes": [],
            "tamanho": [
                {"P": 48.99},     
                {"G": 60.89}
            ]}
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
