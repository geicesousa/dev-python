import random

lista = ['frase', 'palavra', 'verbo', 'idioma', 'letra', 'linguagem']
nomes = ['Luiz', 'Maria', 'Helena', 'Joana']

# random.randrange(início, fim, passo)
r_range = random.randrange(10, 20, 2) # número inteiro aleatório dentro de um intervalo específico
print(r_range)

# random.randint(início, fim)
r_int = random.randint(10, 20) # número inteiro aleatório dentro de um intervalo 
print(r_int)

# random.uniform(início, fim)
r_uniform = random.uniform(10, 20) # número flutuante aleatório dentro de um intervalo 
print(r_uniform)

# random.shuffle(SequenciaMutável) -> 
random.shuffle(lista) # Embaralha a lista original
print(lista)

# random.sample(Iterável, k=N)
novos_nomes = random.sample(lista, k=3)# escolhe elementos do iterável e retorna outro iterável, sem repetir
print(novos_nomes)

# random.choices(Iterável, k=N)
novos_nomes = random.choices(lista, k=3) # escolhe elementos do iterável e retorna outro iterável, repete 
print(novos_nomes)

# random.choice(Iterável) -> Escolhe 1 elemento do iterável
print(random.choice(nomes))

# é um a boa prática gerar novas coisas ao invés de modificar as anteriores 

# random.seed(time.time()) o python usa o time para poder gerar os números aleatórios, então e aleatoriedade é simulada, se a gente passar os mesmo números como parâmetro do seed teremos os mesmos números, por isso não é indicado que usemos o módulo random para gerar senhas ou coisas que envolvam segurança, pq há como prever. Podemos usar o modulo secrets para isso
# se colocamos random.seed(10) no início do cógido ele usa o 10 como padrão para todas as execuções

import secrets
secrets_choice = secrets.choice(lista)
secrets_choice1 = secrets.choice(nomes)
secrets_rdbw = secrets.randbelow(100)
print(secrets_choice, secrets_choice1, secrets_rdbw)