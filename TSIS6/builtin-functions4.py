from time import sleep
import math


def delay(ms, args):
    sleep(ms / 1000)
    return math.sqrt(args)


a = 25100
b = 2123
print("Square root of {0} after {1} specific miliseconds is:".format(a, b))
print(delay(2123, 25100))
