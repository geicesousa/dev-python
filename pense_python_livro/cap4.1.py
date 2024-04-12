import turtle
bob = turtle.Turtle()
# print(bob)
# desenho de um quadrado
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(110)
turtle.mainloop()


# fd avance
# bk para trás
# lt esquerda
# rt direita
# pu caneta para cima (não escreve)
# pd caneta para baixo (escreve)



for i in range(4):
    bob.fd(100)
    bob.lt(90)
turtle.mainloop()

