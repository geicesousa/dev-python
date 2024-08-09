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
    {
    'pergunta' : '',
    'alternativas': [],
    'resposta': '',
    },
]

for dic in perguntas:
    print(dic.items())


print(perguntas[0].items())
print(perguntas[0].keys())
print(perguntas[0].values())


