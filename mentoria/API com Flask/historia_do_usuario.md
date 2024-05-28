## API

#### Esse projeto visa trabalhar os conceitos de: Framework; Arquitetura WEB; Programação Orientada a Objeto; APIs; Organização de Projetos e Análise de Requisitos.

##### Objetivo geral: Construir uma API para um sistema de atendimento de uma Pizzaria

#### **História:**

>*"Estou tendo uma demanda muito grande e está difícil gerenciar pelo whatsapp. Fica difícil gerenciar a fila de pedidos e não atrasar os pedidos mais antigos. Outro dia por conta das várias mensagens acabamos esquecendo um pedido feito às 19h e só colocando ele de fato na cozinha quando o cliente cobrou o prazo de entrega, que era de 50 min. Ou seja, a pizza só chegou na casa do cliente quase 21h. Foi uma dor de cabeça horrível. Eu gostaria de um sistema que me permitisse receber os pedidos, identificando quando é 1 ou 2 sabores, que permitisse também exibir para o cliente o status desse pedido. O pagamento vai ser feito na entrega mas gostaríamos de saber quando levar troco ou a maquininha de cartão. Outro coisa que gostaríamos é ter o telefone das pessoas para mandar as ofertas promocionais numa lista de transmissão do whatsapp. Ah sim, seria bom também termos um relatório de vendas para acompanharmos o nosso faturamento. Vocês fazem esse serviço? Conseguem me entregar na semana que vem?"* 

1. Quais são os problemas que vocês enxergam aqui?
    
    - 

2. Quais são os requisitos desse projeto?

    - 

Os pedidos terão:
    - exibir o status do pedido para o cliente
    - saber a forma do pagamento - caso seja dinheiro, qnto de troco?
    - idetificar a qtd de sabores
    - cliente
    - id
    - ordenar os pedidos pelo horário de confirmação

----
Cliente:
    TEM: dados cadastrais (login, senha, endereço, telefone, nome), histórico de pedidos
    FAZ: pedidos, paga, acompanha o status do pedido, reclamação

Pedido: 
    TEM: status, cardápio, cliente, horário de criação, previsão de entrega (horário+50m),

Restaurante
    TEM: clientes, pedidos e histórico de vendas
    
**colocar uma lista de endpoints e o cardápio **
ENDPOINTS:
   Clientes:
    - GET (cardápio)
    - POST (pedido, cadastro)
    - PUT (pedido, cadastro)
   
   Restaurante:
    - GET (clientes, pedidos)
    - POST (itens cardápio)
    - PUT (cardapio, pedido, clientes - alterar end, tel)
    - DELETE (pedido, cliente, itens cardápio)
   
   Pedido:
    - GET
    - POST
    - DELETE

*****
    - GET: 
        exibir o cardápio,
        pegar pizzas, bebidas, sobremesas
    
    - PUT
        altera pedidos (o cliente poderá alterar?)
        alterar cardápio
    
    - POST
        criar os pedidos (clientes)
        criar sabores e novos itens no cardápio

    - DELETE
        deletar os pedidos (apenas o gerente?)