perguntas = [
    {
    'pergunta' : 'Quais o menor e o maior país do mundo?',
    'alternativas': ['a) Vaticano e Rússia', 'b) Nauru e China', 'c) Mônaco e Canadá', 'd) São Marino e Índia'],
    'resposta': 'a) Vaticano e Rússia',
    },
    {
    'pergunta' : 'O que a palavra legend significa em português?',
    'alternativas': ['a) Legenda', 'b) História', 'c) Lenda', 'd) Legendário'],
    'resposta': 'c) Lenda',
    },
    {
    'pergunta' : 'Quanto tempo a luz do Sol demora para chegar à Terra?',
    'alternativas': ['a) 1 dia', 'b) 12 minutos', 'c) 12 horas', 'd) 8 minutos'],
    'resposta': 'd) 8 minutos',
    },
    # {
    # 'pergunta' : '',
    # 'alternativas': [],
    # 'resposta': '',
    # },
]

        
respostas = []

i = 0
for dic in perguntas:
    
    cada_pergunta = (dic['pergunta'])
    print(cada_pergunta, '\n',  dic['alternativas'])
    resposta = input('Resposta: ')
    respostas.append(resposta)

print()    
print('Suas respostas foram:', respostas)
print('Respostas corretas:') 
print()    

for dic in perguntas:
    
    cada_pergunta = (dic['pergunta'])
    print(cada_pergunta, '\n',  dic['resposta'])
 
#resolução curso
# qtd_acertos = 0
# for pergunta in perguntas:
    # print('Pergunta:', pergunta['Pergunta'])
    # print()

    # opcoes = pergunta['Opções']
    # for i, opcao in enumerate(opcoes):
        # print(f'{i})', opcao)
    # print()

    # escolha = input('Escolha uma opção: ')

    # acertou = False
    # escolha_int = None
    # qtd_opcoes = len(opcoes)

    # if escolha.isdigit():
        # escolha_int = int(escolha)

    # if escolha_int is not None:
        # if escolha_int >= 0 and escolha_int < qtd_opcoes:
            # if opcoes[escolha_int] == pergunta['Resposta']:
                # acertou = True

    # print()
    # if acertou:
        # qtd_acertos += 1
        # print('Acertou 👍')
    # else:
        # print('Errou ❌')

    # print() print('Você acertou', qtd_acertos) print('de', len(perguntas), 'perguntas.')
