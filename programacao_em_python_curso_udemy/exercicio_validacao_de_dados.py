# mudar: nº de faltas 0 - 20 e nota entre 0-10, o programa não deve ser interrompido
# := warlus operator - usa e armazena um dado numa variável ao mesmo tempo variavel := input('pergunta') 
# amount_students = input('digite a quantidade de alunos que a turma possui: ')
# amount_students_number = int(amount_students)
# while amount_students_number <= amount_students_number:
# if amount_students_number:
# print(amount_students_number)

students = []

name = str(input('Nome: ')).lower()

valid = False
while valid == False:
    note_1 = input('Nota 1: ')
    try:
        note_1 = float(note_1)
        if note_1 < 0 or note_1 > 10:
            print('a nota deve ser um valor entre 0 - 10 e os decimos separados por "."')
        else: 
            valid = True
    except:
        print('A nota deve ser um números e os décimos devem ser separados por "."')

valid = False # aqui repete o valid pq no else ele foi atribuído como true
while valid == False:
    note_2 = input('Nota 2: ')
    try:
        note_2 = float(note_2)
        if note_2 < 0 or note_2 > 10:
            print('a nota deve ser um valor entre 0 - 10 e os decimos separados por "."')
        else: 
            valid = True
    except:
        print('A nota deve ser um números e os décimos devem ser separados por "."')

valid_fouls = False
while valid_fouls == False:
    fouls = input('Quantidade de faltas: ')
    try:
        fouls = int(fouls)
        if fouls < 0 or fouls > 20:
            print('O número de faltas deve ser entre 0- 20')
        else:
            valid_fouls = True
    except:
        print('A quantidade de faltas deve ser um número entre 0 - 10')

students.append([name, note_1, note_2, fouls])
# adc_new = input('adicionar novo aluno? ').lower()

print(students)

average = (note_1 + note_2) / 2
attendance = (20-fouls) / 20

print(f'''Estudante: {name}
       Obteve média de {average} e {attendance * 100} % de presença.''')

if average > 6 and attendance >= 0.7:
    print(f'''Estudante: {name} | Situação: Aprovad@''')

else: 
    print(f'''Estudante: {name} | Situação: Reprovad@''')

