from math import tan, pi


def fc(x, y):
    z = x * (y ** 2) / (4 * tan(pi / x))
    return z


n_sides = 4
s_length = 25

print('Input number of sides:', n_sides, '\nInput the length of a side:', s_length)
print("The area of the polygon is: ", int(fc(n_sides, s_length)))
