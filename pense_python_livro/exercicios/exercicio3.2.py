def twice(p):
    print(p)
    print(p)
# 2
def do_twice(f, x):
    f(x)
    f(x)

def print_args(args):
    print(args)


do_twice(print_args, 'geice')
print()

# 4
do_twice(print_args, 'spam')
print()

# 5 Defina uma função nova chamada do_four que receba um objeto de função e um valor e chame a função quatro vezes, passando o valor como um parâmetro. Deve haver só duas afirmações no corpo desta função, não quatro.

def do_four(f,x):
    f(x)
    f(x)
# chamar to_twice
    
do_four(twice, 'geice')