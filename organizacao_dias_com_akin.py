from datetime import datetime, timedelta
import pandas as pd

# Definir a data inicial (por exemplo, uma segunda-feira)
start_date = datetime(2025, 8, 4)  # Segunda-feira
weeks = 8  # Quantas semanas mostrar (ajustável)

# Responsáveis
responsibles = ['Responsável A', 'Responsável B']

# Criação da agenda
days = []
assignments = []

for week in range(weeks):
    current_date = start_date + timedelta(weeks=week)
    
    # Alternância: semanas pares (0, 2, 4...) seguem um padrão, ímpares o inverso
    if week % 2 == 0:
        # Semana par: A (Seg-Qua), B (Qui-Dom)
        for i in range(7):
            day = current_date + timedelta(days=i)
            if i < 3:
                days.append(day)
                assignments.append('Responsável A')
            else:
                days.append(day)
                assignments.append('Responsável B')
    else:
        # Semana ímpar: A (Seg-Quinta), B (Sex-Dom)
        for i in range(7):
            day = current_date + timedelta(days=i)
            if i < 4:
                days.append(day)
                assignments.append('Responsável A')
            else:
                days.append(day)
                assignments.append('Responsável B')

# Criar DataFrame
schedule_df = pd.DataFrame({
    'Data': days,
    'Dia da Semana': [day.strftime('%A') for day in days],
    'Responsável': assignments
})

# Formatar data
schedule_df['Data'] = schedule_df['Data'].dt.strftime('%d/%m/%Y')

# Mostrar resultado
print(schedule_df.head(28))  # Mostra as 4 primeiras semanas (28 dias)
