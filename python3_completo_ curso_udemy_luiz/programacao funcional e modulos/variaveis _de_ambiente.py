import os
from dotenv import load_dotenv # type: ignore
github = os.getenv('github_username'.upper())
nexus = os.getenv('nexus_username'.upper())
print(github)
print(nexus)
print(os.environ) # exibe TODAS as VARIAVEIS DE AMBIENTE

# load_dotenv()
# devemos criar sempre um .env-example para deixar como modelo e nunca subimos o nosso arquivo .env, ele deve estar sempre no gitignore, por uma questão de segurança

# 
# 
# 

