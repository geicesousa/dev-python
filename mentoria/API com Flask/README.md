### Acompanhamento das atividades

[ x ] criação dos cardápios

[ x ] criação de endpoints get

[ x ] exercício da criação de uma matilha 

[ x ] criação de endpoints post

[ x ] criação de endpoints put

[ x ] criação de endpoints delete

[  ] criação dos models

ROTAS CARDAPIO:
'/cardapio' - exibe todos os itens que o restaurante vende
'/cardapio/pizzas' - exibe o sabor de todas das pizzas
'/cardapio/pizzas/<sabor>' - exibe de acordo com o sabor os ingredientes, tamanhos e valor da pizza (ex.: portuguesa)
'/cardapio/bebidas' - exibe todos os itens de bebidas
'/cardapio/sobremesas' - exibe todas as sobremesas
'/cardapio/<categoria>' [post] - cria uma nova categoria no cardápio (ex.: petiscos)
'/cardapio/<categoria>/<tipo>' [post] - cria um novo item dentro de uma categoria (petiscos, batata-frita)
'/cardapio/<categoria>/<tipo>' [put] - edita um item específico do cardápio de acordo com a categoria
'/cardapio/<categoria>/<tipo>' [delete] - deleta um item de determinada categoria do cardápio
'/cardapio/bebidas/<tipo>/<int:index>' [delete] - deleta de bebidas um item de acordo com o id (ex.: cerveja)

ROTAS PEDIDOS:
'/pedidos' - exibe todos os pedidos do restaurante
'/pedidos/<int:id>' - exibe um pedido de acordo com o id 
'/pedidos' [post] - cria um pedido
'/pedidos/<int:id>' [put] - modifica o pedido de acordo com o id
'/pedidos/<int:id>' [delete] - deleta o pedido de acordo com o id

ROTAS CLIENTES:
'/clientes' - exibe uma lista com todos os clientes
'/clientes/<value>' - exibe um cliente de acordo com o id (ex.: io90)
'/clientes' [post] - cria um novo cliente 
'/clientes/<value>' [put] - atualiza/modifica um cliente de acordo com o id

ROTA RELATÓRIO:
'/relatorio' - exibe relatório de vendas