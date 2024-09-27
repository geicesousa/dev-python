import os
import shutil

# para interação com o sistema operacional

print(20 * 'a')
os.system('clear')
print('printou e apagou')
caminho = ''
os.path.exists(caminho)
os.path.split(caminho)
os.path.splitext(caminho)
os.path.isdir(caminho)
os.path.isfile(caminho)

# os.listdir(dir)  #passeia pelos diretórios
# os.walk(dir)  #navega pelos caminhos recursivamente
# os.unlink(dir) #apaga todos os documentos de uma pasta
# os.rename 
# os.shutil # move, copia e apaga arquivos, tem que instalar
# shutil.move
# shutil.copy
# shutil.copytree #copia a arvore inteira
# shutil.rmtree(ignore_errors=True) # remove mesmo com arquivos dentro, não vai pra lixeira
#
print(os.path.expanduser('~'))
# os.makedirs('pasta', exist_ok=bool) # cria um novo diretório, se existir não dá erro