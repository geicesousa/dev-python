import calendar
import locale # para setar a localização
import json
import string

locale.setlocale(locale.LC_ALL, '') # sem passar nada do segundo argumento, usa a localização padrão do SO

calendario = calendar.calendar(2024)
print(calendario)

# comando para saber o padrão do SO -> locale -a
print(locale.getlocale()) # local e codificador/charset

def conversao_para_real(numero: float | int) -> str:
    brl = locale.currency(val=numero, symbol=True, grouping=True)
    return brl

print(conversao_para_real(500))

criando_dicionario = dict(
    nome='Akin',
    patrimonio=conversao_para_real(10042021),
    ano_nascimento=2021,
    aniversario= '10/04'
)
print(criando_dicionario)

print()
frase = '''Olá $nome, esperamos que tudo esteja bem!
O dia $aniversario esta chegando, seu aniversário.
Gostaríamos de informar que seu patrimônio esta avaliado em ${patrimonio}
'''

template = string.Template(frase)
substituicao = template.substitute(criando_dicionario)
# safe_substitute garante que não de erro caso não haja a variável

print(substituicao)

print()
print('frase de um arquivo:')
with open('string_template.txt', 'r') as arquivo:
    template = string.Template(arquivo.read())
    print(template.safe_substitute(criando_dicionario))
    