def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    elif x < y: 
        return -1
    
import math 

def area(radius):
    return math.pi * radius**2

def distance(x1,x2,y1,y2):
    value_x = (x2-x1)**2
    value_y = (y2-y1)**2

    return math.sqrt(value_x + value_y)

def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))

def is_between(x,y,z):
    if x <= y <= z:
        return True
    else:
        return False
    
def fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

instancia_de = isinstance('0', int)
print(instancia_de)
print(90**2)