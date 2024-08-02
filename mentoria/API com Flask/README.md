## API COM FLASK

Esta API permite ao usuário _**visualizar**_ cardápio (pizza, bebidas, sobremesas), clientes, pedidos e relatório de vendas; **_criar_** pedidos, clientes, nova categoria no cardápio, novos itens/sabores em categorias já existentes (pizza, bebidas, sobremesas); _**modificar**_ dados dos clientes, informações do cardápio, pedidos; _**deletar**_ itens em categorias existentes

#### ROTAS CARDAPIO:

'/cardapio' - exibe todos os itens que o restaurante vende <br/>
'/cardapio/pizzas' - exibe o sabor de todas das pizzas  <br/> 
'/cardapio/pizzas/<str:sabor>' - exibe de acordo com o sabor os ingredientes, tamanhos e valor da pizza (ex.: portuguesa)  <br/>
'/cardapio/bebidas' - exibe todos os itens de bebidas  <br/>
'/cardapio/sobremesas' - exibe todas as sobremesas  <br/>
'/cardapio/<str:categoria>' [POST] - cria uma nova categoria no cardápio (ex.: petiscos)  <br/>
'/cardapio/<str:categoria>/<str:tipo>' [POST] - cria um novo item dentro de uma categoria (petiscos, batata-frita)  <br/>
'/cardapio/<str:categoria>/<str:tipo>' [PUT] - edita um item específico do cardápio de acordo com a categoria  <br/>
'/cardapio/<str:categoria>/<str:tipo>' [DELETE] - deleta um item de determinada categoria do cardápio  <br/>
'/cardapio/bebidas/<str:tipo>/<int:index>' [DELETE] - deleta de bebidas um item de acordo com o id (ex.: cerveja)  <br/>

#### ROTAS PEDIDOS:

'/pedidos' - exibe todos os pedidos do restaurante  <br/>
'/pedidos/<int:id>' - exibe um pedido de acordo com o id   <br/>
'/pedidos' [POST] - cria um pedido  <br/>
'/pedidos/<int:id>' [PUT] - modifica o pedido de acordo com o id  <br/>
'/pedidos/<int:id>' [DELETE] - deleta o pedido de acordo com o id

#### ROTAS CLIENTES: 

'/clientes' - exibe uma lista com todos os clientes  <br/>
'/clientes/<str:value>' - exibe um cliente de acordo com o id (ex.: io90)  <br/>
'/clientes' [POST] - cria um novo cliente   <br/>
'/clientes/<str:value>' [PUT] - atualiza/modifica um cliente de acordo com o id <br/>

#### ROTA RELATÓRIO:  

'/relatorio' - exibe relatório de vendas <br/>

### Acompanhamento das atividades

[ x ] criação dos cardápios

[ x ] criação de endpoints get

[ x ] exercício da criação de uma matilha 

[ x ] criação de endpoints post

[ x ] criação de endpoints put

[ x ] criação de endpoints delete

[  ] criação dos models 

[  ] persistir dados 