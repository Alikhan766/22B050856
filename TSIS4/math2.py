def trapezoid(z, x, y):
    A = (x+y)/2 * z
    return A


h = 5
a = 5
b = 6
print('Height:', h, '\nBase, first value:', a, '\nBase,second value:', b)
print('Expected Output:', trapezoid(h, a, b))
