def generator(n):
    for i in range(0, n)[::-1]:
        yield i


for j in generator(10):
    print(j)
