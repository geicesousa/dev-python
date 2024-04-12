import turtle 

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
        
    t.mainloop()


bob = turtle.Turtle()

# square(bob, 150)
# square(bob, 250)
# square(bob, 500)

# fd avance
# bk para trás
# lt esquerda
# rt direita
# pu caneta para cima (não escreve)
# pd caneta para baixo (escreve)

def polygon(n, t, length):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
        
    t.mainloop()

# polygon(5, bob, 80)

# n = nº de lados
# t = turtle    
# length = cumprimento de cada lado
 

def circle(t, r):
   # length * n = circumference.
    n = 100
    circumference = 2 * r

    polygon(n, t, circumference/n)
  
# circle(bob, 250)
    
def arc(t, r, angle):
    arc_length = 2 * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

arc(bob, 60, 180) 
arc(bob, 80, 280) 

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle2(t, r):
    arc(t, r, 360)