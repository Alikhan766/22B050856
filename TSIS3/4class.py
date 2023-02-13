from math import sqrt


class Point:
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init


p1 = Point(10, 3)
p2 = Point(4, -5)


def show(a, b):
    return (a.x, a.y), (b.x, b.y)


def move(a, b):
    return (a.x-1, a.y+2), (b.x-2, b.y+1)


def distance(a, b):
    return sqrt((a.x-b.x)**2+(a.y-b.y)**2)


print ("Method show: ", show(p1, p2))
print("Method move: ", move(p1, p2))
print("Method dist: ", distance(p1, p2))
