from __future__ import print_function, division

import turtle

from polygon import arc


def petal(t, r, angle):
    """Desenha uma pétala usando dois arcos.

     t: Tartaruga
     r: raio dos arcos
     ângulo: ângulo (graus) que subtende os arcos
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)


def flower(t, n, r, angle):
    """Desenha uma flor com n pétalas.

     t: Tartaruga
     n: número de pétalas
     r: raio dos arcos
     ângulo: ângulo (graus) que subtende os arcos
    """
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)

def move(t, length):
    """Mova a Tartaruga (t) para frente (comprimento) das unidades sem deixar rastro.
     Deixa a caneta abaixada.
    """
    t.pu()
    t.fd(length)
    t.pd()

bob = turtle.Turtle()

move(bob, 100)
# flower(turtle.Turtle(), 7, 50, 90)

move(bob, 100)
flower(bob, 25, 150.0, 25.0)

# draw a sequence of three flowers, as shown in the book.
# move(bob, -100)
# flower(bob, 7, 60.0, 60.0)

# move(bob, 100)
# flower(bob, 10, 40.0, 80.0)

# move(bob, 100)
# flower(bob, 20, 140.0, 20.0)

bob.hideturtle()
turtle.mainloop()