import turtle
bob = turtle.Turtle()

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length * n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2 * angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length * n)

#draw(bob, 15, 15)

# fd avance
# bk para trás
# lt esquerda
# rt direita
# pu caneta para cima (não escreve)
# pd caneta para baixo (escreve)
    
def koch(t, x):
    if x < 3:
        t.fd(x)
        return
    
    else:
        koch(t, x/3)
        t.lt(60)
        koch(t, x/3)
        t.rt(120)
        koch(t, x/3)
        t.lt(60)
        koch(t, x/3)

#koch(bob, 500)

def koch2(t, n): #original
    """Draws a koch curve with length n."""

    if n < 10:
        t.fd(n)
        return
    m = n/3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)

koch2(bob, 90)


def snowflake(t, sn): 
       for i in range(3):
        koch2(t, sn)
        t.rt(120)
  

snowflake(bob, 50)