from __future__ import print_function, division

import math
import turtle


def draw_pie(t, n, r):
    """Desenha uma torta e depois se move para a posição à direita.

     t: Tartaruga
     n: número de segmentos
     r: comprimento dos raios radiais
    """
    polypie(t, n, r)
    t.pu()
    t.fd(r*2 + 10)
    t.pd()


def polypie(t, n, r):
    """Desenha uma pizza dividida em segmentos radiais.

     t: Tartaruga
     n: número de segmentos
     r: comprimento dos raios radiais
    """
    angle = 360.0 / n
    for i in range(n):
        isosceles(t, r, angle/2)
        t.lt(angle)


def isosceles(t, r, angle):
    """Desenha um triângulo isósceles. A tartaruga começa e termina no topo, voltada para o meio da base. 
    t: Tartaruga 
    r: comprimento do ângulo das pernas iguais: meio ângulo do pico em graus
    """
    y = r * math.sin(angle * math.pi / 180)

    t.rt(angle)
    t.fd(r)
    t.lt(90+angle)
    t.fd(2*y)
    t.lt(90+angle)
    t.fd(r)
    t.lt(180-angle)


bob = turtle.Turtle()

# bob.pu()
# bob.bk(130)
# bob.pd()

isosceles(bob, 50, 150)

# draw polypies with various number of sides
size = 40
# draw_pie(bob, 5, size)
# draw_pie(bob, 6, size)
# draw_pie(bob, 7, size)
# draw_pie(bob, 8, size)

# bob.hideturtle()
turtle.mainloop()