from datetime import datetime, timedelta 

from dateutil.relativedelta import relativedelta
from pytz import timezone

data2 = datetime(2020,9,10)
data = datetime(2023,9,10)
data_hora = datetime(2019,9,10,8,15)
data_hora_tokyo = datetime(2019,9,10,8,15, tzinfo=timezone('Asia/Tokyo'))
data3 = datetime(2022,9,10)
print(data)
print(data_hora)
print('tokio:', data_hora_tokyo)
print()

array = [data, data2, data3]
print(sorted(array))
print()

print(datetime.now())
print(datetime.now(timezone('US/Eastern')))
print(datetime.now(timezone('Asia/Tokyo')))
print()

data_timestamp = (data.timestamp())
print(data_timestamp)
print(datetime.fromtimestamp(data_timestamp))
print()

# timedelta irá somar e diminuir datas e acrescentar dias, horas, min, etc a uma data
delta = timedelta(days=5, hours=2, minutes=1)
print(data + delta)
print(data - delta)
# relativedelta é mais completo
print()
print('**********************************Datas e parcelas de empréstimo**********************************')
print()

valor_emprestimo = 1_000_000 # um milhão, colocar o _ facilita a leitura, segue sendo um inteiro
data_emprestimo = datetime(2020,12,20)
delta_anos = relativedelta(years=5)
data_final_emprestimo = data_emprestimo + delta_anos

datas_parcelas = []
data_da_parcela = data_emprestimo
while data_da_parcela < data_final_emprestimo:
    datas_parcelas.append(data_da_parcela)
    data_da_parcela += relativedelta(months=+1)
    
valor_parcela = valor_emprestimo / len(datas_parcelas)


for data in datas_parcelas:
    print(f'''Data de pagamento: {data.strftime('%d-%m-%Y')}, Valor da parcela: {valor_parcela:.2f}''')