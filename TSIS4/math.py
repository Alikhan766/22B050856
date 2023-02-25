import math


def fc(n):
    m = n * (math.pi/180)
    return m


a = 15
print('Input degree:', a)
print('Output radian:', fc(a))
