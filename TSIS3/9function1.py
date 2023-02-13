import math


def sphere(r):
    V = (4/3) * math.pi * (r ** 3)
    return V


r = 5
V = sphere(r)
print(V)
