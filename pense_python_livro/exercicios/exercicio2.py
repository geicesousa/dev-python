# PEMDAS - parênteses, exponenciação, multiplicação, divisão, adição e subtração (ordem da operações)

# + e * funcionam em strings
print('geice'*3)
print('geice' + 'sousa')
# print('geice' + 3) TypeError: can only concatenate str (not "int") to str

# erro semântico é erro de lógica
# erro de sintaxe é erro de escrita na linguagem
# erro de execução é quando o programa lança uma exceção ao ser executado

x = r = 1
p = 9
print(r)
print(x)

# 42 = n -> TypeError: can only concatenate str (not "int") to str

# Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias?
print()
qtd = 60
valor_do_desconto_por_livro = 24.95 * 0.4
frete_exemplar_adicional = 0.75 * 59
frete = 3.00
desconto_total = valor_do_desconto_por_livro * qtd
valor_inicial_todos_livros = 24.95 * qtd

print(valor_do_desconto_por_livro)
print(frete_exemplar_adicional)
print(valor_inicial_todos_livros)
print(desconto_total)

custo_total_atacado = valor_inicial_todos_livros - desconto_total
print(custo_total_atacado) 
print()

print(f'''*** O valor das {qtd} cópias com o frete incluso será R$ {custo_total_atacado + frete + frete_exemplar_adicional:.2f}
Sendo os livros R$ {custo_total_atacado:.2f} e o frete R${frete + frete_exemplar_adicional:.2f}''')
