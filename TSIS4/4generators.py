def squares(a, b):
    for i in range(a, b):
        yield i


a = int(input())
b = int(input())
print(' ')
for j in squares(a, b):
    print(j)
