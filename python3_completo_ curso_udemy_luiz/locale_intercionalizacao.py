import calendar
import locale # para setar a localização

locale.setlocale(locale.LC_ALL, '') # sem passar nada do segundo argumento, usa a localização padrão do SO

calendario = calendar.calendar(2024)
print(calendario)

# comando para saber o padrão do SO -> locale -a
print(locale.getlocale()) # local e codificador/charset