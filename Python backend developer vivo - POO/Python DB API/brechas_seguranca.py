import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent
conexao_bd = sqlite3.connect(ROOT / 'banco_de_dados.sqlite')
cursor = conexao_bd.cursor()
cursor.row_factory = sqlite3.Row

id = input('Informe o ID que deseja consultar') # 3 OR 4=4, ou qualquer outro comando SQL, 3 é um id que não existe e mesmo assim vem o dado de um cliente, ou seja, dado vazado 
cursor.execute(f'SELECT * FROM clientes WHERE id={id}')

#não é uma boa prática permitir passar os dados como string, o ideal é usar a ? e a tupla - como esta no arquivo de métodos 

cliente = cursor.fetchone()

if cliente:
    print(dict(cliente))
else:
    print('id não encontrado')

#se fosse fechall(), viria a lista completa de todos os clientes com a injeção de dados, poderia ser um DELETE 
# clientes = cursor.fetchall()

# if clientes:
#     for cliente in clientes:
#         print(dict(cliente))
# else:
#     print('id não encontrado')


# outra boa prática é fechar o cursor e a conexão
cursor.close()


conexao_bd.close()
