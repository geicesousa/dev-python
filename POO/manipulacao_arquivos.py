import os
import shutil 
from pathlib import Path

# open() close()
# w de write(escreve e sobreescreve)
# r de read (lê)
# a (armazena/anexa) sem sobreescrever

arquivo = open('/home/jusbrasil/Área de trabalho/Geice/python_estudos/POO/novo_arquivo.txt', 'w', encoding='utf-8')
nome = "nome"
arquivo.write('Criando e escrevendo no arquivo \n') # os dados anteriores são apagados
arquivo.writelines(nome)
arquivo.writelines(['\n', 'nova linha', '\n'])
dados = {"nome": "geice", "idade": 27, "profissão": "software engieneer"}
arquivo.writelines(str(dados)) # transforma em str pq o writelines não suporta dicts
arquivo.close()

poema = open('/home/jusbrasil/Área de trabalho/Geice/python_estudos/POO/poema.txt', 'r')
# print('texto completo:')
# print(poema.read())

print()

print('linha do texto:')
print(poema.readline())


print()

print('traz uma lista com todas as linhas do texto:')
print(poema.readlines())

poema.close()

print()

poema = open('/home/jusbrasil/Área de trabalho/Geice/python_estudos/POO/poema.txt', 'r')

contador = 0
while len(linha := poema.readline()):
    print(contador, linha)
    contador +=1

# for linha in poema.readlines():
#    print(linha) # mesmo que o while

poema.close()

# __file__ mostra o caminho completo do arquivo, o parent vai garantir que mostre a pasta
root = Path(__file__).parent
print(root)
# criar_pasta = os.mkdir(root /'nova_pasta_teste')
novo_arquivo = open(root / 'arquivo_teste.txt', 'w')
novo_arquivo.close()

os.rename(root / 'novo_arquivo.txt', root / 'arquivo_renomeado.txt')

para_deletar = open(root / 'delete.txt', 'w')
para_deletar.close()

os.remove(root / 'delete.txt') # exclui o arquivo criado acima

shutil.move(root / 'arquivo_teste.txt', root / 'nova_pasta_teste' / 'arquivo_teste.txt')

print()

