from pathlib import Path

root = Path(__file__).parent
print(root)

# tratando erros durante a manipulação de arquivos, erros mais comuns: FileNotFoundError, PermissionError, IOError, UnicodeDecodeError(leitura), UnicodeEncodeError(gravar), IsADirectoryError
print('ERROS')

try:
    open(root / 'trator.txt', 'r')
    open(root / 'nova_pasta_teste' )

except FileNotFoundError as exc :
    print('arquivo não encontrado')
    print(exc)

print()
try:
    open(root / 'nova_pasta_teste' )

except IsADirectoryError as exc :
    print('é um diretório')
    print(exc)

print()

# boas práticas
# o with vai garantir que o arquivo seja fechado - file.close()

with open(root / 'poema.txt', 'r') as arquivo:
    print('arquivo aberto')
    print(arquivo.read())
    print('arquivo fechado')

#print(arquivo.read()) # não consegue mais ler o arquivo 
print()

try:
    with open(root / 'arquivo.txt', 'r') as arquivo:
        print('arquivo okay')

except IOError as exc:
    print('arquivo não pode ser aberto')
    print(exc)