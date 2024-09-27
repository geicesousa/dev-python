#pip index versions <biblioteca>, mostra as versões disponíveis
#pip freeze gera o requiriments.txt pip freeze > requeriments.txt
#pip install -r requeriments.txt
# CADA VEZ QUE ESSE ARQUIVO É EXECUTADO CONSOME MEMÓRIA E UTILIZA RECURSOS, ELE ESTÁ CRIANDO E MODIFICANDO ARQUIVOS A CADA EXECUÇÃO

arquivo = open('arquivo_teste.txt', 'w')
arquivo.close()

#o with garante a abertura e o fechamento do arquivo - context manager
with open('arquivo_com_with.txt', 'w') as arquivo:
    arquivo.write('Nome:')
    arquivo.writelines('\n GEICE')
    print('aquivo criado')
    print('arquivo fechado')    
    
# w+ -> possibilita escrever e ler , o w apaga o que estava no arquivo e escreve novamente
# a -> coloca informações a partir da última linha escrita
# x -> cria o arquivo
with open('arquivo_com_with.txt', 'r') as arquivo:
    print(arquivo.readline())
    print()
    print(arquivo.read())

with open('arquivo_teste.txt', 'a') as arquivo:
    arquivo.write('linha inserida \n')
    print()
    arquivo.write('finalização do a')

# podemos usar o modulo 'os' para apagar o arquivo, usamos remove(<arq>) ou unlink(<arq>)
# o rename() renomeia, mas tbm serve para mover o arquivo de lugar

from pathlib import Path

caminho = Path()

print(caminho.home())
print(caminho.absolute())
novo_arquivo = Path(__file__)
print(novo_arquivo)
print(novo_arquivo.parent)

arquivo_pathlib = caminho.absolute() / 'arquivo_pathlib.txt'
arquivo_pathlib.touch() #cria o arquivo
arquivo_pathlib.write_text('Uma frase bem bonita') #escreve no arquivo
arquivo_pathlib.read_text() #lê o arquivo
#arquivo_pathlib.unlink() # apaga
#mkdir() # cria um diretório


# há um modulo python para compactar e descompactar arquivos zip
# zipfile.ZipFile
