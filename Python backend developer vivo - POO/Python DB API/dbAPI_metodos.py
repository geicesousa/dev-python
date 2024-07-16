import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent #caminho até essa pasta

# cria o documento
bd = sqlite3.connect(ROOT / 'banco_de_dados.sqlite') # a extensão poderia ser .db, mas nem toda extensão do vscode lê; baixei uma extensão que lê o documento e exibe como uma tabela do SQL

cursor = bd.cursor()

#criar tabela
def criar_tabela(bd, cursor):
    cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(200), endereco VARCHAR(300))') 
    #escreve em SQL
    bd.commit() 

#inserir registros na tabela
def inserir_registros(bd, cursor, nome, email, endereco):
    dados = (nome, email, endereco)
    cursor.execute('INSERT INTO clientes (nome, email, endereco) VALUES (?,?,?)', dados) 
    # poderíamos passar as informações direto no values, mas é arriscado fazer direto pois podem passar comando sql dentro e prejudicar o funcionamento do software, então passamos as ? e inserimos uma tupla; a ? funciona como um placeholder

    #salva no banco
    bd.commit() 

# inserir_registros(bd, cursor, 'Luiza', 'luiza@email.com', 'dorin, salvador-ba')

#atualizar registros
dados = ('Maria Luiza', 'luiza@email.com', 'doron, salvador-ba', 4)
cursor.execute(' UPDATE clientes SET nome=?, email=?, endereco=? WHERE id=?', dados)
bd.commit()
#não fazer update sem usar o WHERE pq senão atualiza a tabela inteira e daruim

#deletar registros
def deletar_registros(bd, cursor, id):
    num_id= (id,) #em uma tupla com apenas 1 valor temos que usar vírgula
    cursor.execute('DELETE FROM clientes WHERE id=?', num_id)
    bd.commit()

# inserção de muitos registros, em lote
def inserir_muitos_dados(bd, cursor, dados):
     #lista de tuplas
    cursor.executemany('INSERT INTO clientes (nome, email, endereco) VALUES (?,?,?)', dados)
    bd.commit()

dados = [('Cristiano', 'cristiano@email.com', 'Calabar'),('Claudia', 'claudia@email.com', 'caminho das árvores, salvador-ba'),('Adana', 'adana@email.com', 'brotas, salvador-ba'),('Ricardo', 'ricardo@email.com', 'periperi, salvador-ba')]

#inserir_muitos_dados(bd, cursor, dados)

#PESQUISAS
#apenas 1 resultado
def exibe_cliente_por_id(cursor, id):
    cursor.execute('SELECT * FROM clientes WHERE id=?', (id,))
    result = cursor.fetchone()
    print(f'''Cliente de id {id}: {result}''')


exibe_cliente_por_id(cursor,8)

def uso_row_factory(cursor, id):
    print('ROW_FACTORY') # é um atributo usado para "transformar" as linhas do bd em objetos python 
    cursor.row_factory = sqlite3.Row #
    cursor.execute('SELECT * FROM clientes WHERE id=?', (id,))
    result = cursor.fetchone()
    return result

row_factory = uso_row_factory(cursor,2)
print(f''' row factory transformado em diconário e manipulável através da chave
{dict(row_factory)}
id: {dict(row_factory)['id']}
nome: {dict(row_factory)['nome']}
email: {dict(row_factory)['email']}
''')

#lista todos os itens da lista
lista_clientes = cursor.execute('SELECT * FROM clientes')
#ordenado
lista = cursor.execute('SELECT * FROM clientes ORDER BY nome ASC')
print(lista_clientes) # imprime o primeiro e sqlite3.Cursor object at 0x791144c5a7c0, para aparecer todos temos que fazer um for

print('lista:')
for cliente in lista:
    pass #print(cliente) #esse resultado é sempre uma tupla (imutável)

print()
print('GERENCIAMENTO DE TRANSAÇÕES')
#boa prática usar o rollback() pq, em caso de erro de execução, ele reverte a transação e deixa o bd da forma que encontrou; isso garantirá a consistência de dados
try:
    pass # operação qualquer, todas as operações devem vir antes, de UPDATE, DELETE, INSERT INTO
    bd.commit()
except Exception as e:
    print(f'Ocorreu um erro. {e}')
    bd.rollback()

finally:
    cursor.close()
    bd.close()