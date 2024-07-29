restaurante = {
  "pedidos": [
    {
      "status": "em andamento",
      "criado_as": "datetime",
      "cliente": "clientes.id",
      "previsao_entrega": "criado_as + 50min",
      "sabor": "baiana",
      "tamanho": "G",
      "pagamento": "cartão",
      "troco": "não"
      
    }
    ],
  "clientes": [
    {
      "id": "io90",
      "dados_cadastrais": {
        "nome": "Carlos", 
        "email": "carlos@gmail.com",
        "endereco": "Rua Clemente Mariane, 3000, Boca do Rio",
        "telefone": "(71)9 8000-0000",
        "senha": "carlos123"
      },
      "historico_pedidos": [],

    }
    ],
    "historico_vendas": [
        {}
    ]
}

pedidos = [
  {
    "status": "em andamento",
    "criado_as": "datetime",
    "cliente": "io90", 
    "previsao_entrega": "criado_as + 50min",
    "id": 1,
    "sabor": "baiana",
    "tamanho": "G",
    "pagamento": "cartão"
  },
  {
    "status": "finalizado",
    "criado_as": "23h",
    "cliente": "Flaviana",
    "previsao_entrega": "criado_as + 50min",
    "id": 2,
    "sabor": "brie com geléia de pimenta",
    "tamanho": "P",
    "pagamento": "dinheiro",
    "troco": "sim"
  },
  {
    "status": "em andamento",
    "criado_as": "datetime",
    "cliente": "teste",
    "previsao_entrega": "criado_as + 50min",
    "id": 3,
    "sabor": "portuguesa",
    "tamanho": "G",
    "pagamento": "dinheiro",
    "troco": "não"
  },
  {
    "status": "saiu para entrega",
    "criado_as": "datetime",
    "cliente": "Cicrana",
    "previsao_entrega": "criado_as + 50min",
    "id": 5,
    "sabor": "canadense",
    "tamanho": "P",
    "pagamento": "cartão",
    "troco": "sim"
  },
]

clientes = [
  {
    "id": "io90",
    "dados_cadastrais": {
      "nome": "Carlos", 
      "email": "carlos@gmail.com",
      "endereco": "Rua Clemente Mariane, 3000, Boca do Rio",
      "telefone": "(71)9 8000-0000",
      "senha": "carlos123"
    },
    "historico_pedidos": [],
  },
  {
    "id": "123",
    "dados_cadastrais": {
      "nome": "Manoel", 
      "email": "manoel@gmail.com",
      "endereco": "Rua Jubiabá, 500, Rio Claro",
      "telefone": "(71)9 9999-0000",
      "senha": "manoel123"
    },
    "historico_pedidos": [],
  },
  {
    "id": "io70",
    "dados_cadastrais": {
      "nome": "Gabriela", 
      "email": "Gabriela@gmail.com",
      "endereco": "Rua Cravo e canela, 690, Jorge Amado",
      "telefone": "(71)9 8888-0000",
      "senha": "Gabriela123"
    },
    "historico_pedidos": [],
  },
  {
    "id": "io60",
    "dados_cadastrais": {
      "nome": "Jeovana", 
      "email": "Jeovana@gmail.com",
      "endereco": "Rua Forninho, 690, Anos doismil",
      "telefone": "(71)9 2000-0000",
      "senha": "Jeovana123"
    },
    "historico_pedidos": [],
  },
]

relatorio_vendas = [
  {}
]