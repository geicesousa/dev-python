# naive sem fuso horário; aware com fuso horário (timezone)
from datetime import date, datetime, timedelta, timezone

minutos = 30
hora = 1
hora_em_min = 60
data_atual = datetime.now()

print(f''' {data_atual - timedelta(minutes=minutos)}
{data_atual - timedelta(hours=hora)}
{data_atual - timedelta(hours=hora_em_min)}
{data_atual + timedelta(minutes=minutos)}
{data_atual + timedelta(hours=hora)}
{data_atual + timedelta(hours=hora_em_min)}
{data_atual + timedelta(days=2)}
{date.today()}
''')

# utcnow() é naive
