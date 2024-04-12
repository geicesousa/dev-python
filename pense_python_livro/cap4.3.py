# fd avance
# bk para trás
# lt esquerda
# rt direita
# pu caneta para cima (não escreve)
# pd caneta para baixo (escreve)

import turtle
#1
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
        
    t.mainloop()

# square(turtle)


bob = turtle.Turtle()

square(bob)
