import calendar
# por padrao o dia da semana começa com 0(seg) e acaba com 6(dom)
# print(calendar.calendar(2024))
print(calendar.month(1992, 12))
print(calendar.monthrange(1992, 12), 'dezembro/1992') # retona uma tupla com o primeiro dia da semana representado num nº de 0-6 e ultimo dia do mês(30/31/29/28)
print(calendar.monthrange(2023, 6), 'junho/2023') 
print(calendar.monthrange(2023, 2), 'fevereiro/2023') 
print(calendar.monthrange(2024, 2), 'fevereiro/2024') 

print()
print(list(calendar.day_name)) 
print(list(enumerate(calendar.day_name))) 
print('abreviaturas:', list(calendar.day_abbr)) 
# weekday, para os dias da semana

print()

semanas_mes = calendar.monthcalendar(1992,12)
print('Semanas', semanas_mes)  
